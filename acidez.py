def entrada():
    while True:
            try:
                line = float(input())
                if line == -1.0:
                    break
                else:
                    consulta(line)
            except:
                
                    break

def consulta(line):
     
     if 0 < line <= 6.9:
        print("ACIDA")

     elif 7.1<= line <= 14.0:
        print("BASICA")

     elif line == 7.0:
        print("NEUTRA")

entrada()