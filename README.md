# Password Generator and Manager

This Python script is a simple tool for generating and managing passwords. It allows you to generate passwords and save an **encoded** version in a file for future reference. no extra modules are needed to be installed.

## Usage

### Generate a Password
To generate a password with a specific name (e.g., dbpassword), use the following command:

python3 app.py dbpassword

### Decode a Password
If you want to decode and retrieve a password saved with a specific name (e.g., dbpassword), use the following command:

python3 app.py -d dbpassword

### List All Saved Passwords
To list all the passwords saved by the script, use the following command:

python3 app.py -l

#### alias
for simpler use you can set an alias like this `alias passgen='python3 (address to file)/app.py'` 

then use it like this:
```
passgen webDB
passgen -d webDB
```


## Examples

### Generate a Password
python3 app.py website_password

This will generate a strong password and save it with the name "website_password."

### Decode a Password
python3 app.py -d email_password

This will decode and display the password saved with the name "email_password."

### List All Saved Passwords
python3 app.py -l

This will display a list of all the saved passwords.

## Notes
- Make sure to remember the names you use for passwords, as they are needed for decoding.
- Passwords are saved in a file for future reference.
