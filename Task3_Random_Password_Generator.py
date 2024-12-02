import secrets
import string

def generate_pw(Len):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(characters) for _ in range(Len))

Len = int(input("Please specify the desired Length of the password: "))
pw = generate_pw(Len)

print("Generated password is:-", pw)

