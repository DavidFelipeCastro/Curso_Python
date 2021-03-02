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
print("")

x = numero2.isdigit()
if numero2.isdigit():
	numero2 = int(numero2)




	while contador < 5 and numero2 != numeroRandom:
			

			print(f'-.-. Te quedan {intentos} intento/s -.-.') 
			numero2 = input("-Numero equivocado,intenta de nuevo: ")
			if numero2.isdigit():
				numero2 = int(numero2)
			else:
				print("Intenta con un numero porfavor.")
				print("Reinicia el programa.")
				break
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
else:
	print("Intenta con un numero por favor.")
		


if contador == 5 and numero2 != numeroRandom:
		print("")
		print("Numero de intentos alcanzado.")
		print("Game over")
		print("El numero random equivale a:",numeroRandom)  

if numero2 == numeroRandom:
	 print("")
	 print("Felicidades lo has logrado.")  
	 print("El numero random equivale a:",numeroRandom)  

	
 

