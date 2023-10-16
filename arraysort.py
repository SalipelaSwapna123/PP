array=[]
evenarr=[]
oddarr=[]
n=int(input("Enter no.of elements in an array : "))
for i in range(0,n):
    number=int(input("Enter element at {} index : ".format(i)))
    array.append(number)
    if i%2==0:
        evenarr.append(array[i])
    else:
        oddarr.append(array[i])
evenarr=sorted(evenarr)
print("sorted array is : ",evenarr[0:len(evenarr)])
oddarr=sorted(oddarr)

print("sorted array is : ",oddarr[0:len(oddarr)])

print("Sum of 2nd largest numbers in both arrays is : ",evenarr[-2]+oddarr[-2])
