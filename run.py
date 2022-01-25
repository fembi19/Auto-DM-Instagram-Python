import json
import random
from src.instadm import InstaDM

f = open('accounts.json',)
accounts = json.load(f)

with open('usernames.txt', 'r') as f:
    usernames = [line.strip() for line in f]

with open('messages.txt', 'r') as f:
    messages = [line.strip() for line in f]

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

        for i in range(50):

            if not usernames:
                break

            username = usernames.pop()
            # Send message
            insta.sendMessage(
                user=username, message=random.choice(messages))

        insta.teardown()
