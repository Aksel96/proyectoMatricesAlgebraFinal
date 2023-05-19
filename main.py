#   AKSEL VILLELA ANDRADE, ARTURO IVAN AZUARA OCOTITLA, ELIEZER ISAI MONROY QUINTERO
#   FES ARAGON
#   ICO
#   ALGEBRA LINEAL
#   PROYECTO FINAL
#   MAYO 2023
import os

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')


def producto_matriz(matrizUno, matrizDos):
    filasUno, columnasUno = len(matrizUno), len(matrizUno[0])
    filasDos, columnasDos = len(matrizDos), len(matrizDos[0])
    if columnasUno != filasDos:
        return False
    resultado = [[0 for j in range(columnasDos)] for i in range(filasUno)]
    for i in range(filasUno):
        for j in range(columnasDos):
            valor = 0
            for k in range(columnasUno):
                valor += matrizUno[i][k] * matrizDos[k][j]
            resultado[i][j] = valor
    return resultado


def resta_matriz(matrizUno, matrizDos):
    n = len(matrizUno)
    n2 = len(matrizUno[0])
    resultado = [[0 for j in range(n2)] for i in range(n)]
    for i in range(n):
        for j in range(n2):
            valor = matrizUno[i][j] - matrizDos[i][j]
            resultado[i][j] = valor
    return resultado


def suma_matriz(matrizUno, matrizDos):
    n = len(matrizUno)
    n2 = len(matrizUno[0])
    resultado = [[0 for j in range(n2)] for i in range(n)]
    for i in range(n):
        for j in range(n2):
            valor = matrizUno[i][j] + matrizDos[i][j]
            resultado[i][j] = valor
    return resultado


def determinante_matriz(matriz):
    n = len(matriz)
    if n == 1:
        return matriz[0][0]
    elif n == 2:
        return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]
    else:
        det = 0
        for j in range(n):
            signo = (-1) ** j
            submatriz = [[matriz[i][k] for k in range(n) if k != j] for i in range(1, n)]
            det += signo * matriz[0][j] * determinante_matriz(submatriz)
        return det


def sistema_N_Dimensiones(matrizNDim, vectorResultados):
    n = len(matrizNDim)
    for p in range(n - 1):
        for j in range(p + 1, n):
            valor = -matrizNDim[j][p] / matrizNDim[p][p]
            for i in range(n):
                matrizNDim[j][i] = valor * matrizNDim[p][i] + matrizNDim[j][i]
            vectorResultados[j] = valor * vectorResultados[p] + vectorResultados[j]

    x = [0] * n
    for i in range(n - 1, -1, -1):
        suma = sum(matrizNDim[i][j] * x[j] for j in range(i, n))
        x[i] = (vectorResultados[i] - suma) / matrizNDim[i][i]

    return list(x)


def llenado_matriz(opcion, numFil=0):
    matriz = []
    matrizNDim = []
    vectorResultados = []
    for i in range(numFil):
        valMatriz = []
        if i == 0:
            print("----    Introduce los valores separados por un espacio")
            print("----    Ej: \" 3 3 2 \"")
        if opcion == "E" and i == 0:
            print("----    Ej: Si la ecuacion es 3x + 1y - 4z = 7, deberas colocar: \" 3 1 -4 7 \"")
        if opcion != "E":
            valUsuario = input("Valores de la fila {}: ".format(i + 1))
        else:
            valUsuario = input("Valores de la Ecuacion {}: ".format(i + 1))
        valFila = valUsuario.split(" ")
        for j in range(len(valFila)):
            valMatriz.append(int(valFila[j]))
        matriz.append(valMatriz)
        if opcion == "E":
            matrizNDim.append(valMatriz[0:-1])
            vectorResultados.append(valMatriz[-1])
    if opcion == "E":
        return matrizNDim, vectorResultados
    else:
        return matriz


def matrices_iguales(matrizUno, matrizDos):
    filasUno, columnasUno = len(matrizUno), len(matrizUno[0])
    filasDos, columnasDos = len(matrizDos), len(matrizDos[0])
    if filasUno != filasDos or columnasUno != columnasDos:
        return False
    for i in range(filasUno):
        if len(matrizUno[i]) != len(matrizDos[i]):
            return False
    return True


def pintar_matriz(matriz):
    for fila in matriz:
        print("[", end="")
        for elemento in fila:
            print(f"{elemento:4}", end="")
        print("]")


