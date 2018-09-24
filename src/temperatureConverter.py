def tempC(temp):
	f = temp * 9 / 5 + 32 
	k = temp + 273.15
	print(temp, 'C = ', f, 'F')
	print(temp, 'C = ', k, 'K')

def tempF(temp):
	c = temp - 32 * 5 / 9
	k = temp - 32 * 5 / 9 + 273.15
	print(temp, 'F = ', c, 'C')
	print(temp, 'F = ', k, 'K')

def tempK(temp):
	c = temp - 273.15 
	f = temp - 273.15 * 9 / 5 + 32
	print(temp, 'K = ', c, 'C')
	print(temp, 'K = ', f, 'F') 

# Main
choice = input('Choose input unit (F)ahrenheit, (C)elsius or (K)elvin :')
temp = int(input('Enter a temperature :'))

if choice == 'C':
	tempC(temp)
elif choice == 'F':
	tempF(temp)
elif choice == 'K':
	tempK(temp)
else:
	print('Invalid input')
