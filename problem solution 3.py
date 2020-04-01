l = eval(input('Enter a list : '))
s = eval(input('Enter the Query String : '))
lst = []
for i in l:
    if i.startswith(s)==True:
        lst.append(i)
print(lst)
