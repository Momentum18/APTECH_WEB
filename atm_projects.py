user_new_pin = ''
authenticated = False


def set_pin(pin):
    global user_new_pin
    user_new_pin = pin
    authenticated = True


def check_pin(pin):
    if pin == user_new_pin:
        global authenticated
        authenticated = True
        print('proceed')
    elif pin == default_pin:
        print("your PIN is default, change your PIN")
        change_pin()
    else:
        print("Incorrect PIN")
        reuser_pin = int(input("Enter your Correct PIN: "))
        check_pin(reuser_pin)


def change_pin():
    enter_pin = input("Enter your New PIN: ")
    confirm_pin = input("Confirm your New PIN: ")
    if len(enter_pin) == 4:
        if enter_pin == confirm_pin:
            set_pin(enter_pin)
        else:
            print('pin must match')
            change_pin()
    else:
        print('pin must be four digit')
        change_pin()


while True:
    default_pin = '0000'
    if not authenticated:
        user_pin = input("Enter your PIN: ")
        check_pin(user_pin)
        user = input("Enter your name: ")
    print(f"Welcome {user}")
    Help = """
    Help command
    
    type Check balance - To show your Current Balance
    type Cash Withdrawal - To Withdraw a certain amount from your available balance
    type Load Airtime - To Recharge directly into your phone
    type Bank Transfer - To Transfer funds from one account to the other
    type Open Account - To Open a new account with us
    type Paybills -  To Subscribe to your devices
    type Finish - To exit and remove your Card
    """

    print(Help)
    command = input(">>> ")

    if command == "Check balance":
        account_balance = 100000
        print(f"Your available balance is N{account_balance}K")
        wish = input("Do you wish to continue with other transaction? Y or N: ")

        if wish.lower() == 'y':
            continue
        else:
            break

    if command == "Cash Withdrawal":
        select_option = """
        
        (A) #500               (B) #1000
        (C) #5000              (D) #10000
        (E) #20000             (F) Other
        """
        print(select_option)
        selection = input('Enter selection: ')
        selection = selection.strip().lower()

        if selection == 'a':
            amount = 500
            print(f'{amount} withdrawal successful')
            account_balance = 100000
            available_balance = account_balance - amount

            print(f"your available balance is N{available_balance}")

            wish = input("Do you wish to continue with other transaction? Y or N: ")

            if wish.lower() == 'y':
                continue
            else:
                break

        elif selection == 'b':
            amount = 1000
            print(f'{amount} withdrawal successful')
            account_balance = 100000
            available_balance = account_balance - amount

            print(f"your available balance is N{available_balance}")
            wish = input("Do you wish to continue with other transaction? Y or N: ")

            if wish.lower() == 'y':
                continue
            else:
                break

        elif selection == 'c':
            amount = 5000
            print(f'{amount} withdrawal successful')
            account_balance = 100000
            available_balance = account_balance - amount
            print(f"your available balance is N{available_balance}")

            wish = input("Do you wish to continue with other transaction? Y or N: ")

            if wish.lower() == 'y':
                continue
            else:
                break

        elif selection == 'd':
            amount = 10000
            print(f'{amount} withdrawal successful')
            account_balance = 100000
            available_balance = account_balance - amount
            print(f"your available balance is N{available_balance}")

            wish = input("Do you wish to continue with other transaction? Y or N: ")

            if wish.lower() == 'y':
                continue
            else:
                break

        elif selection == 'e':
            amount = 20000
            print(f'{amount} withdrawal successful')
            account_balance = 100000
            available_balance = account_balance - amount
            print(f"your available balance is N{available_balance}")

            wish = input("Do you wish to continue with other transaction? Y or N: ")

            if wish.lower() == 'y':
                continue
            else:
                break

        else:
            amount = int(input('enter amount'))

            print(f'{amount} withdrawal successful')
            account_balance = 100000
            available_balance = account_balance - amount
            print(f"your available balance is N{available_balance}")

            wish = input("Do you wish to continue with other transaction? Y or N: ")

            if wish.lower() == 'y':
                continue
            else:
                break

    if command == "Load Airtime":
        select_airtime = """
        (1) MTN                               (2) AIRTEL
        (3) GLO                               (4) ETISALAT
        """
        print(select_airtime)
        selection1 = input('Enter option: ')

        if selection1 == '1':
            print('MTN')
            user = int(input('Enter amount: '))
            phone = int(input("Enter your phone number: "))
            print(f"You Successfully recharged the sum of {user} on {phone}")
            account_balance = 100000
            available_balance = account_balance - amount

            print(f"your available balance is N{available_balance}")

            wish = input("Do you wish to continue with other transaction? Y or N: ")

            if wish.lower() == 'y':
                continue
            else:
                break

        if selection1 == '2':
            print('AIRTEL')
            user = int(input('Enter amount: '))
            phone = int(input("Enter your phone number: "))
            print(f"You Successfully recharged the sum of {user} on {phone}")

            account_balance = 100000
            available_balance = account_balance - amount

            print(f"your available balance is N{available_balance}")

            wish = input("Do you wish to continue with other transaction? Y or N: ")

            if wish.lower() == 'y':
                continue
            else:
                break

        if selection1 == '3':
            print('GLO')
            user = int(input('Enter amount: '))
            phone = int(input("Enter your phone number: "))
            print(f"You Successfully recharged the sum of {user} on {phone}")

            account_balance = 100000
            available_balance = account_balance - amount

            print(f"your available balance is N{available_balance}")

            wish = input("Do you wish to continue with other transaction? Y or N: ")

            if wish.lower() == 'y':
                continue
            else:
                break

        if selection1 == '4':
            print('ETISALAT')
            user = int(input('Enter amount: '))
            phone = int(input("Enter your phone number: "))
            print(f"You Successfully recharged the sum of {user} on {phone}")

            account_balance = 100000
            available_balance = account_balance - amount

            print(f"your available balance is N{available_balance}")

            wish = input("Do you wish to continue with other transaction? Y or N: ")

            if wish.lower() == 'y':
                continue
            else:
                break

    if command == 'Bank Transfer':
        transfer_type = """
        (1) Same Bank                           (2)Other Banks
        """
        print(transfer_type)
        selection2 = input('Choose Bank option: ')

        if selection2 == '1':
            print('Same Bank')

            account_number = int(input("Enter your Account Number: "))
            Transfer_amount = int(input("Enter the amount: "))
            print(f"You have Successfully Transferred the sum of {Transfer_amount} into {account_number}")

            account_balance = 100000
            available_balance = account_balance - amount

            print(f"your available balance is N{available_balance}")

            wish = input("Do you wish to continue with other transaction? Y or N: ")

            if wish.lower() == 'y':
                continue
            else:
                break

        if selection2 == '2':
            print('Other Banks')

            select_Bank = """
                (1) Access Bank                     (2) Fidelity Bank
                (3) Ecobank                         (4) First Bank              
                (5) FCMB                            (6) Gateway Bank                   
                (7) Guaranty Trust Bank             (8) Heritage Bank                    
                (9) Keystone Bank                   (10) Platinum Habib Bank             
                (11) Polaris Bank                   (12) Stanbic IBTC                   
                (13) Standard Chattered Bank        (14) Sterling Bank Plc              
                (15) UBA                            (16) Union Bank                     
                (17) Unity Bank                     (18) Wema Bank                      
                (19) Zenith Bank                    (20) Others

            """

            print(select_Bank)
            selection3 = input('Enter option: ')

            if selection3 == '1':
                print('Access Bank')
                account_number = int(input("Enter your Account Number: "))
                Transfer_amount = int(input("Enter the amount: "))
                print(f"You have Successfully Transferred the sum of {Transfer_amount} into {account_number}")

                account_balance = 100000
                available_balance = account_balance - amount

                print(f"your available balance is N{available_balance}")

                wish = input("Do you wish to continue with other transaction? Y or N: ")

                if wish.lower() == 'y':
                    continue
                else:
                    break

            if selection3 == '2':
                print('Fidelity Bank')
                account_number = int(input("Enter your Account Number: "))
                Transfer_amount = int(input("Enter the amount: "))
                print(f"You have Successfully Transferred the sum of {Transfer_amount} into {account_number}")

                account_balance = 100000
                available_balance = account_balance - amount

                print(f"your available balance is N{available_balance}")

                wish = input("Do you wish to continue with other transaction? Y or N: ")

                if wish.lower() == 'y':
                    continue
                else:
                    break

            if selection3 == '3':
                print('Ecobank')
                account_number = int(input("Enter your Account Number: "))
                Transfer_amount = int(input("Enter the amount: "))
                print(f"You have Successfully Transferred the sum of {Transfer_amount} into {account_number}")

                account_balance = 100000
                available_balance = account_balance - amount

                print(f"your available balance is N{available_balance}")

                wish = input("Do you wish to continue with other transaction? Y or N: ")

                if wish.lower() == 'y':
                    continue
                else:
                    break

            if selection3 == '4':
                print('First Bank')
                account_number = int(input("Enter your Account Number: "))
                Transfer_amount = int(input("Enter the amount: "))
                print(f"You have Successfully Transferred the sum of {Transfer_amount} into {account_number}")

                account_balance = 100000
                available_balance = account_balance - amount

                print(f"your available balance is N{available_balance}")

                wish = input("Do you wish to continue with other transaction? Y or N: ")

                if wish.lower() == 'y':
                    continue
                else:
                    break

            if selection3 == '5':
                print('FCMB')
                account_number = int(input("Enter your Account Number: "))
                Transfer_amount = int(input("Enter the amount: "))
                print(f"You have Successfully Transferred the sum of {Transfer_amount} into {account_number}")

                account_balance = 100000
                available_balance = account_balance - amount

                print(f"your available balance is N{available_balance}")

                wish = input("Do you wish to continue with other transaction? Y or N: ")

                if wish.lower() == 'y':
                    continue
                else:
                    break

            if selection3 == '6':
                print('Gateway Bank')
                account_number = int(input("Enter your Account Number: "))
                Transfer_amount = int(input("Enter the amount: "))
                print(f"You have Successfully Transferred the sum of {Transfer_amount} into {account_number}")

                account_balance = 100000
                available_balance = account_balance - amount

                print(f"your available balance is N{available_balance}")

                wish = input("Do you wish to continue with other transaction? Y or N: ")

                if wish.lower() == 'y':
                    continue
                else:
                    break

            if selection3 == '7':
                print('Guaraty Trust Bank')
                account_number = int(input("Enter your Account Number: "))
                Transfer_amount = int(input("Enter the amount: "))
                print(f"You have Successfully Transferred the sum of {Transfer_amount} into {account_number}")

                account_balance = 100000
                available_balance = account_balance - amount

                print(f"your available balance is N{available_balance}")

                wish = input("Do you wish to continue with other transaction? Y or N: ")

                if wish.lower() == 'y':
                    continue
                else:
                    break

            if selection3 == '8':
                print('Heritage Bank')
                account_number = int(input("Enter your Account Number: "))
                Transfer_amount = int(input("Enter the amount: "))
                print(f"You have Successfully Transferred the sum of {Transfer_amount} into {account_number}")

                account_balance = 100000
                available_balance = account_balance - amount

                print(f"your available balance is N{available_balance}")

                wish = input("Do you wish to continue with other transaction? Y or N: ")

                if wish.lower() == 'y':
                    continue
                else:
                    break

            if selection3 == '9':
                print('Keystone Bank')
                account_number = int(input("Enter your Account Number: "))
                Transfer_amount = int(input("Enter the amount: "))
                print(f"You have Successfully Transferred the sum of {Transfer_amount} into {account_number}")

                account_balance = 100000
                available_balance = account_balance - amount

                print(f"your available balance is N{available_balance}")

                wish = input("Do you wish to continue with other transaction? Y or N: ")

                if wish.lower() == 'y':
                    continue
                else:
                    break

            if selection3 == '10':
                print('Platinum Habib Bank')
                account_number = int(input("Enter your Account Number: "))
                Transfer_amount = int(input("Enter the amount: "))
                print(f"You have Successfully Transferred the sum of {Transfer_amount} into {account_number}")

                account_balance = 100000
                available_balance = account_balance - amount

                print(f"your available balance is N{available_balance}")

                wish = input("Do you wish to continue with other transaction? Y or N: ")

                if wish.lower() == 'y':
                    continue
                else:
                    break

            if selection3 == '11':
                print('Polaris Bank')
                account_number = int(input("Enter your Account Number: "))
                Transfer_amount = int(input("Enter the amount: "))
                print(f"You have Successfully Transferred the sum of {Transfer_amount} into {account_number}")

                account_balance = 100000
                available_balance = account_balance - amount

                print(f"your available balance is N{available_balance}")

                wish = input("Do you wish to continue with other transaction? Y or N: ")

                if wish.lower() == 'y':
                    continue
                else:
                    break

            if selection3 == '12':
                print('Stanbic Bank')
                account_number = int(input("Enter your Account Number: "))
                Transfer_amount = int(input("Enter the amount: "))
                print(f"You have Successfully Transferred the sum of {Transfer_amount} into {account_number}")

                account_balance = 100000
                available_balance = account_balance - amount

                print(f"your available balance is N{available_balance}")

                wish = input("Do you wish to continue with other transaction? Y or N: ")

                if wish.lower() == 'y':
                    continue
                else:
                    break

            if selection3 == '13':
                print('Standard Chattered Bank')
                account_number = int(input("Enter your Account Number: "))
                Transfer_amount = int(input("Enter the amount: "))
                print(f"You have Successfully Transferred the sum of {Transfer_amount} into {account_number}")

                account_balance = 100000
                available_balance = account_balance - amount

                print(f"your available balance is N{available_balance}")

                wish = input("Do you wish to continue with other transaction? Y or N: ")

                if wish.lower() == 'y':
                    continue
                else:
                    break

            if selection3 == '14':
                print('Sterling Bank')
                account_number = int(input("Enter your Account Number: "))
                Transfer_amount = int(input("Enter the amount: "))
                print(f"You have Successfully Transferred the sum of {Transfer_amount} into {account_number}")

                account_balance = 100000
                available_balance = account_balance - amount

                print(f"your available balance is N{available_balance}")

                wish = input("Do you wish to continue with other transaction? Y or N: ")

                if wish.lower() == 'y':
                    continue
                else:
                    break

            if selection3 == '15':
                print('UBA')
                account_number = int(input("Enter your Account Number: "))
                Transfer_amount = int(input("Enter the amount: "))
                print(f"You have Successfully Transferred the sum of {Transfer_amount} into {account_number}")

                account_balance = 100000
                available_balance = account_balance - amount

                print(f"your available balance is N{available_balance}")

                wish = input("Do you wish to continue with other transaction? Y or N: ")

                if wish.lower() == 'y':
                    continue
                else:
                    break

            if selection3 == '16':
                print('Union Bank')
                account_number = int(input("Enter your Account Number: "))
                Transfer_amount = int(input("Enter the amount: "))
                print(f"You have Successfully Transferred the sum of {Transfer_amount} into {account_number}")

                account_balance = 100000
                available_balance = account_balance - amount

                print(f"your available balance is N{available_balance}")

                wish = input("Do you wish to continue with other transaction? Y or N: ")

                if wish.lower() == 'y':
                    continue
                else:
                    break

            if selection3 == '17':
                print('Unity Bank')
                account_number = int(input("Enter your Account Number: "))
                Transfer_amount = int(input("Enter the amount: "))
                print(f"You have Successfully Transferred the sum of {Transfer_amount} into {account_number}")

                account_balance = 100000
                available_balance = account_balance - amount

                print(f"your available balance is N{available_balance}")

                wish = input("Do you wish to continue with other transaction? Y or N: ")

                if wish.lower() == 'y':
                    continue
                else:
                    break

            if selection3 == '18':
                print('Wema Bank')
                account_number = int(input("Enter your Account Number: "))
                Transfer_amount = int(input("Enter the amount: "))
                print(f"You have Successfully Transferred the sum of {Transfer_amount} into {account_number}")

                account_balance = 100000
                available_balance = account_balance - amount

                print(f"your available balance is N{available_balance}")

                wish = input("Do you wish to continue with other transaction? Y or N: ")

                if wish.lower() == 'y':
                    continue
                else:
                    break

            if selection3 == '19':
                print('Zenith Bank')
                account_number = int(input("Enter your Account Number: "))
                Transfer_amount = int(input("Enter the amount: "))
                print(f"You have Successfully Transferred the sum of {Transfer_amount} into {account_number}")

                account_balance = 100000
                available_balance = account_balance - amount

                print(f"your available balance is N{available_balance}")

                wish = input("Do you wish to continue with other transaction? Y or N: ")

                if wish.lower() == 'y':
                    continue
                else:
                    break

            if selection3 == '20':
                print('Other Banks')
                bank_name = input("Enter Bank name: ")
                account_number = int(input("Enter your Account Number: "))
                Transfer_amount = int(input("Enter the amount: "))
                print(f"You have Successfully Transferred the sum of {Transfer_amount} into {account_number}")

                account_balance = 100000
                available_balance = account_balance - amount

                print(f"your available balance is N{available_balance}")

                wish = input("Do you wish to continue with other transaction? Y or N: ")

                if wish.lower() == 'y':
                    continue
                else:
                    break

    if command == 'Open Account':
        name = input("Enter your names: ")
        email = input("Enter your email address: ")
        age = int(input("Enter your age: "))
        address = input("Enter your address: ")
        account_type = input("Enter account type: ")
        nationality = input("Enter your Nationality: ")
        occupation = input("Enter your Occupation: ")
        print(f"Thank you for Opening an account with us")

        wish = input("Do you wish to continue with other transaction? Y or N: ")

        if wish.lower() == 'y':
            continue
        else:
            break

    if command == 'Paybills':
        select_item = """
        (A) Cable TV                           (B) Sports and Gaming
        (C) Travel and Hotel                   (D) Electricity 
        """
        print(select_item)
        selection4 = (input('Enter option: '))
        selection4 = selection4.strip().lower()

        if selection4 == 'a':
            print("Cable TV")

            select_billers = """
            (A) DSTV                            (B) GOTV
            (C) STARTIMES                       (D) MYTV
            """
            print(select_billers)
            selection5 = input('Enter Option: ')
            selection5 = selection5.strip().lower()

            if selection5 == 'a':
                print('DSTV')

                select_bills = """
                (A) DStv Padi Bouquet E36                       (B) DStv Movie Bundle Addon E36
                (C) DStv Compact Plus Movie Bundle Addon E36    (D) French Touch
                (E) HDPVR AccessExtraview                       (F) Xtraview Access
                (G) DStv Yanga Bouquet E36                      (H) French 11 Bouquet E36
                (I) Padi Xtraview                               (J) DSTV Confam Bouquet E36
                (K) Yanga Xtraview                              (L) Asia Addon 
                (M) Confam Xtraview                             (N) Compact
                (O) French Plus                                 (P) Compact French Touch
                (Q) Compact HDExtraView                         (R) Compact Plus
                (S) Compact FRench Touch HDExtraView            (T) Compact Asia
                (U) CompactPlus French Touch                    (V) Compact Plus HDExtraView
                (W) Compact French Plus                         (X) Compact Asia Xtraview
                (Y) Premium                                     (Z) Compact Plus Asia
                (ZA) Others 
                """
                print(select_bills)
                selection6 = input('Enter Option: ')

                selection6 = selection6.strip().lower()
                if selection6 == 'a':
                    amount = 2150
                elif selection6 == 'b':
                    amount = 2500
                elif selection6 == 'c':
                    amount = 2501
                elif selection6 == 'd':
                    amount = 2650
                elif selection6 == 'e':
                    amount = 2900
                elif selection6 == 'f':
                    amount = 2901
                elif selection6 == 'g':
                    amount = 2950
                elif selection6 == 'h':
                    amount = 4100
                elif selection6 == 'i':
                    amount = 5050
                elif selection6 == 'j':
                    amount = 5300
                elif selection6 == 'k':
                    amount = 5850
                elif selection6 == 'l':
                    amount = 7100
                elif selection6 == 'm':
                    amount = 8200
                elif selection6 == 'n':
                    amount = 9000
                elif selection6 == 'o':
                    amount = 9300
                elif selection6 == 'p':
                    amount = 11650
                elif selection6 == 'q':
                    amount = 11900
                elif selection6 == 'r':
                    amount = 14250
                elif selection6 == 's':
                    amount = 14550
                elif selection6 == 't':
                    amount = 16100
                elif selection6 == 'u':
                    amount = 16900
                elif selection6 == 'v':
                    amount = 17150
                elif selection6 == 'w':
                    amount = 18300
                elif selection6 == 'x':
                    amount = 19000
                elif selection6 == 'y':
                    amount = 21000
                elif selection6 == 'z':
                    amount = 21350
                else:
                    other_bill = input('Enter Others: ')
                    amount = int(input('Enter amount: '))

                print(f"You Successfully subscribed the {amount} plan")

                wish = input("Do you wish to continue with other transaction? Y or N: ")

                if wish.lower() == 'y':
                    continue
                else:
                    break

            if selection5 == 'b':
                print('GOTV')
                select_billers1 = """
                (A) GOtv Smallie monthly                  (B) GOtv Jinja Bouquet
                (C) GOtv Smallie quarterly                (D) GOtv Jolli Bouquet
                (E) GOtv Max                              (F) SUPA
                (G) GOtv Smallie yearly 
                """
                print(select_billers1)
                selection7 = input('Enter Option: ')
            selection7 = selection7.strip().lower()

            if selection7 == 'a':
                amount = 900
            elif selection7 == 'b':
                amount = 1900
            elif selection7 == 'c':
                amount = 2400
            elif selection7 == 'd':
                amount = 2800
            elif selection7 == 'e':
                amount = 4150
            elif selection7 == 'f':
                amount = 5500
            elif selection7 == 'g':
                amount = 7000
                print(f"Your {amount} subscription is successful")

            wish = input("Do you wish to continue with other transaction? Y or N: ")

            if wish.lower() == 'y':
                continue
            else:
                break

            if selection5 == 'c':
                print('STARTIMES')
                select_billers2 = """
                (A) Ewallet Amount                          (B) Nova One Day
                (C) Basic One Day                           (D) Smart One Day
                (E) Nova One Week                           (F) Classic One Day
                (G) Super One Day                           (H) Basic One Week
                (I) Smart One Week                          (J) Nova One Month
                (K) Classic One Week                        (L) Super One Week
                (M) Basic One Month                         (N) Smart One Month
                (O) Classic One Month                       (P) Super One Month
                (Q) Solar Nova One Month                    (R) Solar Smart One Month
                (S) Solar Super One Month
                """
            print(select_billers2)
            selection8 = input("Enter Option: ")
            selection8 = selection8.strip().lower()

            if selection8 == 'a':
                amount = int(input('Enter amount: '))
            elif selection8 == 'b':
                amount = 90
            elif selection8 == 'c':
                amount = 160
            elif selection8 == 'd':
                amount = 200
            elif selection8 == 'e':
                amount = 300
            elif selection8 == 'f':
                amount = 320
            elif selection8 == 'g':
                amount = 400
            elif selection8 == 'h':
                amount = 600
            elif selection8 == 'i':
                amount = 700
            elif selection8 == 'j':
                amount = 900
            elif selection8 == 'k':
                amount = 1200
            elif selection8 == 'l':
                amount = 1500
            elif selection8 == 'm':
                amount = 1700
            elif selection8 == 'n':
                amount = 2200
            elif selection8 == 'o':
                amount = 2500
            elif selection8 == 'p':
                amount = 4200
            elif selection8 == 'q':
                amount = 9900
            elif selection8 == 'r':
                amount = 10500
            elif selection8 == 's':
                amount = 11400
            print(f"Your {amount} subscription is Successful")

            wish = input("Do you wish to continue with other transaction? Y or N: ")

            if wish.lower() == 'y':
                continue
            else:
                break

            if selection5 == 'd':
                print('MYTV')
                select_billers3 = """
                (A) English - MY TV Smart -1-Month      (B) English - MY TV Smart -3-Months
                (C) English - MY TV Smart -6-Months     (D) English - MY TV Smart -12-Months
                """
                print(select_billers3)

            selection9 = input("Enter option: ")
            selection9 = selection9.strip().lower()

            if selection9 == 'a':
                amount = 500
            elif selection9 == 'b':
                amount = 1450
            elif selection9 == 'c':
                amount = 2800
            elif selection9 == 'd':
                amount = 5400

            print(f"Your {amount} subscription is successful")

            wish = input("Do you wish to continue with other transaction? Y or N: ")

            if wish.lower() == 'y':
                continue
            else:
                break

        if selection4 == 'b':
            print("Sports and Gaming")

            select_billers4 = """
            (A) 360 BETS                       (B) BestBet 360
            (C) 1960Bets                       (D) Bet 9ja
            (E) BetKing                        (F) SportyBet
            """
            print(select_billers4)

            selection10 = input("Enter option: ")
            selection10 = selection10.strip().lower()

            if selection10 == 'a':
                print("Load player account")
                amount = input("Enter amount: ")
                print(f"You have successfully top-up your account with the sum of N{amount}")

                wish = input("Do you wish to continue with other transaction? Y or N: ")

                if wish.lower() == 'y':
                    continue
                else:
                    break

            if selection10 == 'b':
                print("Bet 2 Win")
                amount = input("Enter amount: ")
                print(f"You have successfully top-up your account with the sum of N{amount}")
                wish = input("Do you wish to continue with other transaction? Y or N: ")
                if wish.lower() == 'y':
                    continue
                else:
                    break


            if selection10 == 'c':
                print("1960 Bets")
                amount = input("Enter amount: ")
                print(f"You have successfully top-up your account with the sum of N{amount}")
                wish = input("Do you wish to continue with other transaction? Y or N: ")
                if wish.lower() == 'y':
                    continue
                else:
                    break


            if selection10 == 'd':
                print("Bet 9ja")
                amount = input("Enter amount: ")
                print(f"You have successfully top-up your account with the sum of N{amount}")
                wish = input("Do you wish to continue with other transaction? Y or N: ")
                if wish.lower() == 'y':
                    continue
                else:
                    break


            if selection10 == 'e':
                print("BetKing")
                amount = input("Enter amount: ")
                print(f"You have successfully top-up your account with the sum of N{amount}")
                wish = input("Do you wish to continue with other transaction? Y or N: ")
                if wish.lower() == 'y':
                    continue
                else:
                    break

            if selection10 == 'f':
                print("SportyBet")
                amount = input("Enter amount: ")
                print(f"You have successfully top-up your account with the sum of N{amount}")
                wish = input("Do you wish to continue with other transaction? Y or N: ")
                if wish.lower() == 'y':
                    continue
                else:
                    break


        if selection4 == 'c':
            print("Travel and Hotel")

            select_billers5 = """
            (A) Slim Trader Mobile Book-on-Hold  (B) Discovery Air Book on hold
            (C) Dana Air-Book on Hold            (D) Wakanow
            (E) Hak Air Book-On-Hold             (F) Aero Book-On-Hold
            (G) Arik Air Book-On-Hold            (H) RwandAir Book On Hold
            """
            print(select_billers5)

            selection11 = input("Enter option: ")
            selection11 = selection11.strip().lower()

            if selection11 == 'a':
                print("Welcome to SLIMTRADER")
                print('Slim Trader Mobile Booking')
                amount = int(input("Enter amount: "))
                print(f"Your N{amount} flight booking is successful")
                wish = input("Do you wish to perform another transaction? Y or N: ")

                if wish.lower() == 'y':
                    continue
                else:
                    break

            if selection11 == 'b':
                print("Welcome to DiscoveryAir")
                print('Flight Details')
                amount = int(input("Enter amount: "))
                print(f"Your N{amount} flight booking is successful")
                wish = input("Do you wish to perform another transaction? Y or N: ")

                if wish.lower() == 'y':
                    continue
                else:
                    break

            if selection11 == 'c':
                print("Welcome to DanaAir")
                print('Flight Details')
                amount = int(input("Enter amount: "))
                print(f"Your N{amount} flight booking is successful")
                wish = input("Do you wish to perform another transaction? Y or N: ")

                if wish.lower() == 'y':
                    continue
                else:
                    break

            if selection11 == 'd':
                print("Welcome to Wakanow")
                print('Wakanow Payments')
                amount = int(input("Enter amount: "))
                print(f"Your N{amount} flight booking is successful")
                wish = input("Do you wish to perform another transaction? Y or N: ")

                if wish.lower() == 'y':
                    continue
                else:
                    break

            if selection11 == 'e':
                print("Welcome to HakAir")
                print('Flight Details')
                amount = int(input("Enter amount: "))
                print(f"Your N{amount} flight booking is successful")
                wish = input("Do you wish to perform another transaction? Y or N: ")

                if wish.lower() == 'y':
                    continue
                else:
                    break

            if selection11 == 'f':
                print("Welcome to aero")
                print('Book-On-Hold Payment')
                amount = int(input("Enter amount: "))
                print(f"Your N{amount} flight booking is successful")
                wish = input("Do you wish to perform another transaction? Y or N: ")

                if wish.lower() == 'y':
                    continue
                else:
                    break

            if selection11 == 'g':
                print("Welcome to ArikAir")
                print('Airline Ticket')
                amount = int(input("Enter amount: "))
                print(f"Your N{amount} flight booking is successful")
                wish = input("Do you wish to perform another transaction? Y or N: ")

                if wish.lower() == 'y':
                    continue
                else:
                    break

            if selection11 == 'h':
                print("Welcome to RwandAir")
                print('RwandAir Booking Payment')
                amount = int(input("Enter amount: "))
                print(f"Your N{amount} flight booking is successful")
                wish = input("Do you wish to perform another transaction? Y or N: ")

                if wish.lower() == 'y':
                    continue
                else:
                    break


        if selection4 == 'd':
            print("Electricity")

            select_billers6 = """
            (A) Eko Electricity Distribution Company Plc Postpaid  (B) Enugu Electricity Distribution Company Postpaid
            (C) Ibadan Electricity Distribution Company Postpaid   (D) Benin Electricity Distribution Company Postpaid
            (E) Enugu Electricity Distribution Company Prepaid     (F) Ibadan Electricity Distribution Company Prepaid
            (G) KEDCO Prepaid                                      (H) PortHacourt Electricity Distribution Company (PHED)
            """
            print(select_billers6)

            selection12 = input("Enter option: ")
            selection12 = selection12.strip().lower()

            if selection12 == 'a':
                print("Eko Electricity Distribution Company Plc Postpaid")

                select_billers7 = """
                    (A) Reconnection Fees  (B) Loss of Revenue
                    (C) POSTPAID           (D) Penalties
                    """
                print(select_billers7)

                selection13 = input("Enter option: ")
                selection13 = selection13.strip().lower()

                if selection13 == 'a':
                    print("Reconnection Fees")
                    amount = int(input("Enter Amount: "))
                    print(f"Your N{amount} payment is successful")
                    wish = input("Do you wish to perform another transaction? Y or N: ")

                    if wish.lower() == 'y':
                        continue
                    else:
                        break

                elif selection13 == 'b':
                    print("Loss of Revenue")
                    amount = int(input("Enter Amount: "))
                    print(f"Your N{amount} payment is successful")
                    wish = input("Do you wish to perform another transaction? Y or N: ")

                    if wish.lower() == 'y':
                        continue
                    else:
                        break

                elif selection13 == 'c':
                    print("POSTPAID")
                    amount = int(input("Enter Amount: "))
                    print(f"Your N{amount} payment is successful")
                    wish = input("Do you wish to perform another transaction? Y or N: ")

                    if wish.lower() == 'y':
                        continue
                    else:
                        break

                elif selection13 == 'd':
                    print("Penalties")
                    amount = int(input("Enter Amount: "))
                    print(f"Your N{amount} payment is successful")
                    wish = input("Do you wish to perform another transaction? Y or N: ")

                    if wish.lower() == 'y':
                        continue
                    else:
                        break

            if selection12 == 'b':
                print("POSTPAID Payments")
                amount = int(input("Enter Amount: "))
                print(f"Your N{amount} payment is successful")
                wish = input("Do you wish to perform another transaction? Y or N: ")

                if wish.lower() == 'y':
                    continue
                else:
                    break

            if selection12 == 'c':
                print("Electricity Bill")
                amount = int(input("Enter Amount: "))
                print(f"Your N{amount} payment is successful")
                wish = input("Do you wish to perform another transaction? Y or N: ")

                if wish.lower() == 'y':
                    continue
                else:
                    break

            if selection12 == 'd':
                print("Benin Electricity Distribution Company Postpaid")

                select_billers8 = """
                    (A) POSTPAID                        (B) Penalty
                    (C) Excess Service Charge           (D) Meter Connection Fee Payment
                    (E) Reconnection Fee                (F) Loss of Revenue
                    """
                print(select_billers8)

                selection14 = input("Enter option: ")
                selection14 = selection13.strip().lower()

                if selection14 == 'a':
                    print("POSTPAID")
                    amount = int(input("Enter Amount: "))
                elif selection14 == 'b':
                    print("Penalty")
                    amount = int(input("Enter Amount: "))
                elif selection14 == 'c':
                    print("Excess Service Charge")
                    amount = int(input("Enter Amount: "))
                elif selection14 == 'd':
                    print("Meter Connection Fee Payment")
                    amount = int(input("Enter Amount: "))
                elif selection14 == 'e':
                    print("Reconnection Fee")
                    amount = int(input("Enter Amount: "))
                elif selection14 == 'f':
                    print("Loss of Revenue")
                    amount = int(input("Enter Amount: "))

                    print(f"Your {amount} payment is successful")
                    wish = input("Do you wish to continue with other transaction? Y or N: ")

                    if wish.lower() == 'y':
                        continue
                    else:
                        break

            if selection12 == 'e':
                print("Prepaid")
                amount = int(input("Enter Amount: "))
                print(f"Your N{amount} subscription is successful")
                wish = input("Do you wish to perform another transaction? Y or N: ")

                if wish.lower() == 'y':
                    continue
                else:
                    break

            if selection12 == 'f':
                print("Prepaid")
                amount = int(input("Enter Amount: "))
                print(f"Your N{amount} subscription is successful")
                wish = input("Do you wish to perform another transaction? Y or N: ")

                if wish.lower() == 'y':
                    continue
                else:
                    break

            if selection12 == 'g':
                print("Postpaid Bills")
                amount = int(input("Enter Amount: "))
                print(f"Your N{amount} subscription is successful")
                wish = input("Do you wish to perform another transaction? Y or N: ")

                if wish.lower() == 'y':
                    continue
                else:
                    break

            if selection12 == 'h':
                print("POSTPAID Payments")
                amount = int(input("Enter Amount: "))
                print(f"Your N{amount} subscription is successful")
                wish = input("Do you wish to perform another transaction? Y or N: ")

                if wish.lower() == 'y':
                    continue
                else:
                    break

    if command == "Finish":
        print(f"Thank you for banking with us Mr {user}")
        print("Please take your Card")
        break


