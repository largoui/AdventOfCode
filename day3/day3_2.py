f=open("day3.txt",'r')
sum=0

def issymbol(char):
    return char=="*"

def hasdigit(str):
    for i in range(len(str)):
        if str[i].isdigit():
            return (True,i)
    return (False, None)

def extract_digit(digit, line, start):
    dig=digit
    for j in range(start+1,len(line)):
        if line[j].isdigit():
            dig+=line[j]
        else:
            break
    for k in range(start-1,-1,-1):
        if line[k].isdigit():
            dig=line[k]+dig
        else:
            break
    return dig
        
lines = f.readlines()

for k in range(len(lines)):
    line=lines[k].replace('\n','')
    ratio=1
    for i in range(len(line)):
        if issymbol(line[i]):
            adjacent=[]
            if i>=1 and line[i-1].isdigit():
                digit=extract_digit(line[i-1],line,i-1)
                adjacent.append(int(digit))
            if i+1<len(line) and line[i+1].isdigit():
                digit=extract_digit(line[i+1],line,i+1)
                adjacent.append(int(digit))
            if k+1<len(lines) and hasdigit(lines[k+1][max(0,i-1):min(i+2,len(lines[k+1]))])[0]:
                if lines[k+1][i-1].isdigit() and lines[k+1][i]=='.' and lines[k+1][i+1].isdigit():
                    index=i+1
                    digit=extract_digit(lines[k+1][index],lines[k+1],index)
                    adjacent.append(int(digit))
                index=max(0,i-1)+hasdigit(lines[k+1][max(0,i-1):min(i+2,len(lines[k+1]))])[1]
                digit=extract_digit(lines[k+1][index],lines[k+1],index)
                adjacent.append(int(digit))
            if k-1>=0 and hasdigit(lines[k-1][max(0,i-1):min(i+2,len(lines[k-1]))])[0]:
                if lines[k-1][i-1].isdigit() and lines[k-1][i]=='.' and lines[k-1][i+1].isdigit():
                    index=i+1
                    digit=extract_digit(lines[k-1][index],lines[k-1],index)
                    adjacent.append(int(digit))
                index=max(0,i-1)+hasdigit(lines[k-1][max(0,i-1):min(i+2,len(lines[k-1]))])[1]
                digit=extract_digit(lines[k-1][index],lines[k-1],index)
                adjacent.append(int(digit))
            print(adjacent)
            if len(adjacent)==2:
                ratio=adjacent[0]*adjacent[1]
                sum+=ratio
f.close()
print(sum)