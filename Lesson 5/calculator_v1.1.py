class FormulaError(ValueError):
    pass


# Нашел это решение в интернете, сам о таком к сожалению не знал((
try:
    first_value, operand, second_value = input('Enter the formula: ').split()
    first_value = float(first_value)
    second_value = float(second_value)
except ValueError:
    raise FormulaError(f'Check the entered formula') from None
if operand != '+' and operand != '-':
    raise FormulaError(f'Operand should be "+" or "-". You enter "{operand}"')
elif operand == '+':
    print(first_value + second_value)
else:
    print(first_value - second_value)

