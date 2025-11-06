import random, string

def generate_test_email():
    username = ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(5, 10)))
    return f"{username}@example.com"

def generate_incorrect_email():
    username = ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(5, 10)))
    return f"{username}#example.com"