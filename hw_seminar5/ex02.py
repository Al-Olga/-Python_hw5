# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# RLE означает “run-length encoding” — это способ сокращённой записи 
# последовательности чего угодно (в случае этой задачи — цифр), 
# при котором для подряд идущих группы одинаковых цифр (run) записываются 
# длина этой группы (run length) и сама эта цифра. Таким образом, 
# “99999” превратится в “5 9” («пять девяток»), и так далее.

# Входные и выходные данные хранятся в отдельных текстовых файлах.

with open('code_file_ex.txt','w') as my_file:
    my_file.write('111111444443333377777rrrrrdddddaaaaa')

my_file = open('code_file_ex.txt','r') 
string = my_file.read()
my_file.close()

new_text = []
count = 1
for i in range(len(string)-1):
    if i <= len(string):
        if string[i] == string[i + 1]:
            count += 1
        else:
            a = string[i]
            strk = str(count) + ' ' + string[i]
            new_text.append(strk)
            count = 1
strk = str(count) + ' ' + string[i]
new_text.append(strk)

with open('code_file_in.txt','w') as my_file:
    my_file.write(','.join(new_text))
