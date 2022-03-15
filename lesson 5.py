#items = ['sword','shield']
#
#for item in items:
#    for i in range(4):
#        print(f'{item} - {i}')
#x = int(input('Введите число: '))
#y = 1
#while y*y !=x:
#    y = (y+x/y)/2
#print(y)
interes = int(input('под какой процент вы кладете деньги: '))
saving = int(input('колько вы хотите положить в банк: '))
time = int(input('На сколько вы хотите положить лет деньги в банк: '))
for i in range(time) :
     saving = ((saving/100)*interes)+saving
print(saving)
#saving += saving * interes
