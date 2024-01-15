import requests
import psycopg
from bs4 import BeautifulSoup

#Функция для парсинга сайта и получения значений из таблицы допустимых перегрузок трансформатора
def parser(url : str):

    req = requests.get(f'{url}')
    soup = BeautifulSoup(req.text, 'lxml')

    tables = soup.find_all('table')
    tables = tables[3:19]

    k_1 = [0.25, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    h = [0.5, 1.0, 2.0, 4.0, 6.0, 8.0, 12.0, 24.0]
    k2_M_D = []
    length_k2 = 0
    k2_DC_C = []

    temperature = {
        0 : '-20',
        1 : '-10',
        2 : '0',
        3 : '10',
        4 : '20',
        5 : '30',
        6 : '40',
        7 : '-20',
        8 : '-10',
        9 : '0',
        10 : '10',
        11 : '20',
        12 : '30',
        13 : '40',
        14 : '30',
        15 : '40'
    }

    temporary_data = []

    #Получение значений перегрузки
    for table in tables:
        strings = table.find_all('tr')[4:]

        for string in strings:
            datas = string.find_all('td')
            
            k2_M_D.append([])
            k2_DC_C.append([])

            for n, data in enumerate(datas):
                if n == 0:
                    continue
                temporary_data.append(data.find('p').text if data.find('p').text != '-' else 'None')

            k2_M_D[length_k2].extend(temporary_data[:8])
            k2_DC_C[length_k2].extend(temporary_data[8:])
            length_k2 += 1
            temporary_data.clear()
        

    #Скомпоновка данных для последующей передачи одним целым в базу данных
    count_start = 0
    count_end = 8
    
    for_sql_M_D = []
    for_sql_DC_C = []
    counter = 0

    #Собираем данные вместе
    while True:

        for j, k in zip(h, range(count_start, count_end)):
            for_sql_M_D.append(list(zip([temperature[counter]]*8, [j]*8, k_1, k2_M_D[k], ['М']*8, ['Д']*8)))

            for_sql_DC_C.append(list(zip([temperature[counter]]*8, [j]*8, k_1, k2_DC_C[k], ['ДЦ']*8, ['Ц']*8)))


        count_start = count_end
        count_end += 8
        counter += 1

        if len(for_sql_M_D) == 128:
            break

    return for_sql_M_D, for_sql_DC_C


#Функция для записи в базу данных всех необходимых таблиц
def create_data_sql(for_sql_M_D : list, for_sql_DC_C : list):

    insert_query_str_systems = f'''INSERT INTO kf_transformators_systems 
    (temperature, h, k_1, k_2, type_of_cooling_first, type_of_cooling_second) values
    (%s, %s, %s, %s, %s, %s);
    '''
    
    insert_query_str_accident = f'''INSERT INTO kf_transformators_acceptable 
    (temperature, h, k_1, k_2, type_of_cooling_first, type_of_cooling_second) values
    (%s, %s, %s, %s, %s, %s);
    '''
    
    try:
        connection = psycopg.connect(user = 'postgres',
                                    password = '12345678',
                                    host = '127.0.0.1',
                                    port = '5432',
                                    dbname = 'transformators_db',)
        connection.autocommit = True
        cursor = connection.cursor()
        
        for i in range(len(for_sql_M_D)):
            if i < 56:
                cursor.executemany(insert_query_str_systems, for_sql_M_D[i])
                cursor.executemany(insert_query_str_systems, for_sql_DC_C[i])
            else:
                cursor.executemany(insert_query_str_accident, for_sql_M_D[i])
                cursor.executemany(insert_query_str_accident, for_sql_DC_C[i])
            print(cursor.rowcount, 'Записи успешно добавлены')
    except (Exception, psycopg.Error) as error:
        print('Error at word with PostgerSQL', error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print('Connection with PostgerSQL is closed')       


if __name__ == '__main__':
    for_sql_M_D, for_sql_DC_C = parser('https://allgosts.ru/29/180/gost_14209-85')
    create_data_sql(for_sql_M_D, for_sql_DC_C)