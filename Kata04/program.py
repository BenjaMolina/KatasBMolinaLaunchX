text = """Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. 
On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight temperature of the Moon is 127 C."""


pClaves = ["average", "temperature","distance"]
text_split = text.split('.')

for palabra in text_split:
    for clave in pClaves:
        if clave in palabra:
            print(palabra)
            print("\n")
            break

for palabra in text_split:
    for clave in pClaves:
        if clave in palabra:
            print(palabra.replace(' C', ' Celsius'))
            break

# ----------------------------------------------------------------

planeta = 'Marte '
gravedad  = 0.00143
nombre = 'Ganímedes'

titulo = f'datos de gravedad sobre {nombre}'

body = f"""{'-'*80} 
Nombre del planeta: {planeta} 
Gravedad en {nombre}: {gravedad * 1000} m/s2 
"""

template = f"""
{titulo.title()} 
{body} 
""" 
print(template)


new_template = """
Datos de Gravedad sobre: {nombre}
-------------------------------------------------------------------------------
Nombre del planeta: {planeta}
Gravedad en {nombre}: {gravedad} m/s2
"""
print(new_template.format(nombre=nombre, planeta=planeta, gravedad=gravedad*1000))
