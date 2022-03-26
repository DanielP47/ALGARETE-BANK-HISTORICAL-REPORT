# Daniel J Perez  802-18-9272  SECTION: 116

def main():
    try:
        fileinput = input('Enter file name: ')
        file = open(fileinput, 'r')
        readfile = file.readlines()
        sendfile = account(readfile)
        file.close()
    except:
        print('File was not found!')
        main()

def account(readfile):
        count = 0
        accnum = list()
        names = list()
        accnum_deposit = list()
        accnum_withdraw = list()
        balancel = list()
        balance2 = list()
        balance3 = list()
        dctlist = list()
        opening_dic = {}
        deposit_dic = {}
        withdraw_dic = {}
        withdraw_deposit_dic = {}
        total_dic = {}
        list_dic = {}
        for line in readfile:
            splitlist = line.split(',')
            if splitlist[0] == 'O':
                count += 1
                convstring = str(count)
                while len(convstring) < 10:
                    convstring = '0' + convstring
                accnum.append(convstring)
                name = splitlist[1].lstrip()
                names.append(name)
                balance = splitlist[2].strip()
                balancel.append(balance)
            elif splitlist[0] == 'D':
                name = splitlist[1].lstrip()
                balance = splitlist[2].strip()
                accnum_deposit.append(name)
                balance2.append(balance)
            elif splitlist[0] == 'W':
                name = splitlist[1].lstrip()
                balance = splitlist[2].strip()
                accnum_withdraw.append(name)
                balance3.append(balance)
            else: #if not O, D or W it would continue to the next line
                continue

        for a,b in zip(accnum,balancel): # creates a dictionary with the account number and balance from opening an account
            opening_dic[a] = int(b)

        for x,y in zip(accnum_deposit,balance2): # created a dictionary with the account number and balance from depositing accounts
            deposit_dic[x] = deposit_dic.get(x,0) + int(y)

        for e,u in zip(accnum_withdraw,balance3): # creates a dictionary with the account number and balance from withdrawing accounts/values are negatives since it is a withdraw
            withdraw_dic[e] = withdraw_dic.get(e,0) + int(u) * -1

        for key,value in deposit_dic.items():
            for key1, value1 in withdraw_dic.items(): # add up the balance from depositing accounts and withdraw accounts
                if key == key1:
                    tvalue = value + value1
                    withdraw_deposit_dic[key] = (tvalue)
                if key not in key1:
                    withdraw_deposit_dic[key] = value
                if key1 not in withdraw_deposit_dic:
                    withdraw_deposit_dic[key1] = value1


        for key,value in opening_dic.items():
            for key1,value1 in withdraw_deposit_dic.items(): # add up the balance from withdraw/deposit add up and the opening accounts
                if key == key1:
                    tvalue = value + value1
                    total_dic[key] = (tvalue)
                if key not in total_dic:
                    total_dic[key] = value

        for key,values in total_dic.items():  # creates a list with the keys and value from the total dictionary
            me = key, values
            dctlist.append(me)

        for name,info in zip(names, dctlist):  # save the account name as a key and the account number and balance as a value
            list_dic[name] = info

        main_screen(list_dic)


def main_screen(dico):
    print(' ' * 20 + '--------- ALGARETE BANK HISTORICAL REPORT ---------')
    print('Report of Bank Accounts Ordered by Account Numbers\nAccount Number' + ' ' * 16 + 'Costumer Name' + ' ' * 17 + 'Balance')
    for key,value in dico.items():
       while len(key) < 30:
           key = key + ' '
       reworkvalue = value[0]
       while len(reworkvalue) < 30:
           reworkvalue = reworkvalue + ' '
       print(reworkvalue + key + '$'+ str(value[1]) + '.00')
    print('\nReport of Bank Accounts Ordered by Names of Owners\nCostumer Name' + ' ' * 17 + 'Account Number' + ' ' * 16 + 'Balance')

    for x in sorted(dico):
        ordertuple = (x, dico[x])
        namestr = str(ordertuple[0])
        tupledic = ordertuple[1] # This variable let me take the position of the balance and the account number apart
        while len(namestr) < 30:
            namestr = namestr + ' '
        lentuple0 = tupledic[0]
        while len(lentuple0) < 30:
            lentuple0 += ' '
        print(namestr + lentuple0 + '$' + str(tupledic[1]) + '.00')
    print('\nReport of Accounts with Maximum Balance\nCostumer Name' + ' ' * 17 + 'Account Number' + ' ' * 16 + 'Balance')
    highest = highest_balance(dico)
    print(highest[0], highest[1] + '$' + str(highest[2]) +'.00')
    print('Report of Accounts with Minimum Balance\nCostumer Name' + ' ' * 17 + 'Account Number' + ' ' * 16 + 'Balance')
    lowest = lowest_balance(dico)
    print(lowest[0], lowest[1] + '$' + str(lowest[2]) +'.00')
    average = avarage_balance(dico)
    print('Average of Accounts Balances is: $' + str(average) + '.00')
    print(' ' * 20 + '--------------  END OF HISTORICAL REPORT ----------------')

def highest_balance(bal):
    highestbalance = 0
    balancename = None
    accnum = None
    for key,values in bal.items():
        highvalue = values[1]
        if highvalue > highestbalance:
            highestbalance = highvalue
            balancename = key
            accnum = values[0]
        else:
            continue
    while len(balancename) < 29:
        balancename = balancename + ' '
    while len(accnum) < 30:
        accnum = accnum + ' '
    return balancename,accnum,highestbalance

def lowest_balance(bal):
    lowestbalance = None
    balancename = None
    accnum = None
    for key, values in bal.items():
        lowvalue = values[1]
        if lowestbalance is None or lowvalue < lowestbalance:
            lowestbalance = lowvalue
            balancename = key
            accnum = values[0]
        else:
            continue
    while len(balancename) < 29:
        balancename = balancename + ' '
    while len(accnum) < 30:
        accnum = accnum + ' '
    return balancename,accnum,lowestbalance

def avarage_balance(bal): # adds all the balance to then divide it with the total count
    total = 0
    count = 0
    for value in bal.values():
        balance = value[1]
        total = total + balance
        count += 1
    average = total/count
    return int(average)

if __name__ == "__main__":
    main()

