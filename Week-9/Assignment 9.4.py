"""
9.4 Write a program to read through the mbox-short.txt and figure out who has the most commits. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the senders mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
"""

#output
#cwen@iupui.edu 5

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
f = open(name)

dic = {}
maxvalue = 0
name = ""
l = [i.split()[1] for i in f.readlines() 
            if i.startswith("From") and i.find("@")>0 and len(i.split()) > 2]
for i in l:
    if not dic.has_key(i):
        dic[i] = 1
    else:
        dic[i] +=1
        if maxvalue < dic[i]:
            maxvalue = dic[i]
            name = i

print name,maxvalue

##############################################################Another Code############################################################


name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

counts = dict()

for line in handle :
	line = line.rstrip()
	if line == "": continue
	words = line.split()
	if words[0] != "From" : continue
	counts[words[1]] = counts.get(words[1], 0) + 1

maxCount = None
maxEmail = None
for email,count in counts.items() :
	if maxCount < count :
		maxCount = count
		maxEmail = email

print maxEmail, maxCount

########################################## Another Code #################################################################

#9.4 Write a program to read through the mbox-short.txt and figure out who has the most commits. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the senders mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

#You can download the sample data at http://www.pythonlearn.com/code/mbox-short.txt

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

def doCount(lines,s):
    counts = dict()
    for line in lines:
        if line.startswith(s) and not line.startswith(s+':'):
            line = ((line.rstrip()).lstrip()).split()
	    counts[line[1]] = counts.get(line[1],0) + 1
    return counts

def max(dictionary):
    max = None 
    highest = None
    #print dictionary
    for key in dictionary:
        if max < dictionary[key]:
	    max = dictionary[key]
	    #print "new max is", max
	    highest = key
    return highest

fh = openFile()
sw = startsWith()

dictionary = doCount(fh,sw)
key = max(dictionary)
print key, dictionary[key] 

