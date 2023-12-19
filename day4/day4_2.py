with open("day4.txt",'r') as f:
    lines=f.readlines()
    nbr_cards=len(lines)
    i=0
    while i<len(lines):
        card= lines[i].split(':')[1]
        card_nbr=int(lines[i].split(':')[0].split()[1])
        winning=card.split('|')[0].split()
        numbers=card.split('|')[1].split()
        for num in numbers:
            if num in winning:
                card_nbr+=1
                if card_nbr-1<nbr_cards:
                    lines.append(lines[card_nbr-1])
        i+=1
    
print(i)
