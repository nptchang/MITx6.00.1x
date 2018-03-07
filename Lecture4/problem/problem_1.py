balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

aIR = annualInterestRate
mPR = monthlyPaymentRate
month = 12
remainBal = 0

def bal_cal(balance, aIR, mPR, month):
    if month == 0:
        return balance
    else:
        return (1+aIR/12) * (1-mPR) * bal_cal(balance, aIR, mPR, month-1)



print ("Remaining balance: " + str(round(bal_cal(balance, aIR, mPR, month), 2)))
