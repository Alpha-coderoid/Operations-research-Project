from tabulate import tabulate
# table = [['Cij', ' ', ' ', 4, 3, 0, 0], ['John', 'Smith', 39],
#         ['Mary', 'Jane', 25], ['Jennifer', 'Doe', 28]]

table = []
start = True
text = []
obj = input()
obj = obj.split()
numvariables = len(obj)
for i in range(numvariables):
    text.insert(0, "X"+str(i+1))
text.insert(0, 'Basics')
text.insert(0, 'CB')
obj.insert(0, ' ')
obj.insert(0, ' ')
table.append(obj)
table.append(text)
numconstraints = 0
print(tabulate(table))
helpervariables = 0
nSurplus = 0
nSlack = 0
nArtificial = 0
identity = 2
while (start):
    txt = input()
    if txt == 'start':
        break

    txt = txt.split()
    txt.insert(0, ' ')
    txt.insert(0, ' ')
    if (txt[-2] == '<=' or txt[-2] == '>=' or txt[-2] == '='):
        for i in range(helpervariables):
            txt.insert(-2, 0)
        if (txt[-2] == '<='):
            txt.insert(-1, 1)
            nSlack += 1
            txt.pop(-3)
            table[0].append(0)
            table[1].append('S'+str(nSlack))
            txt[1] = 'S'+str(nSlack)
            identity += 1
            for i in range(numconstraints):
                table[i+2].insert(-1, 0)
        if (txt[-2] == '>='):
            txt.insert(-1, 1)
            txt.insert(-1, -1)
            nArtificial += 1
            nSurplus += 1
            txt.pop(-4)
            table[0].append(-999)
            table[0].append(0)
            table[1].append('R'+str(nArtificial))
            table[1].append('Su'+str(nSurplus))
            txt[1] = 'R'+str(nArtificial)
            for i in range(numconstraints):
                table[i+2].insert(-1, 0)
                table[i+2].insert(-1, 0)
            helpervariables += 1
        if (txt[-2] == '='):
            txt.insert(-1, 1)
            nArtificial += 1
            txt.pop(-3)
            table[0].append(-999)
            table[1].append('R'+str(nArtificial))
            txt[1] = 'R'+str(nArtificial)
            for i in range(numconstraints):
                table[i+2].insert(-1, 0)
        helpervariables += 1

    table.append(txt)
    numconstraints += 1
    print(tabulate(table))


# txt = input()

# x = []
# txt = txt.split()
# txt.insert(0, ' ')
# txt.insert(0, ' ')

# x.append(txt)


# print(x)
# print(tabulate(x))
