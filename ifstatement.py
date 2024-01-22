score = 2


if score > 10:
    print('Good job!')
else: 
    print(f'Your score is less than 10')

user_status = 'users'

# ternary operator
print('Welcome to Dashboard, you are an Admin') if user_status == 'admin' else print('You are not allowed!')

# how to create ternary operator in python
# first thing is the expected output if statement is True
# after that, put if statement what we're checking for
# then else if the output is False

# run: py ifstatement.py