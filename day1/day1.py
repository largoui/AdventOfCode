digits=("one", "two", "three", "four", "five", "six", "seven", "eight", "nine")
word_to_number = {
    'one': "1",
    'two': "2",
    'three': "3",
    'four': "4",
    'five': "5",
    'six': "6",
    'seven': "7",
    'eight': "8",
    'nine': "9"
}
def extract_substring_from_list(target_string, substrings):
    for substring in substrings:
        if substring in target_string[:4]:
            return substring
    for substring in substrings:
        if substring in target_string[:5]:
            return substring

def extract_substring_from_list_reverse(target_string, substrings):
    for substring in substrings:
        if substring in target_string[len(target_string)-4:]:
            return substring
    for substring in substrings:
        if substring in target_string[len(target_string)-5:]:
            return substring

sum=0
f=open("day1.txt","r")
for line in f:
    number=""
    for i in range(len(line)):
        if line[i:].startswith(digits):
            digit=extract_substring_from_list(line[i:],digits)
            number+=word_to_number[digit]
            break
        elif line[i:i+1].isdigit():
            number+=line[i:i+1]
            break
        
    for j in range(len(line)):
        if line[:len(line)-j].endswith(digits):
            digit=extract_substring_from_list_reverse(line[:len(line)-j],digits)
            number+=word_to_number[digit]
            break
        elif line[len(line)-j-1:len(line)-j].isdigit():
            number+=line[len(line)-j-1:len(line)-j]
            break
    print(number)
    sum+=int(number)
f.close()
print(sum)