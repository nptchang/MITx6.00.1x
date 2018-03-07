balance = 3329
annualInterestRate = 0.2

aIR = annualInterestRate
payment = 10

def bal_cal(balance, aIR, payment, month):
    if month == 0:
        return balance
    else:
        return (1+aIR/12)*(bal_cal(balance, aIR, payment, month-1)-payment)

while bal_cal(balance, aIR, payment, 12)>0:
    payment = payment + 10

print ("Lowest Payment: " + str(payment))

