def index_markets(location):
    ziplist = {}
    townlist = {}
    m = open(location, 'r')
    m.readline()
    # Splitting output into dictionary
    for entry in m:
        info = entry.strip().split(',')
        # Checking to make sure a town is present
        if str(info[4]) == '':
            break
        # Checking if entry already exists, then adding.
        if str(info[4]) not in townlist:
            townlist[str(info[4])] = []
            townlist[str(info[4])].append(str(info[7]))
        else:
            townlist[str(info[4])].append(str(info[7]))
        # Checking if zip entry exists, then adding all market info.
        if str(info[7]) not in ziplist:
            ziplist[str(info[7])] = []
            ziplist[str(info[7])].append([info[1], info[2], info[3], info[4], info[6], info[7]])
        else:
            ziplist[str(info[7])].append([info[1], info[2], info[3], info[4], info[6], info[7]])

    return ziplist, townlist
# Booleans for later loops
Running = True
FindFile = True

# Getting user input on market list
while FindFile:
    try:
        markets, towns = index_markets(input("File Name?"))
        FindFile = False
    except FileNotFoundError:
        print("File not found, or it is not in the right directory.")

# Debugging steps, not needed.

# print(markets)
# print(towns)

# Welcome
print("Farmers Market Finder; Find your local fresh foods!")
print("Type quit at any time to exit the program.")
# Forever run loop.
while Running:
    query = str(input("What is the name of your zip code or town?"))
    # Does the user want to quit?
    if query == "quit":
        Running = False
    # Was the entry blank?
    elif query == "":
        print("No Entry.")
    # Main search function
    else:
        # Zip searching
        try:
            # Check for integer status, is it a zip, or not?
            query = int(query)

            # Change back to string for usability
            query = str(query)

            # Search by int
            try:
                for i in markets[query]:
                    print("Market Name:", i[0])
                    print("Market Website:", i[1])
                    print("Location:", i[2], i[3], i[4], i[5])
                    print("-")
            # Handling a Zip not found or incorrect
            except KeyError:
                print("Zip Code not found. Maybe your local market is not listed?")
        # Town searching, if integer conversion failed.
        except ValueError:
            # Search by town
            try:
                for i in towns[query]:
                    print("Market Name:", markets[i][0][0])
                    print("Market Website:", markets[i][0][1])
                    print("Location:", markets[i][0][2], markets[i][0][3], markets[i][0][4], markets[i][0][5])
                    print("-")
            # Handling a town that is not there or is spelled incorrectly.
            except KeyError:
                print("Town could not be found. Maybe your local market is not listed?")
