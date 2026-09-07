n1 = int(input())
n2 = int(input())

l1 = list()
l2 = list()

while(n1 != 0):
    l1.append(int(input().strip()))

    n1 = n1 - 1

while(n2 != 0):
    l2.append(int(input().strip()))

    n2 = n2 - 1


l1.extend(l2)
l3 = l1
l3 = sorted(l3)

sorted_set = set(l3)
print(sorted_set)

#set is not subscripable thing, so converting back to list
l3 = list(sorted_set)


leng = len(sorted_set)
if(leng % 2 == 0):
    midpoint = (l3[leng//2] + l3[leng//2 - 1]) / 2
    print(midpoint)

else:
    middle = l3[leng // 2]
    print(middle)
