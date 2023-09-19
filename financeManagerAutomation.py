#! /usr/bin/env python3 
import gspread
import csv
from time import sleep
import re




Bankfile = 'fake_bank_transactions.csv'

transactions = []
MONTLY_PAYMENTS = ['CHASE',"PAYMENT APPLECARD",'GEICO','Payment Credit One Bank','E-PAYMENT DISCOVER','ACH PMT AMEX']
SUBSCRIPTION_NAMES = ["TRYHACKME.COM",'TRYHACKME.COM 01-06 LONDON 4862DEBIT CARD PURCHASE']
GROCERY = ['FOOD CITY', 'WAL-MART', 'WM SUPERCENTER','PUBLIX']
DEPOSIT = ['DEPOSIT','ATM MIXED DEPOSIT']
BETTING = ['MGM']
MONEY_TRANSFER = ['ZELLE','TrnWise Wise Ltd INTERNATIONAL']
CAR_PAYMENT = ['DRAFT WELLS FARGO AUTO 8476 MERT DEMIREZEN ']
MONTHS = ['','january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
def financeManager(file):
    with open(file,'r') as csv_file:
        header = next(csv_file)
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            post_date,trans_date,trans_type,serial_no,description,amount,balance = row
            category = 'other'
            # amount = re.sub(r"\(|\)", "",amount)
            amount = float(amount.replace('(','').replace(')','').replace('$',''))
            month = MONTHS[int(trans_date[:2])]
            

            

            #DIDNT WORK SO SECOND WAY
            # if description in SUBSCRIPTION_NAMES:
            #     # category = "SUBSCRIPTION"
            if any(list(map(lambda x: x in description,MONTLY_PAYMENTS))) : category = "PAYMENTS CC" 
            if any(list(map(lambda x: x in description,CAR_PAYMENT))) : category = "CAR PAYMENT" 
            if any(list(map(lambda x: x in description,SUBSCRIPTION_NAMES))) : category = "SUBSCRIPTION" 
            if any(list(map(lambda x: x in description,DEPOSIT))) : category = "DEPOSIT"
            if any(list(map(lambda x: x in description,GROCERY))) : category = "GROCERY" 
            if any(list(map(lambda x: x in description,BETTING))) : category = 'Betting -Waste' 
            if any(list(map(lambda x: x in description,MONEY_TRANSFER))) : category = 'ZELLE-MONEY_TRANSFER'

            
            # if category is not DEPOSIT - will be minus (expenses)

            if category != 'DEPOSIT' : amount = -amount
            
            




            transaction = (trans_date, description, amount, category, month)
            transactions.append(transaction)
        return transactions
rows = financeManager(Bankfile)
rows = rows[::-1]
# print(rows)
for trans in transactions:
    print(f'Category: {trans[-2]}, Month: {trans[-1]} --Amount: {trans[2]} - {trans[1]}')
    # print(trans[1])
    # if trans[1] in grocery :
        # print("[DEBUG] Yes!") 

gc = gspread.service_account()
sh = gc.open("Finances")



# -- UPDATE SHEET FOR MONTHS 
for row in rows:
#     # print(row)
    wks = sh.worksheet(row[-1])
#     # print(f'[DEBUG] : {row[-1]} ')
    wks.insert_row([row[0], row[1], row[3], row[2]], 7)
    sleep(2)