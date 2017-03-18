import re


def parseQ(strQ):
    tmp = strQ

    while True:
        match = re.search(r'(?<=\().*(?=\))', tmp)
        if match:
            match = re.search("(\w+): ([\w\s_:()',\[\]]+)", match.group())
            if match:
                lop, rop = match.groups()
                if lop == 'OR':
                    
