import random
N = int(input("N: "))
san = random.randrange(1, N)
print(san)
sum1=0
sum2=0
i=1
j = 1
while i<=N:
    sum1+=i
    i+=1

for j in range(N+1):
    if j==san:
        continue
    else:
        sum2+=j

print(sum1-sum2)
