import os
print('''
      







:::'###::::'##::::'##::'######::'########:'####::'#######::'##::: ##:
::'## ##::: ##:::: ##:'##... ##:... ##..::. ##::'##.... ##: ###:: ##:
:'##:. ##:: ##:::: ##: ##:::..::::: ##::::: ##:: ##:::: ##: ####: ##:
'##:::. ##: ##:::: ##: ##:::::::::: ##::::: ##:: ##:::: ##: ## ## ##:
 #########: ##:::: ##: ##:::::::::: ##::::: ##:: ##:::: ##: ##. ####:
 ##.... ##: ##:::: ##: ##::: ##:::: ##::::: ##:: ##:::: ##: ##:. ###:
 ##:::: ##:. #######::. ######::::: ##::::'####:. #######:: ##::. ##:
..:::::..:::.......::::......::::::..:::::....:::.......:::..::::..::


                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\/
                         `'-------'`
                       .-------------.
                   jgs/_______________\/
''')
print("Welcome to the secrate auction program: ")
nxt_bid = True
aution_bid={}
i = 0
while nxt_bid:
    i += 1
    aution_bid[i]={}
    name = input("Enter your name : ")
    bid = int(input("What's your bid? $"))
    aution_bid[i]['name']= name
    aution_bid[i]['bid'] = bid
    nxt = input("Are there any other bidders? Type 'Yes' or 'No' : ").lower()
    if nxt == 'yes':
        nxt_bid = True
        os.system('clear')
    elif nxt == 'no':
        nxt_bid = False
for i in aution_bid:
    for j in aution_bid:
        if aution_bid[i]['bid'] >= aution_bid[j]['bid']:
            value1 = aution_bid[i]['bid']
        else:
            value2 = aution_bid[j]['bid']

for i in aution_bid:
    if aution_bid[i]['bid'] == value2:
        print(f"The Winner is {aution_bid[i]['name']} with a bid of ${aution_bid[i]['bid']} ")        
