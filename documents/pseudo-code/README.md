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
`for i in range(a, b):`<br>
### Define another function that automatically validates the inputs, and asks again if not valid.
`def take_inputs_and_validate():`<br>
`a, b = inputs()`<br>
`if not validate_input(a, b): a, b = inputs()`<br>
`else: return calc_heart_rate(a, b)`<br>