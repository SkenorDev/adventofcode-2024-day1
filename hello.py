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
for i in range(len(list1)):
    if list1[i]<list2[i]:
        total+=list2[i]-list1[i]
    if list1[i]>list2[i]:
            total+=list1[i]-list2[i]
print(total)