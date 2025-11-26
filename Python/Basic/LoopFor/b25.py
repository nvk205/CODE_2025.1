# In các số chẵn chia hết cho 3 bé hơn 100
i = 0
while i%6 != 0:
    i += 1
while i%6 == 0:
    print(i)
    i += 6
    if i >= 100: 
        break
            