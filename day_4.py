
file = open('day_4.txt', 'r')
data = file.read().split('\n\n')

test_list = ['iyr', 'ecl', 'byr', 'hcl', 'eyr', 'hgt', 'pid']

color_list = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
res = dict((sub, 4) for sub in test_list) 

count = 0
count_1 = 0

def check(a):
    check_dict = dict((a[x], a[x+1]) for x in range(0, len(a)-1, 2))
    if len(check_dict['iyr']) == 4:
        if int(check_dict['iyr']) < 2010 or int(check_dict['iyr']) > 2020:
            return 0
    else:
        return 0
    if len(check_dict['byr']) == 4:
        if int(check_dict['byr']) < 1920 or int(check_dict['byr']) > 2002:
            return 0  
    else:
        return 0
    if len(check_dict['eyr']) == 4:
        if int(check_dict['eyr']) < 2020 or int(check_dict['eyr']) > 2030:
            return 0    
    else:
        return 0
    hcl = check_dict['hcl']
    if hcl[0] == '#' and len(hcl) == 7:
        for i in hcl[1:]:
            if i.isalpha():
                if ord(i) < 97 or ord(i) > 102:
                    return 0
            else:
                if int(i) < 0 or int(i) > 9:
                    return 0
    else:
        return 0
    hgt = check_dict['hgt']
    unit = hgt[len(hgt)-2:]
    check1 = hgt[len(hgt)-2:] in ['in', 'cm']
    if check1:
        x = int(hgt[:len(hgt)-2])
        if unit == 'in':
            if x < 59 or x > 76:
                return 0
        else:
            if x < 150 or x > 193:
                return 0
               
    else:
        return 0
    if len(check_dict['pid']) != 9:
        return 0
    if check_dict['ecl'] not in color_list:
        return 0
    return 1
for a in data:
    print(a)
    a = a.replace(':', ' ')
    a = a.split()
    print(a)
    for i in test_list:
        if i not in a:
            break
    else:
        count += check(a)
        count_1 += 1
print(count)
print(count_1)