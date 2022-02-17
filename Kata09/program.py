def reporte(tanque1, tanque2, tanque3):
    
    return f"""Reporte:
    Promedio: {promedio(tanque1, tanque2, tanque3)}%
    tanque1: {tanque1}%
    tanque2: {tanque2}%
    tanque3: {tanque3}% 
    """
def promedio(tanque1, tanque2, tanque3):
    return (tanque1 + tanque2 + tanque3) / 3


print(reporte(10, 20, 30))




def reporteCohete(destino, *minutes, **fuel_reservoirs):
    reporte = f"""
    mision a {destino}
    Total Viaje: {sum(minutes)} minutos
    Total Combustible: {sum(fuel_reservoirs.values())} galones
    """

    for tank_name, gallons in fuel_reservoirs.items():
        reporte += f"{tank_name} taqnue --> {gallons} galones\n"
    return reporte


print(reporteCohete("Luna", 8, 11, 55, main=300000, external=200000))