sum_odd_digits = 0
sum_even_digits = 0
total = 0

card_number = input('Type your card number: ').replace("-", "").replace(" ", "")
card_number = card_number[::-1]

if not card_number.isdigit():
    print("Invalid input. Only digits are allowed.")
    exit()

for x in card_number[::2]:
    sum_odd_digits += int(x)

for x in card_number[1::2]:
    x = int(x) * 2
    sum_even_digits += (x // 10) + (x % 10)
		
total = sum_odd_digits + sum_even_digits


if total % 10 == 0:
	print('VALID!')
else:
	print('INVALID.')