# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)

avg = 0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    try:
    	avg += float(line[20:])
    	count += 1
    except Exception, e:
    	print "Provide number"
    	exit()

print "Average spam confidence:", avg / count    



################################################# Another Code#############################################

# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
l = []
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    ll = line.split()
    for i in ll:
        try:
            u = float(i)
            l.append(u)
        except:
            pass
print "Average spam confidence:",sum(l)/len(l)


######################################################################## Aonther Code#######################################################


# Use the file name mbox-short.txt as the file name

def openfile():
    fname = raw_input("Enter file name: ")
    try:
        fh = open(fname, 'r')
    except:
        print "Error opening file", fname
        quit()
    return fh

def computeAverage(fh):
    average = None
    count = 0
    for line in fh:
        if line.startswith("X-DSPAM-Confidence:") :
            count = count + 1
            columnPos = line.find(":")
            number = line[columnPos+1::1]
            snumber = number.lstrip()
            if average is None:
                average = 0
            snumber = float(snumber.rstrip())
            average = ( (average * ((count -1)) + snumber) / count )
            #print "new average", average
    return average

fh = openfile()
print "Average spam confidence:", computeAverage(fh)

