from datetime import timedelta, date, datetime
import sys

current_date = datetime.today().date()
print('Today is: ' + str(current_date.strftime('%d/%m/%Y')) + '\n')

correct_date = False # utilizando flag
#while True:
while not correct_date:    
    birthday = input('When is your birthday (dd/mm/yyyy)? ')
    try:
        birthday_date = datetime.strptime(birthday, '%d/%m/%Y').date()
        print('Birthday: ' + str(birthday_date.strftime('%d/%m/%Y')))
        delta_birth = (current_date - birthday_date).days
        # print(type(delta_birth)) # mostra o tipo
        if delta_birth < 0:
            #print('Please give a birthday date before ' + str(current_date)) 
            print(f'Please give a birthday date before {current_date}') # Format string, lembra?
            continue
        else:
            print('You have lived ' + str(delta_birth) + ' days until now. Use your remaining days wisely.')
            #break
            correct_date = True # alterei o valor da variavel, o que vai ser considerado ao reiniciar o loop
    except ValueError:
        print('Enter your birthday in asked format dd/mm/yyyy, please.')