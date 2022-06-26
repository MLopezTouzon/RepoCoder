import sys



if len(sys.argv) == 3:
    nota_1 = float(sys.argv[1])
    nota_2 = float(sys.argv[2])
    if nota_1>=7 and nota_2>=7:
        print("Promocionado")
    elif nota_1>=4 and nota_2>=4:print("Aprobado")
    elif (nota_1<4 or nota_2<4) and (not (nota_1<4 and nota_2<4)):
        if nota_1<4:print("recupera el primer parcial")
        else:print("recupera el segundo parcial")
    else:print("desaprobo los 2 parciales")
else:print("Error, debe ingresar 2 notas")