def equation(x):
    return 2*x**11 - 3*x**8 - 5*x**3 - 1

def derivative(x):
    return 22*x**10 - 24*x**7 - 15*x**2

def newton_method(precision):
    x = 1.0  # 初始猜测值
    while True:
        x_next = x - equation(x) / derivative(x)
        if abs(x_next - x) < precision:
            break
        x = x_next
    return x_next

precision = 0.00000001
root = newton_method(precision)
print("根的近似值为:", root)