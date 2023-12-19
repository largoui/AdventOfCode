f=open("day5.txt",'r')

lines=f.readlines()

pre = ((lines[0]).split(":")[1]).split()
previous = [int(i) for i in pre]
next=[]

def partition(file):
    res=[]
    intermed=[]
    for line in file:
        if line=="\n":
            res+=[intermed]
            intermed=[]
        elif line[0].isdigit():
            intermed+=[line[:-1]]
    return res

cats=partition(lines[2:])
# print(cats)

for cat in cats:
    # print(cat)
    copy=previous.copy()
    for case in cat:
        nums=case.split()
        for el in previous:
            # print(el, int(nums[1])<=el and el<(int(nums[1])+int(nums[2])))
            if int(nums[1])<=el and el<(int(nums[1])+int(nums[2])):
                # print(el, int(nums[0])+(el-int(nums[1])))
                next+=[int(nums[0])+(el-int(nums[1]))]
                copy.remove(el)
    # print(copy)
    next+=copy
    previous=next
    next=[]

for el in previous:
    next+=[el]
print(min(next))
f.close()