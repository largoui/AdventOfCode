f=open("day3.txt",'r')
sum=0

def issymbol(char):
    if (char!='.') and (not char.isdigit()):
        return True
    return False

def hassymbol(str):
    for char in str:
        if issymbol(char):
            return True
    return False

def extract_digit(digit, line, start):
    dig=digit
    for j in range(start+1,len(line)):
        if line[j].isdigit():
            dig+=line[j]
        else:
            end=j
            break
    return dig
        
lines = f.readlines()

for k in range(len(lines)):
    line=lines[k].replace('\n','')
    i=0
    while i<len(line):
        if line[i].isdigit():
            digit=extract_digit(line[i], line, i)
            if i>=1 and issymbol(line[i-1]):
                sum+=int(digit)
            elif i+len(digit)<len(line) and issymbol(line[i+len(digit)]):
                sum+=int(digit)
            elif k+1<len(lines) and hassymbol(lines[k+1][max(0,i-1):min(i+len(digit)+1,len(line))]):
                print(digit)
                sum+=int(digit)
            elif k-1>=1 and hassymbol(lines[k-1][max(0,i-1):min(i+len(digit)+1,len(line))]):
                print(digit)
                sum+=int(digit)
            i+=len(digit)
        else:
            i+=1
f.close()
print(sum)