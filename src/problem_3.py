def take_inputs():
   a = int(float(input("What is your heartbeat at 10:00? ")))
   b = int(float(input("What is your heartbeat at 11:00? ")))
   c = int(float(input("What is your heartbeat at 12:00? ")))
   d = int(float(input("What is your heartbeat at 13:00? ")))
   e = int(float(input("What is your heartbeat at 14:00? ")))
   f = int(float(input("What is your heartbeat at 15:00? ")))
   g = int(float(input("What is your heartbeat at 16:00? ")))
   return [a, b, c, d, e, f, g]

def validate_inputs(input_thing):
    if not input_thing >= 50 or not input_thing <= 200:
        return False
    return True
    

def print_pipes():
   inputs = []
   for thing in take_inputs():
        if validate_inputs(thing):
           inputs.append(thing)
        else:
            print("Invalid input! Please try again.")
            return print_pipes()
   pipes = ["Your average rate of heart beat in the office is:", "\n"]
   for i in inputs:
       value = "|" * (int((round(i, -1))/10))
       pipes.append(value)
   print("\n".join(pipes))

print_pipes()