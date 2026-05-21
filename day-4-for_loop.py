total = 0
for i in range(1, 6):
    mark = int(input(f"Enter Subject {i} mark /200: "))
    if mark < 0 or mark > 200:
        print("Please enter marks between 0 and 200")
        exit()
    total += mark

cutoff = total / 5
print("Your TNEA Cutoff:", cutoff)

if cutoff >= 199.5:
    print("Eligible for CEG CSE 🔥")
elif cutoff >= 198:
    print("Eligible for MIT/PSG CSE 💪")
else:
    print("Eligible for SSN CSE with scholarship 🚀")