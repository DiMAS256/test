################################################################################
#
#	Utility from grad_converter.
#
#	Created:  Ishkinin Dmitrii, 26.03.2020
#	Modified: 
#
################################################################################

t = input("Введите температуру по цельсию: ")  

h = float(t)

g = float(1.8) * h + 32

print ('Температура по Фаренгейту: ' + str(g))

k = h + 273.15

print ('Температура по Кельвину: ' + k)

