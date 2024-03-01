import sys

W = float(sys.argv[1])
H = float(sys.argv[2])/100

IMC = round(W / (H**2), 2)

if IMC >= 40:
    print(f'''
        Su IMC es {IMC}.
        La clasificación OMS es Obesidad Grado III
        ''')
elif IMC >= 35:
    print(f'''
    Su IMC es {IMC}.
    La clasificación OMS es Obesidad Grado II
    ''')
elif IMC >= 30:
    print(f'''
    Su IMC es {IMC}.
    La clasificación OMS es Obesidad Grado I
    ''')
elif IMC >= 25:
    print(f'''
    Su IMC es {IMC}.
    La clasificación OMS es Sobrepeso
    ''')
elif IMC >= 18.5:
    print(f'''
    Su IMC es {IMC}.
    La clasificación OMS es Adecuado
    ''')
else:
    print(f'''
    Su IMC es {IMC}.
    La clasificación OMS es Bajo Peso
    ''')