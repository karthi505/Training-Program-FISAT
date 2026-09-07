n = "1 2 3 4 8"
spike = 2

res = ""

for i in n:
    if i == " ":
        continue

    elif i.isdigit():
        
        binary = bin(int(i))
        binary = binary[2:]
        #print(binary)
        str_binary = str(binary)
        
        if(len(str_binary) > spike):
            
            str_binary = str_binary[ : -spike]
            res = res + str(int(str_binary,2))
        else:
            res = res + "0"
            
    print(res)
    

