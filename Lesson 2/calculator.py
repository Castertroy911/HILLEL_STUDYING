# Можно реализовать ввод в одну строку,но потом нужно будет привести введенные значения к типу данных int().

# first_number, arithmetic_operation, second_number = input('Please, enter an expression. For example 1 + 1.'
#                                                           + '\n' + 'Allowed operations: *, /, -, + : ').split()

first_number = int(input('Please, enter the first number: '))
second_number = int(input('Please, enter the second number: '))
arithmetic_operation = input('Please, enter operation. Allowed operations: *, /, -, + : ')

if arithmetic_operation == '+':
    calculated_number = first_number + second_number
    print(f'Result is {calculated_number}')
elif arithmetic_operation == '-':
    calculated_number = first_number - second_number
    print(f'Result is {calculated_number}')
elif arithmetic_operation == '*':
    calculated_number = first_number * second_number
    print(f'Result is {calculated_number}')
elif int(second_number) == 0 and arithmetic_operation == '/':
    second_number = int(input('Zero division is impossible. Please, enter a valid value: '))
    calculated_number = first_number / second_number
    print(f'Result is {calculated_number}')
elif arithmetic_operation == '/':
    calculated_number = first_number / second_number
    print(f'Result is {calculated_number}')
else:
    print('Please, doublecheck entered operator. Allowed operations: *, /, -, +')
