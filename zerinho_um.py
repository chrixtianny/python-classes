def main():
    
    num = []
    x = 0
    while x < 3:
        try:
            n = int(input())

            if n == 0 or n == 1:
                num.append(n)
                #print(num)
            else:
                main()
        except: 
            break
        x+=1
    
    if num[0] != num[1] and num[0] != num[2]:
        print("A")
    elif num[1] != num[0] and num[1] != num[2]:
        print("B")
    elif num[2] !=num[0] and num[2] != num[1]:
        print("C")
    else:
        print("*") 

main()

