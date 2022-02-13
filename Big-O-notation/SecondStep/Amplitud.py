
from nodo import Nodo

def buscar_solucion_amplitud(estado_inicial, solucion):
    solucionado=False
    nodos_frontera=[]
    nodos_visitados=[]
    nodo_inicial=Nodo(estado_inicial)
    nodos_frontera.append(nodo_inicial)
    
    while (not solucionado) and len(nodos_frontera)!= 0:
        nodo= nodos_frontera.pop()

        nodos_visitados.append(nodo)

        if nodo.get_datos()== solucion:
            solucionado=True
            return nodo
        else:
            #Generar Hijos para Izq, Cent, Der
            dato_nodo = nodo.get_datos()
            
            #Izq [1.0.2.3]
            hijo=[dato_nodo[1], dato_nodo[0], dato_nodo[2], dato_nodo[3]]

            hijo_izquierdo=Nodo(hijo)
            if not hijo_izquierdo.en_lista(nodos_visitados) and not hijo_izquierdo.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_izquierdo)

            #Central [0.2.1.3]
            hijo=[dato_nodo[0], dato_nodo[2], dato_nodo[1], dato_nodo[3]]

            hijo_central=Nodo(hijo)
            if not hijo_central.en_lista(nodos_visitados) and not hijo_central.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_central)

            #Derecha [0.1.3.2]

            hijo=[dato_nodo[0], dato_nodo[1], dato_nodo[3], dato_nodo[2]]

            hijo_derecho=Nodo(hijo)
            if not hijo_derecho.en_lista(nodos_visitados) and not hijo_derecho.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_derecho)
        
        nodo.set_hijos([hijo_izquierdo, hijo_central, hijo_derecho])

if __name__=="__main__":
    estado_inicial = [3,2,4,1]
    solucion = [4,3,2,1]

    nodo_solucion = buscar_solucion_amplitud(estado_inicial,solucion)

    resultado=[]
    nodo=nodo_solucion

    while nodo.get_padre()!=None:
        resultado.append(nodo.get_datos())
        nodo=nodo.get_padre()
    resultado.append(estado_inicial)
    resultado.reverse()
    print(resultado)


