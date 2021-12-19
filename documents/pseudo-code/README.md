<h1 align=center>Problem 1</h1>
<h2 align=center>Find the average of heartbeat data.</h2>

### Create a list of all the heartbeats that are the following:
`my_list = [55.00, 55.05, 56.00, 56.05, 57.00, 57.05]` etc.<br>




<h1 align=center>Problem 2</h1>
<h2 align=center>generate heart rate data between two numbers.</h2>

### Define a function that validates input:
`def validate_input(a: float, b: float)`<br>
### Inside the function, check if data is between 50 and 200.
`if a is not greater than or equal to 50.00 or a is not smaller than or equal to 200.00: return False`<br>
`elif b is not greater than or equal to 50.00 or b is not smaller than or equal to 200.00: return False`<br>
`otherwise, return True`
### Define a function that inputs the highest and lowest values, and returns them
`def inputs():`<br>
`lowest = float(input("What is the lowest rate of the average heart beat?"))`<br>
`highest = float(input("What is the lowest rate of the average heart beat?"))`<br>
`return lowest, highest`<br>
### Define a function that calculates heart rate based on the lowest and the highest numbers.
`def calc_heart_rate(a: float, b: float):`<br>
`my_list = []`<br>
`thing = list(range(a, b))`<br>
`for i in thing:`<br>
`if not str(i).endswith("5"):`<br>
`my_list.remove(i)`<br>
`elif not str(i).endswith("0"):`<br>
`my_list.remove(i)`<br>
`elif not str(i)[-2] == 0:`<br>
`my_list.remove(i)`<br>
`return my_list`<br>
### Define another function that automatically validates the inputs, and asks again if not valid.
`def take_inputs_and_validate():`<br>
`a, b = inputs()`<br>
`if not validate_input(a, b): a, b = inputs()`<br>
`else: return calc_heart_rate(a, b)`<br>
### call take_inputs_and_validate and store in a variable
`my_list = take_inputs_and_validate()`<br>
### Print my_list joined with "\n"
`print("\n".join(my_list))`<br>

<h1 align=center>Problem 3</h1>
<h2 align=center>Calculate the graphics of the heart rates of someone.</h2>

### Take inputs with 10:00, 11:00, 12:00, 13:00, 14:00, 15:00 and 16:00 using a function.
`def take_inputs():`
`   a = int(float(input("What is your heartbeat at 10:00? )))`<br>
`   b = int(float(input("What is your heartbeat at 11:00? )))`<br>
`   c = int(float(input("What is your heartbeat at 12:00? )))`<br>
`   d = int(float(input("What is your heartbeat at 13:00? )))`<br>
`   e = int(float(input("What is your heartbeat at 14:00? )))`<br>
`   f = int(float(input("What is your heartbeat at 15:00? )))`<br>
`   g = int(float(input("What is your heartbeat at 16:00? )))`<br>
`   return [a, b, c, d, e, f, g]`<br>
### Make a function to print all the pipes
`def print_pipes(inputs)`<br>
`   pipes = ["Your average rate of heart beat in the office is:", "\n"]`<br>
`   for i in inputs:`<br>
`       value = "|" * ((round(i, -1))/10)`<br>
`       pipes.append(value)`<br>
`   print("\n".join(pipes))`<br>

<h1 align=center>Problem 4</h1>
<h2 align=center>Exactly the same as problem 3 except that it's repeated 5 times</h2>

### Take inputs with 10:00, 11:00, 12:00, 13:00, 14:00, 15:00 and 16:00 five times using a function.
`def take_inputs():`
`   print("The following data is for Monday")`
`   a = int(float(input("What is your heartbeat at 10:00? )))`<br>
`   b = int(float(input("What is your heartbeat at 11:00? )))`<br>
`   c = int(float(input("What is your heartbeat at 12:00? )))`<br>
`   d = int(float(input("What is your heartbeat at 13:00? )))`<br>
`   e = int(float(input("What is your heartbeat at 14:00? )))`<br>
`   f = int(float(input("What is your heartbeat at 15:00? )))`<br>
`   g = int(float(input("What is your heartbeat at 16:00? )))`<br>


`   print("The following data is for Tuesday")`
`   h = int(float(input("What is your heartbeat at 10:00? )))`<br>
`   i = int(float(input("What is your heartbeat at 11:00? )))`<br>
`   j = int(float(input("What is your heartbeat at 12:00? )))`<br>
`   k = int(float(input("What is your heartbeat at 13:00? )))`<br>
`   l = int(float(input("What is your heartbeat at 14:00? )))`<br>
`   m = int(float(input("What is your heartbeat at 15:00? )))`<br>
`   n = int(float(input("What is your heartbeat at 16:00? )))`<br>


`   print("The following data is for Wednesday")`
`   o = int(float(input("What is your heartbeat at 10:00? )))`<br>
`   p = int(float(input("What is your heartbeat at 11:00? )))`<br>
`   q = int(float(input("What is your heartbeat at 12:00? )))`<br>
`   r = int(float(input("What is your heartbeat at 13:00? )))`<br>
`   s = int(float(input("What is your heartbeat at 14:00? )))`<br>
`   t = int(float(input("What is your heartbeat at 15:00? )))`<br>
`   u = int(float(input("What is your heartbeat at 16:00? )))`<br>



`   print("The following data is for Thursday")`
`   v = int(float(input("What is your heartbeat at 10:00? )))`<br>
`   w = int(float(input("What is your heartbeat at 11:00? )))`<br>
`   x = int(float(input("What is your heartbeat at 12:00? )))`<br>
`   y = int(float(input("What is your heartbeat at 13:00? )))`<br>
`   z = int(float(input("What is your heartbeat at 14:00? )))`<br>
`   aa = int(float(input("What is your heartbeat at 15:00? )))`<br>
`   ab = int(float(input("What is your heartbeat at 16:00? )))`<br>


`   print("The following data is for Friday")`
`   ac = int(float(input("What is your heartbeat at 10:00? )))`<br>
`   ad = int(float(input("What is your heartbeat at 11:00? )))`<br>
`   ae = int(float(input("What is your heartbeat at 12:00? )))`<br>
`   af = int(float(input("What is your heartbeat at 13:00? )))`<br>
`   ag = int(float(input("What is your heartbeat at 14:00? )))`<br>
`   ah = int(float(input("What is your heartbeat at 15:00? )))`<br>
`   ai = int(float(input("What is your heartbeat at 16:00? )))`<br>
`   return [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z, aa, ab, ac, ad, ae, af, ag, ah, ai]`<br>


### Make a function to print all the pipes
`def print_pipes(inputs)`<br>
`   pipes = ["Your average rate of heart beat in the office is:", "\n"]`<br>
`   for i in inputs:`<br>
`       value = "|" * ((round(i, -1))/10)`<br>
`       pipes.append(value)`<br>
`   print("\n".join(pipes))`<br>
### Repeat 5 times and print the day, before printing the pipes.