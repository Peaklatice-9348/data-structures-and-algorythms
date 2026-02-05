def print_name(name,repeat):
    if repeat == 0:
        return 
    else:
        print(f'your name is {name}')
        print_name('yusuf',repeat-1)

def print_range(min_value,max_value):
    if min_value > max_value:
        return
    
    else:
        print(min_value)
        print_range(min_value+1,max_value)

def sum_range(s):
    if s == 0:
        return 0
    else:
        return s + sum_range(s-1)
    
def product_range(s):
    if s == 1:
        return 1
    else:
        return s * sum_range(s-1)

def dec_to_bin(num):
    if num == 0:
        return 0
    else:
        return dec_to_bin(num//2)*10 + num%2

print_name('yusuf',10)

print_range(1,10)

print(sum_range(5))

print(dec_to_bin(56746305632758642890578926458))