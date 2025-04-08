from ecdsa import SECP256k1
from ecdsa.ellipticcurve import Point

import csv

N = 0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141
curve = SECP256k1
G = curve.generator

def extended_gcd(a, b):
    lastrem, rem = abs(a), abs(b)
    x, lastx, y, lasty = 0, 1, 1, 0
    while rem:
        lastrem, (q, rem) = rem, divmod(lastrem, rem)
        x, lastx = lastx - q * x, x
        y, lasty = lasty - q * y, y
    return lastrem, lastx, lasty

def modinv(a, n):
    g, x, y = extended_gcd(a, n)
    return x % n

def load_signatures(filename):
    signatures = []
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            r = int(row[0], 16)
            s = int(row[1], 16)
            z = int(row[2], 16)
            signatures.append((r, s, z))
    return signatures

def test_brute_force_x(r, s, z, r_target):
    print("Trying brute-force on private key...")
    for x_guess in range(1, 100000):  # فقط برای تست، می‌تونی رنج رو بزرگتر کنی
        k = ((z + r * x_guess) * modinv(s, N)) % N
        R = k * G
        if R.x() % N == r_target:
            print(">>> FOUND!")
            print("Private Key x:", hex(x_guess))
            print("Recovered Nonce k:", hex(k))
            return x_guess, k
    print("Not found in range.")
    return None, None

signatures = load_signatures("SignRSZ.txt")

# فقط روی اولین امضا تست می‌کنیم
r, s, z = signatures[0]
test_brute_force_x(r, s, z, r)
