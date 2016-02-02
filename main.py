def index_markets(location):
    ziplist = {}
    townlist = {}
    m = open(location, 'r')
    m.readline()
    # splitting output into dictionary
    for line in m:
        inf = line.strip().split(',')
        ziplist[str(inf[7])] = [inf[1], inf[2], inf[3], inf[4], inf[6]]

    for line in m:
        inf = line.strip().split(',')
        townlist[str(inf[4])] += str(inf[7])

    return ziplist, townlist

markets, towns = index_markets(input("File Name?"))

# Welcome
print("Farmers Market Finder; Find your local fresh foods!")
print("Type quit at any time to exit the program.")
print(markets)
print(towns)