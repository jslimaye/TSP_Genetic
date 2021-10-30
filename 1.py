d1 = {"jalaj":80,"jay":75}

l = ["jalaj","jay"]

l2 = sorted(l, key=d1.get)

d1["jack"] = 10

#d1.update({l:15}) 
 
l3 = [(2,"j"),(3,"p"),(4,"p"),(1,"d")]
#print(sorted(l3))

my_file = open("cities.txt", "r")
content = my_file. read()
print(content)
content_list = content. split(",")
print(content_list)

with open("cost-matrix.txt","r") as file:
    Cost_Matrix = []
    for line in file:
        temp = line.split(",")
        for i in range(len(temp)):
            temp[i] = int(temp[i])
        Cost_Matrix.append(temp)

print(Cost_Matrix)