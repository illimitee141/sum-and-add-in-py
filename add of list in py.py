def add_two(num1,num2): #perameter
    output = num1 + num2
    return output
 
 # for add two number

a = int(input('enter first number    '))
b = int(input('enter second number   '))

output = add_two(a,b)
print(output)


# count the items present in ls 
ls = [43,67,86,97,56,87]
def my_len(ls):
    count = 0
    for items in ls:
        count += 1
    return count 

# sum of total amount present in ls
def total_price(ls):
    total = 0
    
    for items in ls:
        total += items 
        
    return total
ls = [43,67,86,97,56,87]
print(total_price(ls))      



