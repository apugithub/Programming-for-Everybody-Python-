def computepay(h,r):
    if (h > 40) :
	    value = (((h - 40) * 1.5) + 40)  * r
    else:
	    value = h * r
    return value    

try:     
    hrs = raw_input("Enter Hours:")
    h = float(hrs)
    rate = raw_input("please input your rate:")
    r = float(rate)
    p = computepay(h,r)
    print p
except:
    print 'Error, please enter numeric value'
    
