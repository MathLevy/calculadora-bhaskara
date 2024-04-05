import math

a = float(input("\nDigite o coeficiente a: "))
b = float(input("Digite o coeficiente b: "))
c = float(input("Digite o coeficiente c: "))
print()

delta = (b * b) - (4 * a * c)

if delta < 0:
    print("Não existe raíz real")

elif delta == 0:
    x = (-b) / (2 * a)
    print(f"x= {x:.4f}")

else:
    x1 = ((-b) + math.sqrt(delta)) / (2 * a)
    x2 = ((-b) - math.sqrt(delta)) / (2 * a)
    print(f"x¹= {x1:.4f}")
    print(f"x²= {x2:.4f}")

print("\nFIM DO CÁLCULO\n")
