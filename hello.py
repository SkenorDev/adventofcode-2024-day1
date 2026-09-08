with open("input.txt", "r") as file:
    lines = file.read().splitlines()
list1 = []
list2 = []
total: int = 0
for line in lines:
    first, second = line.split()
    list1.append(int(first))
    list2.append(int(second))   

list1.sort(reverse=False)
list2.sort(reverse=False)
for num in list1:
    mult: int =0
    for num2 in list2:
        if num2 == num:
            mult+=1
    total+= num*mult
print(total)