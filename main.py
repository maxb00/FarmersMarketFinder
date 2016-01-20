markets = {}
m = open('C:/Users/barlowm/IdeaProjects/FarmersMArketFinder/Libs/markets-test.csv', 'r')
m.readline()
for line in m:
    inf = line.strip().split(',')
    markets[inf[7]] = inf[0], inf[1], inf[2], inf[3], inf[4], inf[5], inf[6]
print(markets)
try:
    searchZip = int(input("What is your zip code?"))
except ValueError:
    print("Please enter a Zip Code.")
    exit()
