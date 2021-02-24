#Batalla contra la emperatriz de la luz
#El objetivo consiste en derrotar a la emperatriz de la luz con tus diferentes habilidades.

emperatrizdelaluz = {"nombre" : "Emperatriz de la luz","vida": 25000,  "daño" : 150, "habilidades" : ["embestida", "rayos","baile de el sol"]}
Jugador = {"nombre" : "Azucarconmelasu","vida" : 500 ,"daño":1500,"habilidades" :["flechas","mele","magia"]}

#la reina realiza el ataque baile solar

print("///La emperatriz usa baile solar se te adelanta y te ataca///")
print("")
Bailesolar = emperatrizdelaluz["habilidades"][2]
print("la emperatriz te da y sufres daño")
salud = Jugador["vida"]
daño = emperatrizdelaluz["daño"]
Salud1 = salud - daño
print("")
print ("Tu salud:" , Salud1)
print("")


#Turno de el jugador para atacar
AtaqueJ1 =Jugador["habilidades"][0]
DañoJ = Jugador["daño"]
 
VidaEm = emperatrizdelaluz["vida"]
print("Usas", AtaqueJ1 )
print("")
ConclusionAtq = VidaEm - DañoJ
print("Salud emperatriz:" ,ConclusionAtq)
print("")

#Turno de la emperatriz
print("La emperatriz falla su ataque")
#Turno de el jugador
print("")
print("Aprovechas la ocasion para hacer un combo.")
print("")
AtaqueJ2 = Jugador["habilidades"][1]
AtaqueJ3 = Jugador["habilidades"][2]

AtaqueJ2 = DañoJ
AtaqueJ3 = DañoJ

Combox2 = AtaqueJ2 + AtaqueJ3

ConclusionAtq2 = ConclusionAtq - Combox2
print("Salud Emperatriz:" ,ConclusionAtq2)

#la emperatriz usa embestida
embestida = emperatrizdelaluz["habilidades"][0]
embestida = daño
salud2 = Salud1 - embestida
print("Tu salud es:",salud2)

#El jugador queda aturdido por el ataque
#La emperatriz ataca otra vez

rayos = emperatrizdelaluz["habilidades"][1]
rayos = daño
salud3 = salud2 - rayos
print("Tu salud es:", salud3)

#se acerca la mañana y la emperatriz conserva la mayoria de su vida
#si la vida de la emperatriz es mayor a 15.000 ella se lleva esta contienda

resultado = ConclusionAtq2 > VidaEm
print(resultado)

print("")
nombrej = Jugador["nombre"]
print(nombrej , "a sido reducido a una bola de carne")





