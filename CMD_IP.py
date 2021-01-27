# Hari Narayanan PSG College of Technology '24

import re, time
from subprocess import PIPE, run
from pythonping import ping

# Function to feed commands to shell
def out(command):
    result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
    return result.stdout

# Creating a list of CMD Output and removing empty Strings
CMDout = out("ipconfig").split("\n")
CMDout = [x for x in CMDout if x]

# RegEx Patterm
pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')

# Accumulator List
IPList = []

# Using RegEx to store values in the Accumulator
for line in CMDout:
    IPAppend = pattern.search(line)
    if len(str(IPAppend)) > 10:
        IPList.append(str(IPAppend).split("match='", 1)[1][:-2])

# Displaying IPs to User
for i in IPList: print(i)
uPingChoice = False

# Asking if the user wants a Ping Test

while(1):
    uIn = input("Ping Test? (y/n)\n").lower()
    if uIn == 'y':
        uPingChoice = True
        break
    elif uIn == 'n':
        break
    else:
        print('Please enter a valid choice.\n')

# Ping Function

if uPingChoice:
    for IP in IPList:
        check = True
        t = 0
        print("\n\nNow pinging " + IP + "\n\n")
        while(t <= 5):
            try:
                print(ping(IP, verbose = True, timeout = 2.5))
            except:
                print("Unable to ping " + IP + "\n")
            time.sleep(1.5)
            t += 1.5