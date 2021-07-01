f = open("show_version.txt")
i = 0
while i <= 5:
    line = f.readline()
    line = line.strip()
    print(line)
    i = i+1
