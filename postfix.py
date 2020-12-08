

def eval_expr(s):
    
    temp = []
    s = s.split() # rozdelenie na list

    for item in s:
        
        if (item.isnumeric()): # ak to je cislo, tak sa prida do temp zoznamu
            temp.append(item)
        else: # ak to nie je cislo, tak uz sa predpoklada, ze v temp zozname su uz 2 cisla, tie sa vyberu a daju do "a" a "b"
            a = int(temp.pop())
            b = int(temp.pop())
            
            # potom podla toho, ze ake je znamienko, sa vyhodnoti vysledok
            if (item == "+"):
                temp.append(a + b)
            elif (item == "-"):
                temp.append(b - a)
            elif (item == "*"):
                temp.append(a * b)
            elif (item == "/"):
                temp.append(b // a)


    return temp[0]
