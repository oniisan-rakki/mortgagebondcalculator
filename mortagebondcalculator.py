from datetime import date
from dateutil.relativedelta import relativedelta
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

print ('\nAmortization Table\n')

def amortization_table(duration,loan_amount,interest_rate):
    p = loan_amount
    r = interest_rate/100/12
    n = duration * 12
    c = ((r * p)/(1-((1+(r))**(-n))))
    mydata = []
    head = ['#','Payment Date','Opening Balance', 'Interest', 'Principal', 'Total Payments','Closing Balance', 'Remaining']

    mnths = n
    mnth = 0
    beginning_balance = float(loan_amount)
    payment_date = loan_start

    while beginning_balance >= 0:
        #remaining payments - works
        mnths -= 1
        #payment number - works
        mnth += 1
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
        yr = int(payment_date[:4])
        mn = int(payment_date[5:7])
        day = int(payment_date[8:10])
        payment_date = date(yr,mn,day)
        #add values to list
        mydata.append([mnth , payment_date,opening_balance ,interest_paid ,principal_paid ,total_payment ,closing_balance ,mnths])
        #new opening n=balance
        beginning_balance -= principal_paid
        #new date
        payment_date += relativedelta(months=1)
        payment_date = str(payment_date)

        
    return print(tabulate(mydata, headers=head, tablefmt="grid") +'\n')

amortization_table(duration,loan_amount,interest_rate)

print ('\nEquity After Each Year\n')

def property_equity(purchase_price,loan_amount,duration,interest_rate):
    prop_val = purchase_price
    p = loan_amount
    r = interest_rate/100/12
    n = duration * 12
    c = ((r * p)/(1-((1+(r))**(-n))))
    mydata = []
    head = ['Year', 'Property Value', 'Loan Amount', 'Change in Equity']


    beginning_balance = float(p)
    mnths = n + 1
    year = duration
    while beginning_balance >=0 and mnths!=0:
        #remaining payments - works
        mnths -= 1
        #interest
        interest_paid = float(r * beginning_balance)
        #prinicipal
        principal_paid = float(c - interest_paid)
        #after paying
        beginning_balance -= principal_paid
        #for each year?
        if mnths % 12 == 0 and mnths != 0:
            chngequ_question = input ('Has Your Property Value Changed? (Y/N) ')
            if chngequ_question == 'Y':
                new_prop_value = int(input('Enter Your New Property Value (For This Year): R'))
                if new_prop_value > 0:
                    prop_val = new_prop_value
            if year == 'Inception':
                year = duration
            year = year - (mnths/12)
            if year == 0:
                year = 'Inception'
            equity = prop_val - beginning_balance
            mydata.append([year,prop_val,beginning_balance,equity])
            print(tabulate(mydata, headers=head, tablefmt="grid"))
        elif mnths == 1:
            year = duration
            beginning_balance = 0
            equity = prop_val - beginning_balance
            mydata.append([year,prop_val,beginning_balance,equity])
            print(tabulate(mydata, headers=head, tablefmt="grid"))
        
    return print('\nSummary\n' + tabulate(mydata, headers=head, tablefmt="grid") +'\n')
        
property_equity(purchase_price,loan_amount,duration,interest_rate)

print('Thats a wrap.\nGoodbye!\n')