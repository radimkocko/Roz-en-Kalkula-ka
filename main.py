def calculator():
	while True:
		cislo1 = float(input("Zadejte první číslo: "))
		operace = input("Zadejte operaci (+, -, *, /): ")
		cislo2 = float(input("Zadejte druhé číslo: "))
		
		if operace == '+':
			print(cislo1 + cislo2)
		elif operace == '-':
			print(cislo1 - cislo2)
		elif operace == '*':
			print(cislo1 * cislo2)
		elif operace == '/':
			if cislo2 != 0:
				print(cislo1 / cislo2)
			else:
				print("Tímto číslem dělit nelze!")

		pokracovat = input("Chcete pokračovat? (ano/ne): ")
		if pokracovat.lower() != 'ano':
			break

calculator()