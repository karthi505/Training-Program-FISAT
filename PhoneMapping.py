#Phone mapping
phone={"2":['a','b','c'],"3":['d','e','f'],"4":['g','h','i'],"5":['j','k','l'],"6":['m','n','o'],"7":['p','q','r'],"8":['s','t','u','v'],"9":['w','x','y','z']}
n=input()
if n==" ":
    l3=[]
else:
    l3=['']
    for i in range(len(n)):
        if n[i] in phone:
            l1=phone[n[i]]
        l2=[]
        for j in l3:
            for k in l1:
                l2.append(j+k)
        l3=l2
print(l3)

