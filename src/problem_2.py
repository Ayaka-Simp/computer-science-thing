from decimal import Decimal

def drange(x: Decimal, y: Decimal, jump: Decimal):
  while x < y:
    yield round(float(x), 2)
    x += jump

def validate_input(a: float, b: float):
    if not a >= 50 or not a <= 200:
        return False
    elif not b >= 50 or not b <= 200:
        return False
    else:
        return True

def inputs():
    lowest = float(input("What is the lowest rate of the average heart beat? "))
    highest = float(input("What is the highest rate of the average heart beat? "))
    return lowest, highest

def calc_heart_rate(a: float, b: float):
    my_list = []
    thing = list(drange(Decimal(a), Decimal(b), Decimal(0.01)))
    for i in thing:
        my_list.append(round(i, 2))
        if not i-a==float(0) or not i-a == 0.05:
            my_list.remove(i)
    return my_list
    # return thing

def take_inputs_and_validate():
    a, b = inputs()
    valid = validate_input(a, b)
    while not valid:
        print("Invalid input. Try again.")
        a, b = inputs()
        valid = validate_input(a, b)
    
    return calc_heart_rate(a, b)

# print("\n".join(take_inputs_and_validate()))
print(take_inputs_and_validate())