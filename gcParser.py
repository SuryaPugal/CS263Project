f = open("gcData.txt", "r")
numGenerations= {}
totalTime = 0.0
numCollections = 0
for x in f:
  if "gc" in x:
    if "s elapsed" in x:
        subsection = x[42:]
        decimalIndex = subsection.find('.')
        end = subsection.find('s')
        subsection = subsection[decimalIndex-1:end]
        totalTime += float(subsection)
    elif "gc: collecting generation" in x:
        numCollections += 1
        sub = x.find("ion")
        x = x[sub:]
        start = x.find(' ')
        num = x[start+1:x.find('.')]
        if num not in numGenerations:
            numGenerations[num] = 1


print("time = ", totalTime)
print("num collectios = ", numCollections)
print("num generations = ",len(numGenerations))
