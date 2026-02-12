numbers = [1,2,67,8932,567,657,20,46329472835,7,5,5,5,5,5,5,3,32,56,45,1,2,1]

a = int(input('enter number:'))
for number in numbers:
    if number == a:
        b = numbers.index(a)
        a = True
        break
if a == True:
    print('yes')
else:
    print('no')
print('index:',b)