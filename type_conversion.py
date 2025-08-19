#input

x = input('first number:')
y = input('second number:')

toplam = x+y

print(toplam)

# output = if x is 10 and y is 20 , output will be 1020 
# so we have to convert types

#example : 
int_number = 4
float_number = 4.5
bool_ = True

#float to int
converted_float_to_int = int(float_number)
print(converted_float_to_int)
#int to float
converted_int_to_float = float(float_number)
print(converted_int_to_float)
#bool to int (1,0)
converted_bool_to_int = int(bool_)
print(converted_bool_to_int)

"""
HOME-WORK
Area of a circle = πr² (alan formülü)
Circumference of a circle = 2πr (çevre formülü)
Calculate the area and circumference of circle with given radius
yarıçapı verilen bir dairenin alan ve çevresini hesapla
"""

yaricap = float(input('Dairenin yarı çapı ? '))
pi = 3.14 
area = (yaricap ** 2) * pi
circumference = yaricap * 2 * pi
print ('area is : ' , area  )
print ('circumference is : ' , circumference  )
