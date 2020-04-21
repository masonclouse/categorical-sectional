# Creates the airport config file from a text list of airport identifiers.
# Put the file to be converted into the data folder and enter its name below.

# INPUT file name:
file = open('data/FILENAME.txt', 'r')

list = []
for line in file:
    list.append(str(line))

list = [w.replace('\n', '') for w in list]
count = 0

# OUTPUT file name:
output = open("data/airport_config_file.json", 'w')

output.write("{")
output.write("\n")
output.write("  \"ws2811\": [")
output.write("\n")

for line in list:
    output.write("    { \"")
    output.write(line)
    output.write("\": { \"neopixel\": ")
    output.write(str(count))
    output.write(" } }")
    if count < len(list) - 1:
        output.write(",")
    output.write("\n")
    count += 1

output.write("  ]")
output.write("\n")
output.write("}")
