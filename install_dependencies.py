import os

file = "requirements.txt"

opened_file = open(file)

lines = opened_file.readlines()

print("I'm about to install the following dependencies: ")
count = 0
for line in lines:
    count += 1
    print(f"\t{count}: {line}")

response = input("\n Would you like me to procceed? (Y/N): ").lower()

if response == 'y':
    for line in lines:
        if len(line) > 2:
            os.system(f"pip install {line}")

    print("Dependencies were succesfully installed!")
else:
    print("Cancelled process!")

os.system("pause")
