import numpy as np
MatrizCi = np.zeros((100,100))
print("<< PRUEBA NUMPY  >>")
cedula = input("Ingrese su número de cédula: ")
num_separados = []
for q in cedula:
    num_separados.append(q)

for i in range(100):
    MatrizCi[i][0] = num_separados[0]
    MatrizCi[i][1] = num_separados[1]
    MatrizCi[i][2] = num_separados[2]
    MatrizCi[i][3] = num_separados[3]
    MatrizCi[i][4] = num_separados[4]
    MatrizCi[i][5] = num_separados[5]
    MatrizCi[i][6] = num_separados[6]
    MatrizCi[i][7] = num_separados[7]
    MatrizCi[i][8] = num_separados[8]
    MatrizCi[i][9] = num_separados[9]
    MatrizCi[i][10] = num_separados[0]
    MatrizCi[i][11] = num_separados[1]
    MatrizCi[i][12] = num_separados[2]
    MatrizCi[i][13] = num_separados[3]
    MatrizCi[i][14] = num_separados[4]
    MatrizCi[i][15] = num_separados[5]
    MatrizCi[i][16] = num_separados[6]
    MatrizCi[i][17] = num_separados[7]
    MatrizCi[i][18] = num_separados[8]
    MatrizCi[i][19] = num_separados[9]
    MatrizCi[i][20] = num_separados[0]
    MatrizCi[i][21] = num_separados[1]
    MatrizCi[i][22] = num_separados[2]
    MatrizCi[i][23] = num_separados[3]
    MatrizCi[i][24] = num_separados[4]
    MatrizCi[i][25] = num_separados[5]
    MatrizCi[i][26] = num_separados[6]
    MatrizCi[i][27] = num_separados[7]
    MatrizCi[i][28] = num_separados[8]
    MatrizCi[i][29] = num_separados[9]
    MatrizCi[i][30] = num_separados[0]
    MatrizCi[i][31] = num_separados[1]
    MatrizCi[i][32] = num_separados[2]
    MatrizCi[i][32] = num_separados[3]
    MatrizCi[i][34] = num_separados[4]
    MatrizCi[i][35] = num_separados[5]
    MatrizCi[i][36] = num_separados[6]
    MatrizCi[i][37] = num_separados[7]
    MatrizCi[i][38] = num_separados[8]
    MatrizCi[i][39] = num_separados[9]
    MatrizCi[i][40] = num_separados[0]
    MatrizCi[i][41] = num_separados[1]
    MatrizCi[i][42] = num_separados[2]
    MatrizCi[i][43] = num_separados[3]
    MatrizCi[i][44] = num_separados[4]
    MatrizCi[i][45] = num_separados[5]
    MatrizCi[i][46] = num_separados[6]
    MatrizCi[i][47] = num_separados[7]
    MatrizCi[i][48] = num_separados[8]
    MatrizCi[i][49] = num_separados[9]
    MatrizCi[i][50] = num_separados[0]
    MatrizCi[i][51] = num_separados[1]
    MatrizCi[i][52] = num_separados[2]
    MatrizCi[i][3] = num_separados[3]
    MatrizCi[i][54] = num_separados[4]
    MatrizCi[i][55] = num_separados[5]
    MatrizCi[i][56] = num_separados[6]
    MatrizCi[i][57] = num_separados[7]
    MatrizCi[i][58] = num_separados[8]
    MatrizCi[i][59] = num_separados[9]
    MatrizCi[i][60] = num_separados[0]
    MatrizCi[i][61] = num_separados[1]
    MatrizCi[i][62] = num_separados[2]
    MatrizCi[i][63] = num_separados[3]
    MatrizCi[i][64] = num_separados[4]
    MatrizCi[i][65] = num_separados[5]
    MatrizCi[i][66] = num_separados[6]
    MatrizCi[i][67] = num_separados[7]
    MatrizCi[i][68] = num_separados[8]
    MatrizCi[i][69] = num_separados[9]
    MatrizCi[i][70] = num_separados[0]
    MatrizCi[i][71] = num_separados[1]
    MatrizCi[i][72] = num_separados[2]
    MatrizCi[i][73] = num_separados[3]
    MatrizCi[i][74] = num_separados[4]
    MatrizCi[i][75] = num_separados[5]
    MatrizCi[i][76] = num_separados[6]
    MatrizCi[i][77] = num_separados[7]
    MatrizCi[i][78] = num_separados[8]
    MatrizCi[i][79] = num_separados[9]
    MatrizCi[i][80] = num_separados[0]
    MatrizCi[i][81] = num_separados[1]
    MatrizCi[i][82] = num_separados[2]
    MatrizCi[i][83] = num_separados[3]
    MatrizCi[i][84] = num_separados[4]
    MatrizCi[i][85] = num_separados[5]
    MatrizCi[i][86] = num_separados[6]
    MatrizCi[i][87] = num_separados[7]
    MatrizCi[i][88] = num_separados[8]
    MatrizCi[i][89] = num_separados[9]
    MatrizCi[i][90] = num_separados[0]
    MatrizCi[i][91] = num_separados[1]
    MatrizCi[i][92] = num_separados[2]
    MatrizCi[i][93] = num_separados[3]
    MatrizCi[i][94] = num_separados[4]
    MatrizCi[i][95] = num_separados[5]
    MatrizCi[i][96] = num_separados[6]
    MatrizCi[i][97] = num_separados[7]
    MatrizCi[i][98] = num_separados[8]
    MatrizCi[i][99] = num_separados[9]

