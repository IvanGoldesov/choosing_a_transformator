import requests
import csv
from bs4 import BeautifulSoup



def parser(url : str):

    create_csv()
    req = requests.get(f'{url}')
    soup = BeautifulSoup(req.text, 'lxml')

    #Создаём списки для хранения данных об двухобмоточных, трёхобмоточных трансформаторах и автотрансформаторах
    list_trans_double_winding = [[]]
    length_list_trans_double_winding = 0

    list_trans_three_winding = [[]]
    length_list_trans_three_winding = 0
    

    list_autotrans = [[]]
    length_list_autotrans = 0

    #Процесс парсинга
    transformators_info = soup.find_all('table', class_ = 'wikitable')


    for info in transformators_info:
        transformators = info.find_all('tr')
        
        #Забираем название таблицы с сайта
        number_of_windings = info.find('caption').text

        #В зависимости от кол-ва обмоток разбиваем и делим их
        if 'двухобмоточные' in number_of_windings:
            for num, trans in enumerate(transformators):
                if num < 3:
                    continue

                for j in trans.find_all('td'):

                    text_tr = j.text.strip().replace(u'\xa0%', u' %')
                    list_trans_double_winding[length_list_trans_double_winding].append(text_tr)
                
                if list_trans_double_winding[length_list_trans_double_winding]:
                    length_list_trans_double_winding += 1 
                    list_trans_double_winding.append([])
        else:
            for num, trans in enumerate(transformators):
                flag_three_winding = True
                flag_autotrans = False
                if num < 3:
                    continue

                for j in trans.find_all('td'):

                    text_tr = j.text.strip().replace(u'\xa0%', u' %').replace(u'\xa0г.', u' г.')

                    #Разделяем на трёхобмоточный трансформатор и автотрансформатор
                    if text_tr.startswith('А'):
                        flag_three_winding = False
                        flag_autotrans = True

                    if flag_autotrans:
                        list_autotrans[length_list_autotrans].append(text_tr)
                        
                    elif flag_three_winding:
                        list_trans_three_winding[length_list_trans_three_winding].append(text_tr)
                
                if list_trans_three_winding[length_list_trans_three_winding]:
                    length_list_trans_three_winding += 1 
                    list_trans_three_winding.append([])
                
                if list_autotrans[length_list_autotrans]:
                    length_list_autotrans += 1
                    list_autotrans.append([])


#________________________________________________________________________________________________________________________________________________________________________________________
    #Обработка запроса

    del list_trans_double_winding[length_list_trans_double_winding]
    del list_trans_three_winding[length_list_trans_three_winding]
    del list_autotrans[length_list_autotrans]


    #Последняя таблица на сайте продолжение предпоследней. Поэтому объединяем данные и удаляем лишнюю таблицу из списка
    for i in range(11, (len(list_autotrans) - 9)):
        list_autotrans[i].extend(list_autotrans[i + 9][2:])

    del list_autotrans[20:]


    #Добавляем в последнюю таблицу двухобмоточых трансформаторов столбец (предела регулирования)
    for i in range(60, len(list_trans_double_winding)):
        list_trans_double_winding[i].insert(2, '-')

    #Добавляем пределы регулирования автотрансформаторов  и проценты передачи мощности по сторонам автотрансформатора
    for i in range(5, 11):
        if list_autotrans[i][1] == '240':
            list_autotrans[i].insert(2, '-')
            list_autotrans[i].insert(6, '100')
            list_autotrans[i].insert(7, '100')
            list_autotrans[i].insert(8, '25')
        elif list_autotrans[i][1] == '200' or list_autotrans[i][1] == '250':
            list_autotrans[i].insert(2, '±6*2 %')
            list_autotrans[i].insert(6, '100')
            list_autotrans[i].insert(7, '100')
            list_autotrans[i].insert(8, '40')
        elif list_autotrans[i][1] == '133':
            list_autotrans[i].insert(2, '±6*2 %')
            list_autotrans[i].insert(6, '100')
            list_autotrans[i].insert(7, '100')
            list_autotrans[i].insert(8, '25')
        else:
            list_autotrans[i].insert(2, '±6*2 %')
            list_autotrans[i].insert(6, '100')
            list_autotrans[i].insert(7, '100')
            list_autotrans[i].insert(8, '50')


    
    # Убираем у трехобмоточных трансформаторов лишние столбцы в которых нет данных
    for i in range(9, len(list_trans_three_winding)):
        del list_trans_three_winding[i][10:12]

    #Добавляем пределы регулирования для трансформаторов
    for i in range(9):
        if  list_trans_three_winding[i][0].startswith('ТДТНЖ') and list_trans_three_winding[i][1] == '40':
            list_trans_three_winding[i].insert(2, '±8*1,5 %')
        else:
            list_trans_three_winding[i].insert(2, '±9*1,78 %')

    #Создаём csv файлы для хранения данных
    append_to_csv_transformators(list_trans_double_winding, list_trans_three_winding)
    append_to_csv_autotrans(list_autotrans)


