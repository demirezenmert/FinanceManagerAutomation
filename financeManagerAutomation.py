#! /usr/bin/env python3 
import gspread
import csv
from time import sleep


Bankfile = '/Users/mertdemirezen/Documents/Projects/FinanceManagerAutomation/acct_5623_01_01_2023_to_04_01_2023.csv'


transactions = []
MONTLY_PAYMENTS = ['CHASE',"PAYMENT APPLECARD",'GEICO','WELLS FARGO','Payment Credit One Bank','E-PAYMENT DISCOVER','ACH PMT AMEX']
SUBSCRIPTION_NAMES = ["TRYHACKME.COM",'TRYHACKME.COM 01-06 LONDON 4862DEBIT CARD PURCHASE']
GROCERY = ['FOOD CITY', 'WAL-MART', 'WM SUPERCENTER','PUBLIX']
DEPOSIT = ['DEPOSIT','ATM MIXED DEPOSIT']

def financeManager(file):
    with open(file,'r') as csv_file:
        header = next(csv_file)
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            post_date,trans_date,trans_type,serial_no,description,amount,balance = row
            category = 'other'




            if 'ZELLE' in description:
                category = 'ZELLE'

            #DIDNT WORK SO SECOND WAY
            # if description in SUBSCRIPTION_NAMES:
                # category = "SUBSCRIPTION"
            category = "SUBSCRIPTION" if any(list(map(lambda x: x in description,SUBSCRIPTION_NAMES))) else "other"
            category = "DEPOSIT" if any(list(map(lambda x: x in description,DEPOSIT))) else "other"
            category = "GROCERY" if any(list(map(lambda x: x in description,GROCERY))) else "other"
            category = "PAYMENTS CC" if any(list(map(lambda x: x in description,MONTLY_PAYMENTS))) else "other"
            
        
            if 'MGM' in description :
                category = 'Betting -Waste'
            



            transaction = (trans_date, description, amount, category)
            transactions.append(transaction)
        return transactions
rows = financeManager(Bankfile)
print(rows)
for trans in transactions:
    print(f'Category: {trans[-1]} --Amount: {trans[2]}- {trans[1][:4]}')
    # print(trans[1])
    # if trans[1] in grocery :
        # print("[DEBUG] Yes!") 

gc = gspread.service_account()
sh = gc.open("Finances")

wks = sh.worksheet(f'january')
# for row in rows:
#     wks.insert_row([row[0], row[1], row[3], row[2]], 8)
#     sleep(2)