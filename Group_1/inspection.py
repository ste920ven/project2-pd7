inspections = []

for line in open("WebExtract.txt", "r").readlines():
    inspections.append(line)

###Test restaurant search###
#x = 0 
#for line in inspections:
 #   if (line.find("KITCHENETTE") != -1 and line.find("10007") != -1):
  #      ind = inspections.index(line)
   #     tmp = inspections[ind].split(",")
        #trying to get rid of the rating-less restaurants
    #    if (tmp[12][1] != '"'):
     #       print tmp[1].strip('"'), tmp[12][1]
      #      break
        #print a[ind].split(",")[12][1]
    #x = x + 1

def getGradeFor(restname):
    global inspections
    for line in inspections:
        #if that restaurant appears in the array        
        if (line.find(str(restname).upper()) != -1):
            #tell me the index of the restaurant
            restIndex = inspections.index(line)
            #make that line into a list
            details = inspections[restIndex].split(",")
            #if there is a sanitation grade return it, otherwise keep parsing
            if (details[12][1] != '"'):
                return details[12][1]

#print getGradeFor("Baluchi")
