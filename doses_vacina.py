def main():
    contents = []
    
    while True:
        try:
            line = input()
            contents.append(line)
        except:
            break
    
        contents = [int(x) for x in contents]
        #print(contents)
    
    doses = 4
    for i in range(doses-1):
        a = contents[0]
        p = contents[1]
        ano = a + (p*(i+1))
        print(ano, end=" ")
main()