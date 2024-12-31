print()
print("30 Days Down - What did you think?")
print()

for i in range(1,31):
    thought = input(f"Day {i}:\n")
    print()
    mytext = f"You thought Day{i} was"
    print(f"{mytext:^35}")
    print(f"{thought:^35}")
    print()
    
