f=open("day2_2.txt", 'r')
sum=0

def game_min(combis):
    min_cubes={"red": 0, "green": 0, "blue": 0}
    for combi in combis:
        colors=combi.split(",")
        for color in colors:
            num=color.split()[0]
            key=color.split()[1]
            if int(num)>min_cubes[key]:
                min_cubes[key]=int(num)
    return min_cubes

for line in f:
    games=line.split(":")
    combis=games[1].split(";")
    cubes=game_min(combis)
    power=cubes["red"]*cubes["green"]*cubes["blue"]
    sum+=power
f.close()
print(sum)