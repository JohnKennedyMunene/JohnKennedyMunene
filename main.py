import random

lucky_number = random.randint(40,42)

lucky_text = ''

if lucky_number == 40:
  lucky_text = 'Not good enough'

if lucky_number == 41:
  lucky_text = 'All Good!'

if lucky_number == 42:
  lucky_text = 'You will get there'

print(f'Your Lucky Number is {lucky_number} and {lucky_text}')