txt1 = input('Digite algo: ')
print('O tipo primitivo desse valor é ',type(txt1))
print('Só tem espaços?', txt1.isspace())
print('É um número?', txt1.isnumeric())
print('É alfabético?', txt1.isalpha())
print('É alfanumérico?', txt1.isalnum())
print('Esta em maiúsculas?', txt1.isupper())
print('Está em minúsculas?', txt1.islower())
print('Está capitalizada?', txt1.istitle())