# Day 5: Lists Simple Version
marks = [200, 200, 199, 200, 200] 

total = sum(marks)
cutoff = total / 5

print("Marks:", marks)
print("Cutoff:", cutoff)

    if cutoff >= 199.5:
    print("Top College Eligible - Great score!")
else:
    print("Good Score - Aim higher next time")