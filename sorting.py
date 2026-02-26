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
print(numbers2)

    
