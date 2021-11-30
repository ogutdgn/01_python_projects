largest = 0
for i in range(1,10000):
    peak = ""
    inti = 1
    while len(peak) < 9:
        peak += str(i * inti)
        inti += 1
    if ((len(peak) == 9) and (len(set(peak)) == 9) and ('0' not in peak)):
        if int(peak) > largest:
            largest = int(peak)
print(largest)
    
