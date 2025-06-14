import math

class SmartCalculator:
    def __init__(self):
        self.history = []

    def _record(self, operation, result):
        self.history.append({"operation": operation, "result": result})

    def add(self, a, b):
        result = a + b
        self._record(f"{a} + {b}", result)
        return result

    def subtract(self, a, b):
        result = a - b
        self._record(f"{a} - {b}", result)
        return result

    def multiply(self, a, b):
        result = a * b
        self._record(f"{a} * {b}", result)
        return result

    def divide(self, a, b):
        if b == 0:
            result = "Error: Division by zero"
        else:
            result = a / b
        self._record(f"{a} / {b}", result)
        return result

    def power(self, a, b):
        result = a ** b
        self._record(f"{a} ** {b}", result)
        return result

    def modulus(self, a, b):
        if b == 0:
            result = "Error: Modulus by zero"
        else:
            result = a % b
        self._record(f"{a} % {b}", result)
        return result

    def sqrt(self, x):
        if x < 0:
            result = "Error: Square root of negative number"
        else:
            result = math.sqrt(x)
        self._record(f"sqrt({x})", result)
        return result

    def log(self, x):
        if x <= 0:
            result = "Error: Logarithm undefined for non-positive numbers"
        else:
            result = math.log(x)
        self._record(f"log({x})", result)
        return result

    def evaluate_expression(self, expression):
        try:
            result = eval(expression, {"__builtins__": None, "sqrt": math.sqrt, "log": math.log, "pow": pow, "abs": abs, "round": round, "math": math})
        except ZeroDivisionError:
            result = "Error: Division by zero"
        except Exception:
            result = "Error: Invalid expression"
        self._record(f"evaluate({expression})", result)
        return result
