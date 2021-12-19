def take_inputs():
    print("The following data is for Monday")
    a = int(float(input("What is your heartbeat at 10:00? ")))
    b = int(float(input("What is your heartbeat at 11:00? ")))
    c = int(float(input("What is your heartbeat at 12:00? ")))
    d = int(float(input("What is your heartbeat at 13:00? ")))
    e = int(float(input("What is your heartbeat at 14:00? ")))
    f = int(float(input("What is your heartbeat at 15:00? ")))
    g = int(float(input("What is your heartbeat at 16:00? ")))


    print("The following data is for Tuesday")
    h = int(float(input("What is your heartbeat at 10:00? ")))
    i = int(float(input("What is your heartbeat at 11:00? ")))
    j = int(float(input("What is your heartbeat at 12:00? ")))
    k = int(float(input("What is your heartbeat at 13:00? ")))
    l = int(float(input("What is your heartbeat at 14:00? ")))
    m = int(float(input("What is your heartbeat at 15:00? ")))
    n = int(float(input("What is your heartbeat at 16:00? ")))


    print("The following data is for Wednesday")
    o = int(float(input("What is your heartbeat at 10:00? ")))
    p = int(float(input("What is your heartbeat at 11:00? ")))
    q = int(float(input("What is your heartbeat at 12:00? ")))
    r = int(float(input("What is your heartbeat at 13:00? ")))
    s = int(float(input("What is your heartbeat at 14:00? ")))
    t = int(float(input("What is your heartbeat at 15:00? ")))
    u = int(float(input("What is your heartbeat at 16:00? ")))



    print("The following data is for Thursday")
    v = int(float(input("What is your heartbeat at 10:00? ")))
    w = int(float(input("What is your heartbeat at 11:00? ")))
    x = int(float(input("What is your heartbeat at 12:00? ")))
    y = int(float(input("What is your heartbeat at 13:00? ")))
    z = int(float(input("What is your heartbeat at 14:00? ")))
    aa = int(float(input("What is your heartbeat at 15:00? ")))
    ab = int(float(input("What is your heartbeat at 16:00? ")))


    print("The following data is for Friday")
    ac = int(float(input("What is your heartbeat at 10:00? ")))
    ad = int(float(input("What is your heartbeat at 11:00? ")))
    ae = int(float(input("What is your heartbeat at 12:00? ")))
    af = int(float(input("What is your heartbeat at 13:00? ")))
    ag = int(float(input("What is your heartbeat at 14:00? ")))
    ah = int(float(input("What is your heartbeat at 15:00? ")))
    ai = int(float(input("What is your heartbeat at 16:00? ")))
    return [[a, b, c, d, e, f, g], [h, i, j, k, l, m, n], [o, p, q, r, s, t, u], [v, w, x, y, z, aa, ab], [ac, ad, ae, af, ag, ah, ai]]

def validate_inputs(input_thing):
    if not input_thing >= 50:
        return False
    elif not input_thing <= 200:
        return False
    else:
        return True

# list_of_inputs = take_inputs()

list_of_inputs = [[60, 75, 70.50, 73, 120.25, 150.00, 70], [60, 75, 70.50, 73, 120.25, 150.00, 70], [60, 75, 70.50, 73, 120.25, 150.00, 70], [60, 75, 70.50, 73, 120.25, 150.00, 70], [60, 75, 70.50, 73, 120.25, 150.00, 70]]

pipes = []

pipes.append("Your average rate of heart beat in the office is:")
pipes.append("\n")

def print_pipes_monday():
    inputs = []
    for thing in list_of_inputs[0]:
        inputs.append(thing)
    pipes.append("Monday")
    pipes.append("\n")
    for i in inputs:
       value = "|" * (int((round(i, -1))/10))
       pipes.append(value)

def print_pipes_tuesday():
    inputs = []
    for thing in list_of_inputs[1]:
       inputs.append(thing)
    pipes.append("Tuesday")
    pipes.append("\n")
    for i in inputs:
       value = "|" * (int((round(i, -1))/10))
       pipes.append(value)

def print_pipes_wednesday():
    inputs = []
    for thing in list_of_inputs[2]:
       inputs.append(thing)
    pipes.append("Wednesday")
    pipes.append("\n")
    for i in inputs:
       value = "|" * (int((round(i, -1))/10))
       pipes.append(value)

def print_pipes_thursday():
    inputs = []
    for thing in list_of_inputs[3]:
       inputs.append(thing)
    pipes.append("Thursday")
    pipes.append("\n")
    for i in inputs:
       value = "|" * (int((round(i, -1))/10))
       pipes.append(value)

def print_pipes_friday():
    inputs = []
    for thing in list_of_inputs[4]:
        inputs.append(thing)
    pipes.append("Friday")
    pipes.append("\n")
    for i in inputs:
        value = "|" * (int((round(i, -1))/10))
        pipes.append(value)

def print_pipes():
    print_pipes_monday()
    pipes.append("\n")
    print_pipes_tuesday()
    pipes.append("\n")
    print_pipes_wednesday()
    pipes.append("\n")
    print_pipes_thursday()
    pipes.append("\n")
    print_pipes_friday()
    pipes.append("\n")
    for i in list_of_inputs:
        for thing in i:
            if not validate_inputs(thing):
                print("Invalid input! Please try again")
            else:
                continue
    print('\n'.join(pipes))

print_pipes()
# print(pipes)
"""
68
75
70.50
73
120.25
150.00
70
"""