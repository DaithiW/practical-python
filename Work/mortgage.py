# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
months = 0
count = 0

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_pament = 1000

while principal > 0:
    if extra_payment_start_month <= months <= extra_payment_end_month:
        total_payment = payment + extra_pament
        if total_payment > principal * (1 + rate / 12):
            total_payment = principal * (1 + rate / 12)
        principal = principal * (1 + rate / 12) - total_payment
        total_paid = total_paid + total_payment
        months += 1
        count += 1
    else:
        total_payment = payment
        if total_payment > principal * (1 + rate / 12):
            total_payment = principal * (1 + rate / 12)
        principal = principal * (1 + rate / 12) - total_payment
        total_paid = total_paid + total_payment
        months += 1

    print(
        f"{months} months, total payment = {round(total_payment, ndigits=2)}, principal = {round(principal, ndigits=2)}"
    )

print("Total paid", round(total_paid, ndigits=2))
