#
n = 10
result_list = list()
while(n > 0):
    result_list.append(n % 2)
    n = n // 2

result_ans = " "
binary_rep = result_list[::-1]
print("Binary Representation of the deimcal: ",binary_rep)

output_rep = list()
#convert(compliment of the binary)
for i in binary_rep:
    if i == 0:
        #print(result_ans)
        output_rep.append('1')
    else:
        output_rep.append('0')

print(result_ans)
print("Toggled Binary: ",output_rep)
result = 0

#binary to decimal
for i in range(len(output_rep)):
    result = result + (int(output_rep[i]) * pow(2,(len(output_rep)-1)- i))

print("Result after Toggling: ",result)
