

def eval_expr(s):
    
    temp = []
    s = s.split() # rozdelenie na list

    for i in range(0, len(s)): # premena cisel na int
        if (s[i].isnumeric()):
            s[i] = int(s[i])

    for item in s:
        
        if (item != "+"):
            temp.append(item)
        else:
            a = temp.pop()
            b = temp.pop()

            temp.append(a + b)


    return temp[0]
