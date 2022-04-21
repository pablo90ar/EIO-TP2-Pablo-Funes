# Módulo EXERCISE
# Este módulo contiene la entidad utilizada para almacenar todos los datos relevantes de un ejercicio de transporte

# Clase Exercise: utilizada para cargar y manipular los datos de un ejercicio que provienen del archivo "Problems.json"
# Esta clase define el esquema, estructura o molde de la tabla de asignación de un ejercicio práctico
class Exercise:
    number: int = 0  # El número de ejercicio en la guía
    pre_prompt: str  # Consigna del problema antes de la tabla
    post_prompt: str  # Consigna del problema después de la tabla
    orig_type: str  # Nombre de la columna orígen
    orig_name: list  # Nombres de los orígenes
    dest_type: str  # Nombre de la fila de destinos
    dest_name: list  # Nombres de los destinos
    offer_type: str  # Nombre de la columna de oferta
    demand_type: str  # Nombre de la fila de demanda
    cost: list  # cost[i][j] Es el valor del costo de transporte en el casillero con coordenada "ij"
    demand: list  # Lista de cantidades demandadas en destinos
    offer: list  # Lista de cantidades disponibles en orígenes

    def __init__(self):
        self.number = 0
        self.pre_prompt = ""
        self.post_prompt = ""
        self.orig_type = ""
        self.orig_name = []
        self.dest_type = ""
        self.dest_name = []
        self.offer_type = ""
        self.demand_type = ""
        self.cost = []
        self.demand = []
        self.offer = []

    # Función que devuelve el número de columnas de la tabla de costos de un ejercicio
    def get_column_num(self):
        return len(self.cost[0])

    # Función que devuelve el número de filas de la tabla de costos de un ejercicio
    def get_row_num(self):
        return len(self.cost)

    # Referencia de las variables usadas:
    """
    +--------------+------------------------------------------------------------+-------------+
    |              |                     dest_type                              |             |
    +--------------+------------------------------------------------------------+-------------+
    |  orig_type   | dest_name[0]   dest_name[1]   dest_name[2]   dest_name[n]  | offer_type  |
    +--------------+------------------------------------------------------------+-------------|
    | orig_name[0] |  cost[0][0]     cost[0][1]     cost[0][2]     cost[0][n]   |  offer[0]   |
    | orig_name[1] |  cost[1][0]     cost[1][1]     cost[1][2]     cost[1][n]   |  offer[1]   |
    | orig_name[2] |  cost[2][0]     cost[2][1]     cost[2][2]     cost[2][n]   |  offer[2]   |
    | orig_name[n] |  cost[n][0]     cost[n][1]     cost[n][2]     cost[n][n]   |  offer[n]   |
    +--------------+------------------------------------------------------------+-------------+
    | demand_type  |  demand[0]      demand[1]      demand[2]      demand[n]    |             |
    +--------------+------------------------------------------------------------+-------------+
    """