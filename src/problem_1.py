from decimal import Decimal
my_list: list[float] = [55.00, 55.05, 56.00, 56.05, 57.00, 57.05, 58.00, 57.05, 57.00, 56.05, 56.00, 55.05, 55.00]
float_var: float = 0.00
for i in my_list:
    float_var += i
float_var /= len(my_list)
print(round(Decimal(float_var), 2))