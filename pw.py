#! python3
# shebang line - powyższa linijka wskazuje adres interpretera przy
# uruchomieniu # programu z wiersza poleceń, dla linuxa będzie inna!

# Program pozwala na niezbyt bezpieczne przechowywanie haseł

import sys, pyperclip

PASSWORDS = {'email': '07ewuhmuihyug^@gghjghhhl',
            'blog': 'oimiou8**@HH',
            'walizka': '184'}

if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()
account = sys.argv[1]
# first command line arg iss the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named' + account)