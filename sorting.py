numbers = [1,4321,5431254,345,235,342525,876,8,21,4,8,7879,65,552,4,37,769,98675,54,32,2,5,6,73,234,34,5,54,45,34,56,567,456,2,435,54,6754,6,345,436]
#selection sort

j=0
for k in range(len(numbers)-1):
    s = numbers[k]
    index=k
    for i in range(j,len(numbers)):
        if numbers[i] < s:
            s = numbers[i]
            index = i
    j+=1
    temp = numbers[k]
    numbers[k]=s
    numbers[index]=temp
    print(numbers)

#bubble sort
numbers2 = [4321,5431254,345,235,342525,876,8,21,4,8,7879,65,552,4,37,769,98675,54,32,2,5,6,73,234,34,5,1,54,45,34,56,567,456,2,435,54,6754,6,345,436]
print('')
for i in range(len(numbers2)-1):
    for j in range(len(numbers2)-i-1):
        num1 = numbers2[j]
        num2 = numbers2[j+1]
        if num1 > num2:
           numbers2[j] = num2
           numbers2[j+1] = num1
    print(numbers2)

#insertion sort
numbers3 = [4321,5431254,345,235,342525,876,8,21,4,8,7879,65,552,4,37,769,98675,54,32,2,5,6,73,234,34,5,1,54,45,34,56,567,456,2,435,54,6754,6,345,436]
print('')
for i in range(1,len(numbers3)):
    j = i - 1
    key = numbers3[1]
    while j >= 0 and key < numbers3[j]:

        numbers3[j+1] = numbers[j]
        j = j-1
    numbers3[j+1] = key
    print(numbers3)

#merge sort
list = [4321,5431254,345,235,342525,876,8,21,4,8,7879,65,552,4,37,769,98675,54,32,2,5,6,73,234,34,5,1,54,45,34,56,567,456,2,435,54,6754,6,345,436]
print('')
def mergesort(list,start,end):
    if start < end:
        midpoint = (start+end)//2
        mergesort(list,start,midpoint)
        mergesort(list,midpoint+1,end)
        merge(list,start,midpoint,end)

def merge(list,start,midpoint,end):
    list2 = []
    start1 = start
    start2 = midpoint+1
    while start1 <= midpoint and start2 <= end:
        number1 = list[start1]
        number2 = list[start2]
        if number1 < number2:
            list2.append(number1)
            start1 += 1
        else:
            list2.append(number2)
            start2 += 1
    while start2 <= end:
        list2.append(list[start2])
        start2 += 1
    while start1 <= midpoint:
        list2.append(list[start1])
        start1 += 1
    for i in range(len(list2)):
        list[start] = list2[i]
        start += 1


mergesort(list,0,len(list)-1)
print(list)
