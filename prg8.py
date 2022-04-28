n=int(input("Enter the range: "))
list=[]
for i in range(n):
    value=int(input("Enter the element: "))
    list.append(value)

histogram = ''
for i in range(len(list)):
    histogram = ' '
    while list[i] > 0 :
        histogram = histogram + '#'
        list[i]-=1
    print(histogram)