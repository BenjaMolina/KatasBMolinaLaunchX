# Añadir el código necesario para crear una variable que guarde la velocidad del asteroide.
# Escribe una expresión de prueba para calcular si necesita una advertencia.
# Agregue las instrucciones que se ejecutarán si la expresión de prueba es true o false.

vAsteroide = 49
if vAsteroide > 25:
    print("Asteroide Demasiado Rapido")
else:
    print("No pasa nada")


# Agrega el código para crear una variable para un asteroide que viaja a 19 km/s
# Escribe varias expresiones de prueba para determinar si puedes ver el rayo de luz desde la tierra
# Agrega las instrucciones que se ejecutarán si las expresiones de prueba son True o False

vAsteroide = 19
if vAsteroide >= 20:
    print("Rayo de Luz")
else:
    print("......")


# Agrega el código para crear nuevas variables para la velocidad y el tamaño del asteroide
# Para probar el código, prueba con varias velocidades y tamaños
# Escribe varias expresiones de prueba o combinaciones de expresiones de prueba para determinar qué mensaje se debe enviar a Tierra.

tamanoAsteroide = 20
vAsteroide = 25

if (tamanoAsteroide > 25 and tamanoAsteroide < 1000) and vAsteroide > 25:
    print("Causar mucho Daño")
elif vAsteroide >= 20:
    print("Hay un rayo de luz")
else:
    print("No pasa nada")