def menu():
    print("+---------------------------------------------------------------+")
    print("\t\tPROGRAMA GENERAL DE OPERACIONES CON MATRICES")
    print("+---------------------------------------------------------------+")
    print("Menu de opciones:")
    print("\t1) PRODUCTO de Dos Matrices")
    print("\t2) RESTA de Dos Matrices")
    print("\t3) SUMA de Dos Matrices")
    print("\t4) DETERMINATE de una Matriz")
    print("\t5) Solucion de Sistema de Ecuaciones de N Dimensiones")
    print("\t6) Limpiar la pantalla")
    print("\tX) SALIR")
    print("+---------------------------------------------------------------+")


def opcion_menu(opcion):
    match opcion:
        case "1":
            print("Obtencion del producto de dos matrices")
            print("Recuerda que para que el producto sea valido es necesario que el número de columnas de la primera "
                  "matriz sea igual al número de filas de la segunda matriz")
            num_filas = int(input("Introduce el numero de filas que tiene la primera matriz: "))
            matriz1 = llenado_matriz("C", num_filas)
            num_filas2 = int(input("Introduce el numero de filas que tiene la segunda matriz: "))
            matriz2 = llenado_matriz("C", num_filas2)
            resultado = producto_matriz(matriz1, matriz2)
            if not resultado:
                print("Las matrices no se pueden multiplicar")
            else:
                print("El resultado del PRODUCTO de dos matrices:")
                print("Matriz 1:")
                pintar_matriz(matriz1)
                print("Matriz 2:")
                pintar_matriz(matriz2)
                print("Matriz de resultado:")
                pintar_matriz(resultado)
        case "2":
            print("Resta de dos matrices")
            print("Recuerda que para que la resta sea valida, ambas matrices tienen que tener el mismo numero de "
                  "elementos")
            num_filas = int(input("Introduce el numero de filas que tienen las matrices: "))
            matriz1 = llenado_matriz("C", num_filas)
            matriz2 = llenado_matriz("C", num_filas)
            if matrices_iguales(matriz1, matriz2):
                resultado = resta_matriz(matriz1, matriz2)
                print("El resultado de la RESTA de dos matrices:")
                print("Matriz 1:")
                pintar_matriz(matriz1)
                print("Matriz 2:")
                pintar_matriz(matriz2)
                print("Matriz de resultado:")
                pintar_matriz(resultado)
            else:
                print("\t\t----------ERROR---------- "
                      "\nLas matrices no tienen los mismos elementos"
                      "\nVuelve a leer las instrucciones")
        case "3":
            print("Suma de dos matrices")
            print("Recuerda que para que la suma sea valida ambas matrices tienen que tener el mismo numero de "
                  "elementos")
            num_filas = int(input("Introduce el numero de filas que tienen las matrices: "))
            matriz1 = llenado_matriz("C", num_filas)
            matriz2 = llenado_matriz("C", num_filas)
            if matrices_iguales(matriz1, matriz2):
                resultado = suma_matriz(matriz1, matriz2)
                print("El resultado de la SUMA de dos matrices:")
                print("Matriz 1:")
                pintar_matriz(matriz1)
                print("Matriz 2:")
                pintar_matriz(matriz2)
                print("Matriz de resultado:")
                pintar_matriz(resultado)
            else:
                print("\t\t----------ERROR---------- "
                      "\nLas matrices no tienen los mismos elementos"
                      "\nVuelve a leer las instrucciones")

        case "4":
            print("Obtencion del Determinante de una matriz")
            num_filas = int(input("Introduce el numero de filas que tiene la Matriz: "))
            matriz = llenado_matriz("D", num_filas)
            determinante = determinante_matriz(matriz)
            print("El determinante de la matriz:")
            pintar_matriz(matriz)
            print(f"Es: {determinante}")

        case "5":
            print("Solucion de un sistema de ecuaciones de N dimensiones")
            print("Recuerda que le numero de incognitas tiene que ser el mismo que el de las ecuaciones")
            num_filas = int(input("Introduce el numero de Incognitas que tiene la matriz: "))
            matriz, vector_resultados = llenado_matriz("E", num_filas)
            print("Matriz de las incognitas:")
            pintar_matriz(matriz)
            print("Vector: {}".format(vector_resultados))
            if determinante_matriz(matriz) == 0:
                print("La matriz no tiene solucion o tiene multiples soluciones")
            else:
                resultadoMatriz = sistema_N_Dimensiones(matriz, vector_resultados)
                print("El valor de las incognitas en orden es el siguiente: {}".format(resultadoMatriz))
        case "6":
            clearConsole()
        case "X":
            print("\nAdios...")
        case other:
            print("Opcion no valida :/")


def main():
    while True:
        menu()
        opcion = input("Introduce la opcion: ")
        opcion_menu(opcion)
        if opcion.upper() == "X":
            break
    print("\n\t\t#######\tGracias por usar el Programa :D\t#######")


if __name__ == '__main__':
    main()