#Создание сsv файла, с названием полей
def create_csv() -> None:
    with open('double_winding_transformatorts.csv', 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(
            (
                'Тип',
                'Sном, МВА',
                'Пределы регулирования',
                'Uном.обм ВН кВ',
                'Uном.обм НН кВ',
                'Uк, %',
                'ΔРк, кВт',
                'Рх, кВт',
                'Iх, %',
                'Rт, Ом',
                'Хт, Ом',
                'ΔQх, квар'
            )
        )

    with open('three_winding_transformatorts.csv', 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(
            (
                'Тип',
                'Sном, МВА',
                'Пределы регулирования',
                'Uном.обм ВН кВ',
                'Uном.обм CН кВ',
                'Uном.обм НН кВ',
                'Uк В-С, %',
                'Uк В-Н, %',
                'Uк С-Н, %',
                'ΔРк, кВт',
                'Рх, кВт',
                'Iх, %',
                'Rт ВН, Ом',
                'Rт СН, Ом',
                'Rт НН, Ом',
                'Хт ВН, Ом',
                'Хт СН, Ом',
                'Хт НН, Ом',
                'ΔQх, квар'
            )
        )

        with open('autotransformators.csv', 'w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(
                (
                    'Тип',
                    'Sном, МВА',
                    'Пределы регулирования',
                    'Uном.обм ВН кВ',
                    'Uном.обм СН кВ',
                    'Uном.обм НН кВ',
                    'Uк В-С, %',
                    'Uк В-Н, %',
                    'Uк С-Н, %',
                    'ΔРк В-С, кВт',
                    'ΔРк В-Н, кВт',
                    'ΔРк С-Н, кВт',
                    'Рх, кВт',
                    'Iх, %',
                    'Rт ВН, Ом',
                    'Rт СН, Ом',
                    'Rт НН, Ом',
                    'Хт ВН, Ом',
                    'Хт СН, Ом',
                    'Хт НН, Ом',
                    'ΔQх, квар'
                )
            )


#Добавляем в csv файл парсенный сайт
def append_to_csv_transformators(transformators_double_winding : list[list], transformators_three_winding : list[list]) -> None:
    with open('double_winding_transformatorts.csv', 'a', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(transformators_double_winding)
    
    with open('three_winding_transformatorts.csv', 'a', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        for num, trans in enumerate(transformators_three_winding):
            if num == 8:
                writer.writerow(['При Хт обмотки СН, равном нулю, обмотки НН изготавливаются с Uном, равным 6,3 или 10,5 кВ.']+[''*18])
                writer.writerow(())
            writer.writerow(trans)


#Добавляем в csv файл парсенный сайт
def append_to_csv_autotrans(autotransformators : list[list]) -> None:
    with open('autotransformators.csv', 'a', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        for num, trans in enumerate(autotransformators):
            if num == 5:
                writer.writerow(())
                writer.writerow(
                    (
                    'Тип',
                    'Sном, МВА',
                    'Пределы регулирования',
                    'Uном.обм ВН кВ',
                    'Uном.обм СН кВ',
                    'Uном.обм НН кВ',
                    'S обмоток ВН, %',
                    'S обмоток СН, %',
                    'S обмоток НН, %',
                    'Uк В-С, %',
                    'Uк В-Н, %',
                    'Uк С-Н, %',
                    'ΔРк В-С, кВт',
                    'ΔРк В-Н, кВт',
                    'ΔРк С-Н, кВт',
                    'Рх, кВт',
                    'Iх, %',
                    'Rт ВН, Ом',
                    'Rт СН, Ом',
                    'Rт НН, Ом',
                    'Хт ВН, Ом',
                    'Хт СН, Ом',
                    'Хт НН, Ом',
                    'ΔQх, квар' 
                    )
                )
            elif num == 11:
                writer.writerow(())
                writer.writerow(
                    (
                    'Тип',
                    'Sном, МВА',
                    'Пределы регулирования',
                    'Uном.обм ВН кВ',
                    'Uном.обм СН кВ',
                    'Uном.обм НН кВ',
                    'S обмоток ВН, %',
                    'S обмоток СН, %',
                    'S обмоток НН, %',
                    'Uк В-С, %',
                    'Uк В-Н, %',
                    'Uк С-Н, %',
                    'ΔРк ВНСН, кВт',
                    'Рх, кВт',
                    'Iх, %',
                    'Rт ВН, Ом',
                    'Rт СН, Ом',
                    'Rт НН, Ом',
                    'Хт ВН, Ом',
                    'Хт СН, Ом',
                    'Хт НН, Ом',
                    'ΔQх, квар' 
                    )
                )
        
            writer.writerow(trans)


if __name__ == '__main__':
    parser(url = 'https://powersystem.info/index.php?title=%D0%A1%D0%BF%D1%80%D0%B0%D0%B2%D0%BE%D1%87%D0%BD%D1%8B%D0%B5_%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D0%B5_%D0%BF%D0%B0%D1%80%D0%B0%D0%BC%D0%B5%D1%82%D1%80%D0%BE%D0%B2_%D1%82%D1%80%D0%B0%D0%BD%D1%81%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%82%D0%BE%D1%80%D0%BE%D0%B2_%D0%BE%D1%82_35_%D0%BA%D0%92')
