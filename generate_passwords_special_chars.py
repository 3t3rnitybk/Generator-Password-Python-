import random
import string

def generate_password(length=10):
    # Lista de simboluri acceptate (fără ~ și `)
    symbols = "!@#$%^&*()_+-={}[]|\\:;\"'<>,.?/"
    characters = string.ascii_letters + string.digits + symbols
    return ''.join(random.choice(characters) for _ in range(length))

def generate_passwords_continuous(filename, length=10):
    with open(filename, 'a') as f:
        try:
            while True:
                pwd = generate_password(length)
                f.write(pwd + '\n')
        except KeyboardInterrupt:
            print("\nGenerare oprită manual.")

if __name__ == "__main__":
    output_file = "passwords_continuous.txt"
    generate_passwords_continuous(output_file)
