bag={"red": 12, "green": 13, "blue": 14}
f=open("day2_1.txt", 'r')
sum=0

def game_valid(combis):
    for combi in combis:
        colors=combi.split(",")
        for color in colors:
            num=color.split()[0]
            key=color.split()[1]
            if int(num)>bag[key]:
                return False
    return True

for line in f:
    games=line.split(":")
    combis=games[1].split(";")
    if game_valid(combis):
        sum+=int((games[0].split())[1])
f.close()
print(sum)