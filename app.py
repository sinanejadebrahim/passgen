import random
import string
from sys import argv
import base64


backup_file = "/etc/.not-passwords"

def help_message():
    print("""
give me a option:
python3 app.py dbpassword   << generate a password with dbpassword name >>
python3 app.py -d dbpassword  << decode a password saved with dbpassword name >>
python3 app.py -l   << list all saved password >>
    """)


def genpass(name):

    chars = string.ascii_letters + string.digits

    password = ''.join(random.sample(chars,18))

    encoded_byte = base64.b64encode(password.encode('utf-8'))

    with open(backup_file, 'a') as file:

        file.write(f"{argv[1]} {encoded_byte.decode('utf-8')} \n")

    return(password)



def show_pass(name):
    saved_pass = {}

    with open(backup_file, 'r') as file:

        for line in file:
            if name in line:
                name, password = line.strip().split()
                saved_pass[name] = password
                decoded_byte = base64.b64decode(password)
                return decoded_byte.decode('utf-8')
        else:
            return "no such password found, use -l to list all passwords"


def list():
    with open(backup_file, 'r') as file:
        print(file.read())


if len(argv) < 2:
    help_message()
    exit()

elif argv[1] == "-l" :
    list()

elif argv[1] == "-d":
    name = argv[2]
    decoded_password = show_pass(name)
    print(decoded_password)


else:
    name = argv[1]
    password = genpass(name)
    print(password)
