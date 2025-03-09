#print('\033[36m\033[1mПідтвердження особистості')
#print ('='*25,'\033[0m\n')
#ans='1'
#while ans=='1':
# for kol in range(3):
#  age=int(input('Ваш вік:'))
# if age >=0 and age <14:
#     print('Свідоцтво про народження')
# elif 14<=age<=35:
#    print('id-паспорт')
# elif 35<age<=110:
#     print('паспорт старого зразку')
# else:
#     print('Помилка у введені віку')
# print('\033[0m')
# ans=input('Продовжити (1-так | 2-ні)')


print('\033[36m\033[1mВизначення оцінки студента')
print('=' * 30, '\033[0m\n')

ans = '1'
while ans == '1':
    for _ in range(3):
        score = input('Введіть кількість балів:')
        if score.isdigit():
            score = int(score)
            if 0 <= score <= 49:
                print('Незадовільно')
            elif 50 <= score <= 69:
                print('Задовільно')
            elif 70 <= score <= 89:
                print('Добре')
            elif 90 <= score <= 100:
                print('Відмінно')
            else:
                print('Помилка у введенні балів')
        else:
            print('Помилка: введіть число!')

    print('\033[0m')
    ans = input('Продовжити (1 - так | 2 - ні): ')

print('========END========')