def count_words(text):
    count = len(text.split())
    
    return count

def count_characters(book):
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    f = 0
    g = 0
    h = 0
    i = 0
    j = 0
    k = 0
    l = 0
    m = 0
    n = 0
    o = 0
    p = 0
    q = 0
    r = 0
    s = 0 
    t = 0
    u = 0
    v = 0
    w = 0
    x = 0
    y = 0
    z = 0
    dot = 0
    comma = 0
    colon = 0
    space = 0
    zero = 0
    one = 0
    two = 0
    three = 0
    four = 0
    five = 0
    six = 0
    seven = 0
    eight = 0
    nine = 0
    openpar = 0
    endpar = 0
    slash = 0
    dash = 0
    apostrophe = 0
    dollar = 0
    semicolon = 0
    star = 0
    question = 0
    exclamation = 0



    for character in book:
        if character.lower() == "a":
            a += 1
        elif character.lower() == "b":
            b += 1
        elif character.lower() == "c":
            c += 1
        elif character.lower() == "d":
            d += 1
        elif character.lower() == "e":
            e += 1
        elif character.lower() == "f":
            f += 1
        elif character.lower() == "g":
            g += 1
        elif character.lower() == "h":
            h += 1
        elif character.lower() == "i":
            i += 1
        elif character.lower() == "j":
            j += 1
        elif character.lower() == "k":
            k += 1
        elif character.lower() == "l":
            l += 1
        elif character.lower() == "m":
            m += 1
        elif character.lower() == "n":
            n += 1
        elif character.lower() == "o":
            o += 1
        elif character.lower() == "p":
            p += 1
        elif character.lower() == "q":
            q += 1
        elif character.lower() == "r":
            r += 1
        elif character.lower() == "s":
            s += 1
        elif character.lower() == "t":
            t += 1
        elif character.lower() == "u":
            u += 1
        elif character.lower() == "v":
            v += 1
        elif character.lower() == "w":
            w += 1
        elif character.lower() == "x":
            x += 1
        elif character.lower() == "y":
            y += 1
        elif character.lower() == "z":
            z += 1
        elif character.lower() == ".":
            dot += 1
        elif character.lower() == ",":
            comma += 1
        elif character.lower() == ":":
            colon += 1
        elif character.lower() == " ":
            space += 1
        elif character.lower() == "0":
            zero += 1
        elif character.lower() == "1":
            one += 1
        elif character.lower() == "2":
            two += 1
        elif character.lower() == "3":
            three += 1
        elif character.lower() == "4":
            four += 1
        elif character.lower() == "5":
            five += 1
        elif character.lower() == "6":
            six += 1
        elif character.lower() == "7":
            seven += 1
        elif character.lower() == "8":
            eight += 1
        elif character.lower() == "9":
            nine += 1
        elif character.lower() == "(":
            openpar += 1
        elif character.lower() == ")":
            endpar += 1
        elif character.lower() == "/":
            slash += 1
        elif character.lower() == "-":
            dash += 1
        elif character.lower() == "'":
            apostrophe += 1
        #elif character.lower() == "":
            #quote += 1
        elif character.lower() == "$":
            dollar += 1
        elif character.lower() == ";":
            semicolon += 1
        elif character.lower() == "*":
            star += 1
        elif character.lower() == "?":
            question += 1
        elif character.lower() == "!":
            exclamation += 1
        else:
            pass
    
    characterdict = {
        'a': a,
        'b': b,
        'c': c,
        'd': d,
        'e': e,
        'f': f,
        'g': g,
        'h': h,
        'i': i,
        'j': j,
        'k': k,
        'l': l,
        'm': m,
        'n': n,
        'o': o,
        'p': p,
        'q': q,
        'r': r,
        's': s,
        't': t,
        'u': u,
        'v': v,
        'w': w,
        'x': x,
        'y': y,
        'z': z,
        '.': dot,
        ',': comma,
        ' ': space,
        '0': zero,
        '1': one,
        '2': two,
        '3': three,
        '4': four,
        '5': five,
        '6': six,
        '7': seven,
        '8': eight,
        '9': nine,
        '(': openpar,
        ')': endpar,
        '/': slash,
        '-': dash,
        '´': apostrophe,
        '$': dollar,
        ';': semicolon,
        '*': star,
        '?': question,
        '!': exclamation,



     }

    return characterdict
        
def report_data(data):
    
    dict = {

    }
    list= []
    for num in data:
        dict = {"character": num, "count": data[num]}
        list.append(dict)
       # report_data["character": num] = {"count": data[num]}
    
    def sort_on(list):
        return list["count"]
    
    list.sort(reverse=True, key=sort_on)

    return list



