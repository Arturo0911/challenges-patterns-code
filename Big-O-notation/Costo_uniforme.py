# viaje por carretera con busqueda de coste uniforme.
from Nodo import Nodo
from functools import cmp_to_key


def compara(x, y):
    return x.get_costo() - y.get_costo()


def Busqueda_Costo_Uniforme(conexiones, estado_inicial, solucion):
    solucionado = False
    nodos_visitados = []
    nodos_frontera = []
    nodo_inicial = Nodo(estado_inicial)
    nodo_inicial.set_costo(0)
    nodos_frontera.append(nodo_inicial)

    while (not solucionado) and len(nodos_frontera) != 0:
        # ordenar la lista de nodos fronteras
        nodos_frontera = sorted(nodos_frontera, key=cmp_to_key(compara))
        nodo = nodos_frontera[0]
        # extraer nodo y añadirlo a visitados.
        nodos_visitados.append(nodos_frontera.pop(0))
        if nodo.get_datos() == solucion:
            # solucion encontrada
            solucionado = True
            return nodo
        else:
            # expandir nodos hijo (ciudades de conexion)
            dato_nodo = nodo.get_datos()
            lista_hijos = []
            for un_hijo in conexiones[dato_nodo]:
                hijo = Nodo(un_hijo)
                coste = conexiones[dato_nodo][un_hijo]
                hijo.set_costo(nodo.get_costo() + coste)
                lista_hijos.append(hijo)
                if not hijo.en_lista(nodos_visitados):
                    # si esta en la lista lo sustituimos con el nuevo valor de coste si es menos:
                    if hijo.en_lista(nodos_frontera):
                        for n in nodos_frontera:
                            if n.igual(hijo) and n.get_costo() > hijo.get_costo():
                                nodos_frontera.remove(n)
                                nodos_frontera.append(hijo)
                    else:
                        nodos_frontera.append(hijo)
                        nodo.set_hijos(lista_hijos)


if __name__ == "__main__":

    conexiones = {
        'A': {'B': 15, 'C': 10, 'D': 23},
        'B': {'E': 6},
        'C': {'E': 6, 'F': 8},
        'D': {'F': 8},
        'E': {'B': 15, 'C': 10, 'F': 8, 'G': 12},
        'F': {'C': 10, 'D': 23, 'E': 6, 'H': 15, 'I': 8},
        'G': {'E': 6, 'H': 15, 'Z': 4},
        'H': {'F': 8, 'I': 8, 'G': 12, 'Z': 4},
        'I': {'F': 8, 'H': 15, 'Z': 4}

    }
    estado_inicial = "A"
    solucion = "Z"
    nodo_solucion = Busqueda_Costo_Uniforme(
        conexiones, estado_inicial, solucion)
    # mostrar resultado
    resultado = []
    nodo = nodo_solucion

    while nodo.get_padre() != None:
        resultado.append(nodo.get_datos())
        nodo = nodo.get_padre()
    resultado.append(estado_inicial)
    resultado.reverse()
    print(resultado)
    print('costo uniforme d', nodo_solucion.get_costo())
