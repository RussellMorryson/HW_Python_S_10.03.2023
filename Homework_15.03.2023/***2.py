# ***(2)У вас есть девять цифр: 1, 2, …, 9. Именно в таком порядке. 
# Вы можете вставлять между ними знаки «+», «-» или ничего. У вас 
# будут получаться выражения вида 123+45-6+7+89. Найдите все из них, которые равны 100.
from random import randint

NA = [1, 2, 3, 4, 5, 6, 7, 8, 9]    #Numbers Array
SA = ['+', '-', '']                 #Symbol Array
TVA = [' ']                         #Text variation array
TXT = [' ']
Summa = 0
count = 0
num_size = 0
while Summa != 100:
    text = ''
    for i in NA:
        s = randint(0, 2)
        c = randint(0, 1)
        if i == 1:
            text += f"{i}"
        else:
            if s == 2:
                num_size += 1
                if num_size >= 3:
                    text += f"{SA[c]}{i}"
                else: 
                    text += f"{SA[s]}{i}"
            else:
                text += f"{SA[s]}{i}"
    #print(text) 
    num_size = 0
    re = 0
    for i in TXT:
        if i == text:            
            continue
        else: 
            re += 1
    if re > 0:
        TXT.append(text)        
#==============================================================
    Buf = ''
    FSA = [0] #Fatal Sum Array
    for j in text:
        if j != '+' and j != '-'and j !='9':
            Buf += f"{j}"
        else:
            if j == '9':
                Buf += f"{j}"
                FSA.append(Buf)
                Buf =''
            else:
                FSA.append(Buf)
                Buf =''
#==============================================================
    for k in FSA:
        Summa += int(k)
        #print(Summa)
    if Summa == 100:
        TVA.append(text)
    Summa = 0
    count += 1
    print(count)
    if count == 100000:
        break
        

print("Результаты: ")
for h in TVA:
    print(h)
