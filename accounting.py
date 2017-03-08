# pylint: disable=C0301, C0103
# https://www.reddit.com/r/dailyprogrammer/comments/5wnbsi/20170228_challenge_304_easy_little_accountant/

import sys
import datetime

MONTH = {'JAN':1, 'FEB':2, 'MAR':3, 'APR':4, 'MAY':5, 'JUN':6, 'JUL':7, 'AUG':8, 'SEP':9, 'OCT':10, 'NOV':11, 'DEC':12}

def find_accounts(start, end, journal):
    return [v for v in journal if v[0][:len(start)] >= start and v[0][:len(end)] <= end]

def filter_by_date(period, journal):
    return [v for v in journal if v[1] >= period['start'] and v[1] <= period['end']]

def sumup_accounts(accounts):
    result = {}
    for k, date, debit, credit in accounts:
        if k in result:
            result[k][1] += int(debit)
            result[k][2] += int(credit)
        else:
            result[k] = [date, int(debit), int(credit)]
    return result

def display_csv_summery(totals, period, list_of_accounts, acc_descr):
    keys = sorted(list_of_accounts)
    print('Total Debit: ' + str(totals[0]) + ' Total Credit: ' + str(totals[1]))
    print('Balance from account ' + keys[0] + ' to ' + keys[-1] + ' from period ' + period['start'].strftime('%b-%y') + ' to ' + period['end'].strftime('%b-%y'))
    print('\nBalance:')
    print('ACCOUNT;DESCRIPTION;DEBIT;CREDIT;BALANCE;')
    total_debit = 0
    total_credit = 0
    for k in keys:
        debit = list_of_accounts[k][1]
        credit = list_of_accounts[k][2]
        print(k + ';' + acc_descr[k] + ';' + str(debit) + ';' + str(credit) + ';' + str(debit - credit) + ';')
        total_debit += debit
        total_credit += credit
    print('TOTAL;;' + str(total_debit) + ';' + str(total_credit) + ';' + str(total_debit-total_credit) + ';')
    return

def display_text_summery(totals, period, list_of_accounts, acc_descr):
    keys = sorted(list_of_accounts)
    print('Total Debit: ' + str(totals[0]) + ' Total Credit: ' + str(totals[1]))
    print('Balance from account ' + keys[0] + ' to ' + keys[-1] + ' from period ' + period['start'].strftime('%b-%y') + ' to ' + period['end'].strftime('%b-%y'))
    print('\nBalance:')
    print('ACCOUNT'.ljust(10) + '| ' + 'DESCRIPTION'.ljust(20) + '|' + 'DEBIT'.rjust(10) + ' |' + 'CREDIT'.rjust(10) + ' |' + 'BALANCE'.rjust(10)+ ' |')
    print(''.ljust(71, '-'))
    total_debit = 0
    total_credit = 0
    for k in keys:
        debit = list_of_accounts[k][1]
        credit = list_of_accounts[k][2]
        print(k.ljust(10) + '| ' + acc_descr[k].ljust(20) + '|' + str(debit).rjust(10) + ' |' + str(credit).rjust(10) + ' |' + str(debit - credit).rjust(10) + ' |')
        total_debit += debit
        total_credit += credit
    print('TOTAL'.ljust(10) + '| ' + ' '.ljust(20, ' ') + '|' + str(total_debit).rjust(10) + ' |' + str(total_credit).rjust(10) + ' |' + str(total_debit-total_credit).rjust(10) + ' |')
    return

def make_date_obj(date_str):
    m, y = date_str.split('-')
    return datetime.date(int(y) + 2000, MONTH[m], 1)

def main():
    with open(sys.argv[1], 'r') as file:
        lines = list(map(lambda s: s.strip(), file.readlines()))
    journal = []
    totals = [0, 0]
    period = {'end': datetime.date(2000, 1, 1), 'start': datetime.date(2099, 12, 31)}
    for l in lines[1:]:
        account_no, date, debit, credit = l.strip(';').split(';')
        totals[0] += int(debit)
        totals[1] += int(credit)
        date_obj = make_date_obj(date)
        if date_obj < period['start']:
            period['start'] = date_obj
        if date_obj > period['end']:
            period['end'] = date_obj
        journal.append((account_no, date_obj, debit, credit))
    if totals[0] != totals[1]:
        print('Journal is unbalanced debit=' + totals[0] + ' credit=' + totals[1])
        return
    with open(sys.argv[2], 'r') as file:
        accounts = list(map(lambda s: s.strip(), file.readlines()))
    acc = {}
    for s in accounts[1:]:
        account_no, label = s.strip(';').split(';')
        keyval = {account_no:label}
        acc.update(keyval)
    request = input('?')
    #request = '2 3000 FEB-16 AUG-16 TEXT'
    #request = '2 * FEB-16 * TEXT'
    #request = '* 2 FEB-16 * TEXT'
    #request = '40 * MAR-16 * CSV'
    start_acc, end_acc, start_period, end_period, outformat = request.split(' ')
    if start_acc == '*':
        start_acc = '1'
    if end_acc == '*':
        end_acc = '9999'
    if start_period != '*':
        period['start'] = make_date_obj(start_period)
    if end_period != '*':
        period['end'] = make_date_obj(end_period)
    filtered_accounts = find_accounts(start_acc, end_acc, journal)
    resulting_accounts = filter_by_date(period, filtered_accounts)
    resulting_accounts = sumup_accounts(resulting_accounts)
    if outformat == 'TEXT':
        display_text_summery(totals, period, resulting_accounts, acc)
    if outformat == 'CSV':
        display_csv_summery(totals, period, resulting_accounts, acc)
    return

if __name__ == '__main__':
    main()
