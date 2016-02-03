def index_markets(location):
    ziplist = {}
    townlist = {}
    m = open(location, 'r')
    m.readline()
    # Splitting output into dictionary
    for entry in m:
        info = entry.strip().split(',')
        townlist[str(info[4])] = []
        townlist[str(info[4])].append(str(info[7]))
        # Could not read through file twice, had to condense.
        ziplist[str(info[7])] = []
        ziplist[str(info[7])].append((info[1], info[2], info[3], info[4], info[6]))
    return ziplist, townlist

markets, towns = index_markets(input("File Name?"))

# Welcome
print("Farmers Market Finder; Find your local fresh foods!")
print("Type quit at any time to exit the program.")
print(markets)
print(towns)
Running = True
while Running:
    query = input("What is the name of your zip code or town?")
    try:
        # Check for integer status, is it a zip, or not?
        query = int(query)

        # Change back to string for usability
        query = str(query)

        # Search by int
        for i in markets[query]:
            print(markets[query][i])
    except ValueError:
        # Search by town
        quit()
