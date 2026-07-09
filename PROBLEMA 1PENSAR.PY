S = float(input("ingrese su salario base: "))
salud = S * 0.04
pension = S * 0.04
SF = S - salud - pension
print("Su salario final es igual: ", SF)