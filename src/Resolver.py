import Printer
import pprint
from Exercise import Exercise
from pulp import *
import pandas as np

pp = pprint.PrettyPrinter()


def resolve(ex: Exercise):
    Printer.clear_console()
    print(ex.orig_type + ": " + str(ex.orig_name))
    print(ex.dest_type + ": " + str(ex.dest_name))
    print(ex.offer_type + ": " + str(ex.offer))
    print(ex.demand_type + ": " + str(ex.demand))

    # Suma toda la oferta
    total_offer = 0
    for i in range(ex.get_row_num()):
        total_offer += ex.offer[i]
    # Suma toda la demanda
    total_demand = 0
    for i in range(ex.get_column_num()):
        total_demand += ex.demand[i]
    # Verifica si la función está balanceada o no
    if not (total_offer == total_demand):
        print("\nFunción NO balanceada.\nOferta: " + str(total_offer) + "\nDemanda: " + str(total_demand))
        Printer.press_enter_to("volver al menú")
        return None
    else:
        print("\nFunción balanceada. Cantidad total: " + str(total_offer) + "\n")

    # Muestra los valores de la tabla en formato pedido por PuLP
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
    print("\nCantidades:")
    pp.pprint(cost)

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
    # Resolución
    problem.solve()
    Printer.clear_console()
    print("-----Solución-----")
    print("Status:", LpStatus[problem.status])
    # Impresión de la solucion
    for v in problem.variables():
        if v.varValue > 0:
            print(v.name, "=", v.varValue)
    print("El costo mínimo es:", value(problem.objective))

    Printer.press_enter_to("volver al menú")
