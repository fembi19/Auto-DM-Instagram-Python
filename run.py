import json
import random
from src.instadm import InstaDM

from colorama import init
from termcolor import colored

f = open('setting/accounts.json',)
accounts = json.load(f)

with open('setting/usernames.txt', 'r') as f:
    usernames = [line.strip() for line in f]

with open('setting/messages.txt', 'r') as f:
    messages = [line.strip() for line in f]


print('--------------------------------------------------------------------------------\n')
print(colored('**-- Aplikasi Kirim Pesan Instagram Otomatis By Fembi Nur Ilham --**', 'blue'))
print('--------------------------------------------------------------------------------\n')


def progress(percent=0, width=40):
    left = width * percent // 100
    right = width - left

    tags = "#" * left
    spaces = " " * right
    percents = f"{percent:.0f}%"

    print("\r[", tags, spaces, "]", percents, sep="", end="", flush=True)


while True:
    if not usernames:
        print('** Selesai **')
        print('--------------------------------------------------------------------------------\n')
        break

    for account in accounts:
        if not usernames:
            break

        # Auto login
        insta = InstaDM(username=account["username"],
                        password=account["password"], headless=False)

        total = 0
        for i in range(len(usernames)):
            total += 1
            progress(round(total/len(usernames)*100))
            print(' ')

            if not usernames:
                break

            username = usernames.pop()
            # Send message
            insta.sendMessage(
                user=username, message=random.choice(messages))

        insta.teardown()