print(MatrizCi)

"""
num_separados = np.tile (num_separados,10)
X,Y = np.meshgrid(num_separados, MatrizCi[::-1])
print("\nMatriz de 100x 100:")
nuevaM = np.zeros((100,100))
nuevaM = X
print(nuevaM)
"""
opc = 0
while opc < 1 or opc >= 6:
    print("\n << MENU DE OPCIONES  >>")
    print("1. Sumar elementos de una columna")
    print("2. Sumar elementos de una fila")
    print("3. Sumar elementos de una diagonal")
    print("4. Multiplicar elementos de una columna")
    print("5. Multiplicar elementos de una fila")
    print("6. Multiplicar elementos de una diagonal")
    opc = int (input ("Seleccione una opción: "))

if opc == 1:
    suma = 0
    col = int (input("Indique la columna cuyos elementos desea sumar: "))
    for i in range (100):
        suma += MatrizCi[i][col -1]
    print("Suma de la columna ", col, " : ", suma)
if opc == 2:
    suma = 0
    fila = int (input("Indique la fila cuyos elementos desea sumar: "))
    for i in range (100):
        suma += MatrizCi[fila -1 ][i]
    print("Suma de la fila ", fila , " : ", suma)
if opc == 3:
    print ("Suma de una diagonal:")
    suma = 0
    for i in range (100):
        for j in range (100):
            if i == j:
                suma += MatrizCi[i][i]
    print("Suma de la diagonal  : ", suma)
if opc == 4:
    col = int (input("Indique la columna cuyos elementos desea multiplicar: "))
    multi = 0
    for i in range(100):
        multi *= MatrizCi[i][col - 1]
    print("Multiplicación de la columna ", col, " : ", multi)
if opc == 5:
    multi = 0
    fila = int(input("Indique la fila cuyos elementos desea multiplicar: "))
    for i in range(100):
        multi *= MatrizCi[fila - 1][i]
    print("Multiplicación de la fila ", fila, " : ", multi)
if opc == 6:
    print("Multiplicación de una diagonal:")
    multi = 0
    for i in range(100):
        for j in range(100):
            if i == j:
                multi *= MatrizCi[i][i]
    print("Multiplicación de la diagonal  : ", multi)


