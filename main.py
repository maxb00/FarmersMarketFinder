# setup for program, open files
markets = {}
m = open('E:/GitHub/FarmersMarketFinder/Libs/markets-test.csv', 'r')

# Next line only useful if there is a blank or irrelevant line at top of file. Mine has none.
# m.readline()

# splitting output into dictionary
for line in m:
    inf = line.strip().split(',')
    markets[inf[7]] = inf[1], inf[2], inf[3], inf[4], inf[6]
print(markets)

# search function
try:
    searchZip = int(input("What is your zip code?"))
except ValueError:
    print("Please enter a Zip Code.")
    exit()
#Printing search result
print("Data will be printed in the form of (Market Name, Website, street, city, County, State) when applicable")
print(markets[str(searchZip)])
