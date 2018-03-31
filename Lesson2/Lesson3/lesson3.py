file = open('shop.txt', 'r', encoding = 'utf-8')
name = []

leastProduct = 99999

for line in file:

    listValues = line.split(',')
    
    if int(listValues[4]) < int(leastProduct):
        leastProduct = int(listValues[4])
        name = listValues

        

print(name[4])
print(name[1])
    

