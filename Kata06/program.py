planetas = ['Mercurio', 'Venus', 'Tierra', 'Marte', 'Jupiter', 'Saturno', 'Urano', 'Neptuno']

print('Existen', len(planetas), 'planetas')

planetas.append('Plutón')
print(planetas[-1], 'es el ultimo planeta')


planeta = input('Ingrese el nombre de un planeta (Usa una letra mayúscula para comenzar) ')
indice = planetas.index(planeta)

print(f'Plantas mas cercanos a: {planeta}')
print(planetas[0:indice])

print(f'Plantas mas Lejanos a: {planeta}')
print(planetas[indice+1:])