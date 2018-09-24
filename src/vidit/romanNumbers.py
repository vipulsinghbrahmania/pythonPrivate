#program to print a number to roman number
Ones 		= ['I',	'II',	'III',	'IV',	'V',	'VI',	'VII',	'VIII',	'IX',	'']
Tens 		= ['X',	'XX',	'XXX',	'XL',	'L',	'LX',	'LXX',	'LXXX',	'XC',	'']
Hundreds 	= ['C',	'CC',	'CCC',	'CD',	'D',	'DC',	'DCC',	'DCCC',	'CM',	'M',	'']

#n = int(input("Enter number:\n"))
n = 499
ones = int(n % 10)
tens = int(((n % 100) - ones) / 10)
hundreds = int(((n % 1000) -tens -ones) / 100)

roman = Hundreds[hundreds-1] + Tens[tens-1] + Ones[ones-1]

print(n,"=",roman)