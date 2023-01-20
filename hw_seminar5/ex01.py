# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# Входные и выходные данные хранятся в отдельных текстовых файлах.

with open('my_file_ex.txt','w') as my_file:
    my_file.write('Забвение наступило быстро. В Зимбабве все бывает')

my_file = open('my_file_ex.txt','r') 
text = my_file.read().split(' ')
my_file.close()

print(text)

poisk_w = 'абв'
new_text = []
for word in text:
    if poisk_w not in word:
        new_text.append(word)
print(new_text)

with open('my_file_in.txt','w') as my_file:
    my_file.write(' '.join(new_text))