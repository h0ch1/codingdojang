total = 0
for h in range(24): #시간
    for m in range(60): #분
        if '3' in str(h) or '3' in str(m):
            total += 60

print (total)