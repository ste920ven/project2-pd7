a = []

for line in open("WebExtract.txt", "r").readlines():
    a.append(line)

#x = 0 
for line in a:
    if (line.find("KITCHENETTE") != -1):
        ind = a.index(line)
        tmp = a[ind].split(",")
        #trying to get rid of the rating-less restaurants
        if (tmp[12][1] != '"'):
            print tmp[1].strip('"'), tmp[12][1]
        #print a[ind].split(",")[12][1]
    #x = x + 1
