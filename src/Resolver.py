import Printer
import pprint
from Exercise import Exercise
from pulp import LpProblem, LpMinimize, LpStatus, LpVariable, lpSum, value
pp = pprint.PrettyPrinter()

# Módulo RESOLVER
# Este módulo contiene funciones utilizadas para la resolución de ejercicios


# Esta función toma como parámetro el objeto tipo "Exercise" y realiza el cálculo de optimización con la librería PuLP
def resolve(ex: Exercise):
    # Borra la consola
    Printer.clear_console()
    Printer.print_exercise_title(ex.number)
    # Muestra los valores del ejercicio en formato pedido por PuLP
    print("\nOrígenes: " + str(ex.orig_name))
    print("\nDestinos: " + str(ex.dest_name))
    offer = {}
    for i in range(ex.get_row_num()):
        offer.update({ex.orig_name[i]: ex.offer[i]})
    print("\nOferta: " + str(offer))
    demand = {}
    for i in range(ex.get_column_num()):
        demand.update({ex.dest_name[i]: ex.demand[i]})
    print("\nDemanda: " + str(demand))
    cost = {}
    for i in range(ex.get_row_num()):
        cost.update({ex.orig_name[i]: {}})
        for j in range(ex.get_column_num()):
            cost[ex.orig_name[i]].update({ex.dest_name[j]: ex.cost[i][j]})
    print("\nCostos:")
    pp.pprint(cost)

    # Inicia el cálculo del ejercicio
    problem = LpProblem("Transporte", LpMinimize)
    routes = [(i, j) for i in ex.orig_name for j in ex.dest_name]
    amount = LpVariable.dicts("Cantidades", (ex.orig_name, ex.dest_name), 0)
    problem += lpSum(amount[i][j] * cost[i][j] for (i, j) in routes)
    # Restricciones
    for j in ex.dest_name:
        problem += lpSum(amount[i][j] for i in ex.orig_name) == demand[j]
    # Restricciones
    for i in ex.orig_name:
        problem += lpSum(amount[i][j] for j in ex.dest_name) <= offer[i]
    Printer.press_enter_to("calcular y mostrar los resultados")
    # Resolución final del ejercicio
    problem.solve()
    Printer.clear_console()
    Printer.print_exercise_title(ex.number)
    print("Solución:")
    print("Status:", LpStatus[problem.status])
    # Impresión de la solución
    for v in problem.variables():
        if v.varValue > 0:
            print(v.name, "=", v.varValue)
    print("El costo mínimo es:", value(problem.objective))
    # Vuelve al menú principal
    Printer.press_enter_to("volver al menú")
