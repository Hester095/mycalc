with open('poly_1.txt', 'w') as file:
    file.write('1 многочлен')
with open('poly_2.txt', 'w') as file:
    file.write('2 многочлен')

with open('poly_1.txt','r') as file:
    poly_1 = file.readline()
    list_of_poly_1 = poly_1.split()


with open('poly_2.txt','r') as file:
    poly_2 = file.readline()
    list_of_poly_2 = poly_2.split()

print(f'{list_of_poly_1} + {list_of_poly_2}')
sum_poly = list_of_poly_1 + list_of_poly_2

with open('sum_poly.txt', 'w') as file:
    file.write(f'{sum_poly}')