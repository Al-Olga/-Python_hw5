# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# RLE означает “run-length encoding” — это способ сокращённой записи 
# последовательности чего угодно (в случае этой задачи — цифр), 
# при котором для подряд идущих группы одинаковых цифр (run) записываются 
# длина этой группы (run length) и сама эта цифра. Таким образом, 
# “99999” превратится в “5 9” («пять девяток»), и так далее.

# Входные и выходные данные хранятся в отдельных текстовых файлах.

# создаем файл
with open('file_text.txt','w') as my_file:
    my_file.write('111111444443333377777rrrrrdddddaaaaa')

# читаем из файла
my_file = open('file_text.txt','r') 
string = my_file.read()
my_file.close()

# кодируем
new_text = []
count = 1
for i in range(len(string)-1):
    if i <= len(string):
        if string[i] == string[i + 1]:
            count += 1
        else:
            a = string[i]
            new_text.append(str(count) + ' ' + string[i])
            count = 1
new_text.append(str(count) + ' ' + string[i])

# записываем код в файл
with open('file_code.txt','w') as my_file:
    my_file.write(','.join(new_text))

#читаем код из файла
my_file = open('file_code.txt','r') 
text = my_file.read().split(',')
my_file.close()

# раскодируем
new_text = []
text_cod = ''
for word in text:
    new_text = word.split(' ')
    text_cod=text_cod+(str(new_text[1])*int(new_text[0]))

with open('file_code_out.txt','w') as my_file:
    my_file.write(text_cod)
