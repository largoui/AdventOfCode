f=open("day4.txt",'r')
sum=0

lines=f.readlines()
for line in lines:
    card= line.split(':')[1]
    winning=card.split('|')[0].split()
    numbers=card.split('|')[1].split()
    i=0
    for num in numbers:
        if num in winning:
            if i==0:
                i+=1
            else:
                i*=2
    sum+=i
f.close()
print(sum)