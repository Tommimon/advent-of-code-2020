key = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
forbidden_letters=['g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
eye_colors=['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
number_set=[0,1,2,3,4,5,6,7,8,9]
letters_set=['a','b','c','d','e','f']

def verify(verification_array):
    if sum(check)!=7:
        return 0
    return 1
    
def compute(type, value):

    if type == 'byr' and ((int(value)<1920) or (int(value)>2002)):
        return 0

    if type == 'iyr' and ((int(value)<2010) or (int(value)>2020)):
        return 0

    if type == 'eyr' and ((int(value)<2020) or (int(value)>2030)):
        return 0

    if type == 'hgt' :
        if 'cm' in value:
            value=int(value.replace('cm', ''))
            if (value<150) or (value>193):
                return 0
        elif 'in' in value:
            value=int(value.replace('in', ''))          
            if (value<59) or (value>76):
                return 0
        return 1

    if type == 'hcl' :
        if len(value) != 7:
            return 0                  
        else:
            if ('#' not in value):
                return 0
                
            for i in value:
                for forbidden in forbidden_letters:
                    if i == forbidden:
                        return 0          
        return 1

    if type == 'ecl':
        flag=0
        for color in eye_colors:
            if color == value:  
                flag=1
        return flag

    if type == 'pid' :
        if len(value)!= 9 :
            return 0
        return 1    

    if type == 'cid':
        return 1
    else: 
        return 1


with open('marcoparadina/4/input_d4.txt') as f:
    x=[]
    arr=[]
    check=[0]*7
    valid_passports=0
    
    for line in f:
    
        if line == '\n':      
            for el in key:
                if el in arr:
                    check[key.index(el)]=1   
        
            verification_array=sum(check)            
            if sum(check) == 7:
                index=0
                valid=1
                while index<14:
                    valid = valid * compute(arr[index], arr[index+1])
                    index+=2
                valid_passports = valid_passports + valid
            x=[]
            arr=[]
            check=[0]*7
        else:
            # If the current line is not empty i collect all it contains in a single array. 
            # Eventually said array will contain all the data of a passport
            replaced=line.replace(':', ' ')            
            x=replaced.split()            
            arr+=x            
        
print('Part 2 solution:', valid_passports)       

