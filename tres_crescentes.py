def tres_c():
    contents = []
    while True:
        try:
            line = input()
            contents.append(line)
        except EOFError:
            break
        
        #print(contents)
        contents = [int(x) for x in contents]
        contents = sorted(contents)
        #print(contents)
    
    print (*contents, sep="\n")

def tres_c():
    contents = []
    while True:
        try:
            line = input()
            contents.append(line)
        except EOFError:
            break
        
        #print(contents)
        contents = [int(x) for x in contents]
        contents = sorted(contents)
        #print(contents)
    
    print (*contents, sep="\n")

tres_c()