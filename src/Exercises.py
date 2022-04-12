"""
Exercise example
|-----------------------------------------------------------------|
|           | dest_name0   dest_name1   dest_name2   dest_name(n) |
|-----------------------------------------------------------------|
|orig_name0 |    v00          v01          v02          v0n       |
|orig_name1 |    v10          v11          v12          v1n       |
|orig_name2 |    v20          v21          v22          v2n       |
|orig_namen |    vn0          vn1          vn2          vnn       |
|-----------------------------------------------------------------|

value(ij) = n
"""


# clase que define el esquema, estructura o molde de la tabla de asignacion de un ejercio práctico
class Exercise:
    number: int  # Número del ejercicio en la guía
    prompt_text: str  # Consigna del problema
    orig_name: list  # Nombres de los orígenes
    dest_name: list  # Nombres de los destinos
    orig_list: list  # Cantidades disponibles en orígenes
    dest_list: list  # Cantidades demandadas en destinos
    i: int  # Posición horizontal de coordenadas
    j: int  # Posición vertical de coordenadas
    value: list  # value[i][j] Es el valor en el casillero de coordenada "ij"
