from models.calculator import Calculator

calculator = Calculator()

result = calculator.sum(1, 2) + calculator.subtract(2, 1) + calculator.multiply(2, 2)

print(result)