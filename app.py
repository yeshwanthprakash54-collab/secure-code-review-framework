AWS_SECRET_ACCESS_KEY = "AKIA1234567890SECRET"
API_KEY = "sk_live_51Hxxxxxxxxxxxxxxxxxxxx"
DB_PASSWORD = "Password@123"
import os
import hashlib

# 1️⃣ Hardcoded password (Security Risk)
DB_PASSWORD = "SuperSecret123"

# 2️⃣ Weak hashing (MD5)
def hash_password(password):
    import hashlib

def hash_password(password):
    return hashlib.pbkdf2_hmac(
        'sha256',
        password.encode(),
        b'salt',
        100000
    ).hex()

# 3️⃣ Command Injection Risk
def ping_host(host):
    os.system("ping " + host)

# 4️⃣ Unsafe eval (Code Execution Risk)
def calculate():
    user_input = input("Enter calculation: ")
    result = eval(user_input)
    print(result)

if __name__ == "__main__":
    print("Hashed:", hash_password("admin"))
    ping_host("127.0.0.1")