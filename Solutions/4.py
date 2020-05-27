palindrom = 0     
for i in range(999, 100, -1):
    for j in range(999, 100, -1):
        m = i * j
        if str(m) == str(m)[::-1]:           
            if m > palindrom:
                palindrom = m
                
# 906609
print palindrom
            
