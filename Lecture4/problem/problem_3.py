balance = 3329
annualInterestRate = 0.2

aIR = annualInterestRate
upperB = (balance * (1+aIR/12)**12) / 12
lowerB = balance / 12
payment = (upperB+lowerB)/2

def bal_cal(balance, aIR, payment, month):
    if month == 0:
        return balance
    else:
        return (1+aIR/12) * (bal_cal(balance, aIR, payment, month-1) - payment)

while abs(bal_cal(balance, aIR, payment, 12)) > 0.01:
    if bal_cal(balance, aIR, payment, 12) > 0:
        lowerB = payment
        payment = (upperB + lowerB) / 2
    elif bal_cal(balance, aIR, payment, 12) < 0:
        upperB = payment
        payment = (upperB+lowerB) / 2



print ("Lowest Payment: " + str(round(payment,2)))

