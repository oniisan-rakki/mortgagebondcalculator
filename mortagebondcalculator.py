import datetime
from tabulate import tabulate

print ('\nMortgage Loan Calulator\n')
print ('Loan Details\n')
purchase_price = int(input('Purchase Price: R'))
interest_rate = float(input('Interest Rate: '))
duration = int(input('Duration of Loan (in years): ')) 
deposit = int(input('Deposit (Optional): R'))
loan_amount = purchase_price - deposit
print('Loan Amount R' + str(loan_amount))
loan_start = input('Loan Start Date (year-month-day): ')

print('\nKey Statistics\n')

def key_statistics(loan_amount,interest_rate,duration):
    p = loan_amount
    r = interest_rate/100/12
    n = duration * 12
    c = ((r * p)/(1-((1+(r))**(-n))))
    monthly_repayment = 'Monthly Loan Payments: R' + str(round(c,2))
    i = (p*r - c)*(((1 + r)**n - 1)/r)+c*n
    total_interest_paid = 'Total Interest Paid: R' + str(round(i,2))
    t = p + i
    total_loan_payment = 'Total Loan Payments: R' + str(round(t,2))
    return print(monthly_repayment + '\n' + total_interest_paid + '\n' + total_loan_payment)

key_statistics(loan_amount,interest_rate,duration)

print ('\nEquity After Each Year')

def property_equity():
    pass
    #change in balance of loan each year
    #change in equity


#property_equity(loan_amount,interest_rate,duration)

print ('\nAmortization Table\n')

def amortization_table(duration,loan_amount,interest_rate):
    p = loan_amount
    r = interest_rate/100/12
    n = duration * 12
    c = ((r * p)/(1-((1+(r))**(-n))))
    start_date = loan_start
    mydata = []
    head = ['#','Payment Date','Opening Balance', 'Interest', 'Principal', 'Total Payments','Closing Balance', 'Remaining']

    months = n
    month = 0
    beginning_balance = float(loan_amount)
    interest = (p*r - c)*(((1 + r)**n - 1)/r)+c*n
    payment_date = start_date

    while beginning_balance >= 0 and interest >=0:
        #remaining payments - works
        months -= 1
        #payment number - works
        month += 1
        #opening balance - works 
        opening_balance = float(beginning_balance)
        #interest 
        interest_paid = float(r * opening_balance)
        #prinicipal
        principal_paid = float(c - interest_paid)
        #total payments - works
        total_payment = float(principal_paid + interest_paid)
        #closing balance - works
        closing_balance = round(opening_balance - principal_paid,2)
        #payment_date
        #add values to list
        mydata.append([month , payment_date,opening_balance ,interest_paid ,principal_paid ,total_payment ,closing_balance ,months])
        #new opening n=balance
        beginning_balance -= principal_paid
        #new date
        
    return print(tabulate(mydata, headers=head, tablefmt="grid"))

amortization_table(duration,loan_amount,interest_rate)