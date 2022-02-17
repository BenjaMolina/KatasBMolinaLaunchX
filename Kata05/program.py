# Crear variables para almacenar las dos distancias
# ¡Asegúrate de quitar las comas!

primerPlaneta = 149597870
segundoPlaneta = 778547200

# Calcular la distancia entre planetas

distancia = segundoPlaneta - primerPlaneta
print(distancia)

millas = distancia * 0.621
print(millas)


# Almacenar las entradas del usuario
primerPlaneta = input('Distancia desde sol para el primer planeta en KM')
segundoPlaneta = input('Distancia desde el sol para el segundo planeta en KM')

# Convierte las cadenas de ambos planetas a números enteros
primerPlaneta = int(primerPlaneta)
segundoPlaneta = int(segundoPlaneta)

# Realizar el cálculo y determinar el valor absoluto
distancia = segundoPlaneta - primerPlaneta
print(distancia)

# Convertir de KM a Millas
millas = distancia * 0.621
print(millas)