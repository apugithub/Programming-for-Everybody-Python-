"""
10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below. Note that the autograder does not have support for the sorted() function.
"""
######  You can download the sample data at http://www.pythonlearn.com/code/mbox-short.txt
#output:
#04 3
#06 1
#07 1
#09 2
#10 3
#11 6
#14 1
#15 2
#16 4
#17 2
#18 1
#19 1

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

counts = dict()

for line in handle :
	line = line.rstrip()
	if line == "": continue
	words = line.split()
	if words[0] != "From" : continue
	time = words[5].split(":")
	counts[time[0]] = counts.get(time[0], 0) + 1

list = list()

for key,value in counts.items() :
	list.append((key,value))
list.sort()

for hour,count in list :
	print hour, count
	

######################################################## Another Code ###########################################

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
dic = dict()
for i in handle:
    if i.startswith("From") and len(i.split()) > 2:
        l = i.split()
        if not dic.has_key(l[5][:2]):
            dic[l[5][:2]] = 1
        else:
            dic[l[5][:2]] += 1
                
key = sorted(dic)
for i in key:
    print "%s %d" % (i,dic[i])
    
    
######################################################## Another Code ###########################################


def openFile():
    fname = raw_input("Enter file name: ")
    if len(fname) < 1 : fname = "mbox-short.txt"
    try:
        fh = open(fname, 'r')
    except:
        print "Error opening file", fname
        quit()
    return fh

def startsWith():
    sw = raw_input("Enter line prefix to consider: ")
    if len(sw) < 1 : sw = "From"
    return sw

def countTimes(lines,s):
    counts = dict()
    for line in lines:
        if line.startswith(s) and not line.startswith(s+':'):
            line = ((line.rstrip()).lstrip()).split()
	    str = line[5]
	    hour = str[0:str.find(":"):1]
            counts[hour] = counts.get(hour,0) + 1
    return counts

def sortTimes(d):
    lst = list()
    for key, val in d.items():
        lst.append((key,val))
    lst.sort()
    for val,key in lst:
        print val,key
    
fh = openFile()
sw = startsWith()
dictionary = countTimes(fh,sw)
t = sortTimes(dictionary)


	
