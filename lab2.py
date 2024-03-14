import csv
import re
import random

with open('books.csv') as f:
    reader = csv.reader(f, delimiter=';')
    books = list(reader)
    sum = 0
    max = 30
    
    for book in books:
        book_name = book[1]
        if len(book_name) > max:
            sum+=1
    print(f'Количество записей, у которых в поле "Название" строка длиннее 30 символов: {sum}')
f.close ()

def find_book (s):
    with open('books.csv') as f:
        filtered_book = []
        date = []
        for book in books:
            title = book[1]
            author = book[3]
            full_author = book[4]
            date = book[6].replace(' ', '.').split('.')
            if ((s in author) or (s in full_author)) and (int(date[2])<=2016): #2 вариант
                filtered_book.append(title)
    return filtered_book    

s = input('Введите имя автора, которого вы хотите найти: ')
answer = find_book (s)
if len(answer)>0:
    print(f'Книги автора: {s}: {answer}')
else:
     print('Книги не найдены')


bibliography = []
with open('books.csv') as f:
    for line in f:
        bibliography.append(line.split(';'))
    
with open('txtfile.txt', 'w') as fmy:
    for i in range(20):
        num = random.randint(1, 9409)
        l = bibliography[num]
        author = l[3]
        name = l[1]
        date = l[6]
        fmy.write(f'{num}. {author}. {name} - {date[6:10]} \n')
fmy.close()

