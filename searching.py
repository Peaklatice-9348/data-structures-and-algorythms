numbers = [1,2,67,8932,567,657,20,46329472835,7,5,5,5,5,5,5,3,32,56,45,1,2,1]
#linear search
flag = False
a = int(input('enter number:'))
for number in numbers:
    if number == a:
        flag = True
        break

if flag == True:
    print('yes')
    print('index:',numbers.index(a))
else:
    print('no')

#best case:first value(Ω(1)) Worst case:last value(O(n)) Average case:middle value(θ(n/2))

#binary search
numbers = [1,2,3,43,54,67,123,7564,34343,100000,4673285,676767676,999999999999]
a = int(input('enter number:'))
flag = False
first_pos = 0
last_pos = len(numbers)-1
while first_pos <= last_pos:
    mid_pos = (first_pos + last_pos)//2
    number = numbers[mid_pos]
    if number == a:
        flag=True
        break

    if number > a:
        last_pos = mid_pos-1
    
    if number < a:
        first_pos = mid_pos+1
        
if flag:
    print('Yes')
else:
    print('no')