target = 199.5
attempt = 1

while True: 
    print(f"\n--- Attempt {attempt} ---")
    marks = []
    
    for i in range(5): 
        m = int(input(f"Subject {i+1} mark /200: "))
        marks.append(m)
    
    cutoff = sum(marks) / 5
    print("Your Cutoff:", cutoff)
    
    if cutoff >= target:
        print("🏆 TARGET ACHIEVED! 🔥")
        print(f"Total attempts: {attempt}")
        break
    else:
        print("Target miss. wnat to improve more💪")
        attempt += 1 