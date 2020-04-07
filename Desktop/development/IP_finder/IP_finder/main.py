import tkinter as tk
import socket
import os
from tkinter import filedialog
from collections import Counter


root = tk.Tk()
root.withdraw()

filePath = filedialog.askopenfilename()

ipAdr = []

with open(filePath, 'r') as file:

    for line in file:

        pos1 = line.find('dstip')
        assert pos1 != -1
        pos1 += 7
        pos2 = line.find('" proto')
        assert pos2 != -1
        ip = line[pos1:pos2]
        ipAdr.append(ip)

cntIP = Counter(ipAdr)
IPlist = list(cntIP.items())

output = []

for i in range(len(IPlist)):

    name = socket.gethostbyaddr(IPlist[i][0])
    output.append((IPlist[i][0], IPlist[i][1] ,name[0]))


def takeSecond(elem):
    return elem[1]


output.sort(key=takeSecond, reverse=True)

dir_path = os.path.dirname(os.path.realpath(__file__))

outputDir = dir_path + 'output.txt'

with open(outputDir, 'w+') as file2:

    for i in range(len(output)):

        dis1 = 18 - len(str(output[i][0]))
        dis2 = 18 - len(str(output[i][1]))
        line = str(output[i][0]) + ' ' * dis1 + str(output[i][1]) + ' ' * dis2 + str(output[i][2]) + '\n'
        file2.writelines(line)