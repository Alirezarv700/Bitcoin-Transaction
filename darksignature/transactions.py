import subprocess

def save_output_to_file(output):
    with open("SignatureRSZ.txt", "a") as file:
        file.write(output)

# Number of signatures in a Bitcoin transaction
for i in range(32):
    process = subprocess.run(
        ["./darksignature", "-pubkey",
         "f3b587144f038f7fd504eaebb2159ad97c0ca33c3cbaf7f3899849a9e2c9074b",
         "42a45c2e288680541b18fce950789d877f08dd293864a5c41786b9509bf8f62d"],
        stdout=subprocess.PIPE,
        universal_newlines=True
    )

    output = f"|ECDSA Signature R,S,Z values from Bitcoin №{i+1}:\n{process.stdout}\n"
    print(output)
    save_output_to_file(output)
