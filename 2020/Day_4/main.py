f = open('input.txt')
data = f.readlines()
newData = []
newRow = []

partOne = False

for row in data:
    if row != '\n':
        if(row[-1] == '\n'):
            newRow.append(row[:-1])
        else:
            newRow.append(row)
    else:
        newRow = [" ".join(newRow)]
        newData.append(newRow)
        newRow = []
    if row == data[-1]:
        newRow = [" ".join(newRow)]
        newData.append(newRow)


numValid = 0
for passport in newData:
    num_missing = 0
    num_valid_fields = 0
    cid_missing = False
    if 'ecl' not in passport[0]:
        num_missing = num_missing+1
    else:
        index = passport[0].index('ecl')
        color = passport[0][index+4:index+7]
        x = color in 'ambblubrngrygrnhzloth'
        if (color in 'ambblubrngrygrnhzloth'):
            num_valid_fields = num_valid_fields + 1
    if 'pid' not in passport[0]:
        num_missing = num_missing + 1
    else:
        index = passport[0].index('pid')
        if passport[0].find(' ', index) == -1:
            id = passport[0][index + 4:]
        else:
            id = passport[0][index + 4:passport[0].find(' ', index)]
        skip = False
        for num in id:
            if num not in ('0123456789'):
                skip = True
                break
        if (not skip and len(id) == 9):
            num_valid_fields = num_valid_fields + 1
    if 'eyr' not in passport[0]:
        num_missing = num_missing + 1
    else:
        index = passport[0].index('eyr')
        if passport[0].find(' ', index) == -1:
            year = passport[0][index + 4:]
        else:
            year = passport[0][index + 4:passport[0].find(' ', index)]
        if int(year) >= 2020 and int(year)<= 2030 and len(year) == 4:
            num_valid_fields = num_valid_fields + 1
    if 'hcl' not in passport[0]:
        num_missing = num_missing + 1
    else:
        index = passport[0].index('hcl')
        if passport[0].find(' ', index) == -1:
            hcolor = passport[0][index + 4:]
        else:
            hcolor = passport[0][index+4:passport[0].find(' ',index)]
        skip = False
        if (hcolor[0] =='#' and len(hcolor) ==7):
            for i in hcolor[1:]:
                if (i not in '0123456789') and (i not in 'abcdef'):
                    skip = True
                    break
            if not skip:
                num_valid_fields = num_valid_fields + 1
    if 'byr' not in passport[0]:
        num_missing = num_missing + 1
    else:
        index = passport[0].index('byr')
        if passport[0].find(' ', index) == -1:
            birth = passport[0][index + 4:]
        else:
            birth = passport[0][index + 4:passport[0].find(' ', index)]
        if int(birth) >= 1920 and int(birth)<= 2002 and len(birth) == 4:
            num_valid_fields = num_valid_fields + 1
    if 'iyr' not in passport[0]:
        num_missing = num_missing + 1
    else:
        index = passport[0].index('iyr')
        if passport[0].find(' ', index) == -1:
            issue = passport[0][index + 4:]
        else:
            issue = passport[0][index + 4:passport[0].find(' ', index)]
        if int(issue) >= 2010 and int(issue)<= 2020 and len(issue) == 4:
            num_valid_fields = num_valid_fields + 1
    if 'cid' not in passport[0]:
        num_missing = num_missing + 1
        cid_missing = True
    if 'hgt' not in passport[0]:
        num_missing = num_missing + 1
    else:
        index = passport[0].index('hgt')
        if passport[0].find(' ', index) == -1:
            height = passport[0][index + 4:]
        else:
            height = passport[0][index + 4:passport[0].find(' ', index)]
        if height.find('cm') != -1:
            if int(height[:height.find('cm')]) >= 150 and int(height[:height.find('cm')]) <= 193:
                num_valid_fields = num_valid_fields + 1
        else:
            if int(height[:height.find('in')]) >= 59 and int(height[:height.find('in')]) <= 76:
                num_valid_fields = num_valid_fields + 1
    if partOne:
        if cid_missing:
            if num_missing == 1:
                numValid = numValid + 1
        else:
            if num_missing == 0:
                numValid = numValid + 1
    else:
        if num_valid_fields == 7:
            if cid_missing:
                if num_missing == 1:
                    numValid = numValid + 1
            else:
                if num_missing == 0:
                    numValid = numValid + 1

print(f'Valid passports detected: {numValid}')
