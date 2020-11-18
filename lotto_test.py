import csv
num_list = []
for i in range(0, 49):
    i += 1
    num_list.append(i)
neue = []

for i in range(0, 49):
    for j in range(0, 49):
        for k in range(0, 49):
            for x in range(0, 49):
                for y in range(0, 49):
                    for z in range(0, 49):
                        if(i != j and j != k and k != i and i != x and j != x and k != x and i != y and j !=y and k != y and x != y and z != y and z != j and z !=i and z != k and z != x):
                            print("{},{},{},{},{},{}".format(
                                num_list[i], num_list[j], num_list[k], num_list[x], num_list[y], num_list[z]))
                            asd = [num_list[i], num_list[j], num_list[k], num_list[x], num_list[y], num_list[z]]
                            neue.append(asd)
                            with open('Lotto_Kombis.csv', 'w+', newline="") as csvfile:
                                writer = csv.writer(csvfile)
                                for list in neue:
                                    writer.writerow(list)
