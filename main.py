from tabulate import tabulate
# table = [['Cij', ' ', ' ', 4, 3, 0, 0], ['John', 'Smith', 39],
#         ['Mary', 'Jane', 25], ['Jennifer', 'Doe', 28]]
import matplotlib.pyplot as plt
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
helpervariables = 0
nSurplus = 0
nSlack = 0
nArtificial = 0
identity = 2
print(tabulate(table))

while (start):
    txt = input()
    if txt == 'start':
        break

    txt = txt.split()
    txt2 = txt.copy()
    txt2.pop(-2)
    x1 = []
    y1 = []
    txt2 = [eval(i) for i in txt2]

    if txt2[1] == 0:
        plt.axvline(x=txt2[2], color='b', label='axvline - full height')
    else:
        if txt2[0] == 0:
            plt.axhline(y=txt2[2], color='r', linestyle='-')
        else:
            x1.append(float(txt2[2]/txt2[1]))
            y1.append(0)
            y1.append(float(txt2[2]/txt2[0]))
            x1.append(0)
            plt.plot(x1, y1)

    print(txt2)
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
            txt[0] = 0
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
            txt[0] = -999
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
            txt[0] = -999
            txt[1] = 'R'+str(nArtificial)
            for i in range(numconstraints):
                table[i+2].insert(-1, 0)
        helpervariables += 1

    table.append(txt)
    numconstraints += 1
    print(tabulate(table))
print(x1)
print(y1)
plt.show()
table[1].append("Obj.F")
table[1].append("Ratio")
numvariables += helpervariables
txt = []
txt2 = []
txt2.insert(0, ' ')
txt2.insert(1, 'Cj - Zj')
txt.insert(0, ' ')
txt.insert(1, 'Zj')
for i in range(numvariables+1):
    txt.insert(i+2, ' ')
    txt2.insert(i+2, ' ')
table.append(txt)
table.append(txt2)
# print(table[1][2])
print("numvariables: ", numvariables)
print("numconstraints: ", numconstraints)
evaluate = True
while evaluate:
    row = 0
    col = 0
    max = -9999999
    min = 999999
    evaluate = False
    for k in range(numconstraints):
        table[k+2].append(' ')
    for i in range(numvariables+1):
        z = 0
        for k in range(numconstraints):
            print(table[k+2][0], "*", table[k+2][i+2])
            z += float(table[k+2][0])*float(table[k+2][i+2])
        table[numconstraints+2][i+2] = z
        print("= ", z)
        if i < numvariables:
            table[numconstraints+3][i+2] = float(table[0][i+2]) - z
            cz = table[numconstraints+3][i+2]
            if cz > max:
                max = cz
                col = i+2
            if cz > 0:
                evaluate = True
    for k in range(numconstraints):
        if float(table[k+2][col]) == 0:
            continue
        table[k+2][numvariables+3] = float(table[k+2]
                                           [numvariables+2]) / float(table[k+2][col])
        ratio = table[k+2][numvariables+3]
        if ratio < min and ratio >= 0:
            min = ratio
            row = k+2
    table[row][0] = table[0][col]
    table[row][1] = table[1][col]
    print(tabulate(table))
    print("col: ", col, "max: ", max)
    print("row: ", row, "min: ", min)
    pivotElemnt = float(table[row][col])
    for i in range(numvariables+1):
        table[row][i+2] = float(table[row][i+2])/pivotElemnt
    for k in range(numconstraints):
        if k+2 == row:
            continue
        coff = float(table[k+2][col])*-1
        for i in range(numvariables+1):
           # print("coff is :", coff)
           # print("table[k+2][i+2]", table[k+2][i+2],
           #       "table[row][i+2]*coff", table[row][i+2]*coff)
            table[k+2][i+2] = float(table[k+2][i+2]) + \
                (float(table[row][i+2])*coff)
    print(tabulate(table))
    text = input()
# print(numvariables)

# txt = input()

# x = []
# txt = txt.split()
# txt.insert(0, ' ')
# txt.insert(0, ' ')

# x.append(txt)

# print(x)
# print(tabulate(x))
