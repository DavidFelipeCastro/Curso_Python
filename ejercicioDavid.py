import random
numeroRandom = random.randint(1, 100)
print("//Adivina el numero//")
print("")

print("")
print("¿Como se juega?")
print("")
print("-El sistema genera un numero random(1 - 100) que sera comparado con el numero que ingreses,")
print ("si estos coinciden abras ganado de lo contrario sera Game Over.")
print("")
print("")
contador = 0
intentos = 5
numero2 = input("Ingresa el numero:")
numero2 = int(numero2)

print("")



while contador < 5 and numero2 != numeroRandom:
	print(f'-.-. Te quedan {intentos} intento/s -.-.') 
	numero2 = input("-Numero equivocado,intenta de nuevo: ")
	numero2 = int(numero2)
	contador += 1
	intentos -= 1

	if numero2 > 0 and 100 >= numero2:
		

	
		if numero2 < numeroRandom:
			print("__________________________________________")
			print(f"Intenta con un numero mayor a {numero2}.")
			print("__________________________________________")



		elif numero2 > numeroRandom:
			print("__________________________________________")
			print(f"Intenta con un numero menor a {numero2}")  
			print("__________________________________________")  

		
	else:
		print("")
		print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
		print("Intenta con un numero dentro de el rango establecido (1-100)")
		print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
		print("")
		numero2 = input("Ingresa el numero:")
		contador += 1

	

if contador == 5 and numero2 != numeroRandom:
	print("")
	print("Numero de intentos alcanzado.")
	print("Game over")

else:
	 print("")
	 print("Felicidades lo has logrado.")  

	
 

print("El numero random equivale a:",numeroRandom)  