#Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below. 
#Convert the extracted value to a floating point number and print it out.

text = "X-DSPAM-Confidence:    0.8475";
str1= text.find("0")
#print str1
str2= text.find("5")
#print str2
final= text[str1:(str2+1)] 
print float(final)


#################################  Another code ############################################
text = "X-DSPAM-Confidence:    0.8475";
str1= text.find("0")
#print str1
#str2= text.find("5")
#print str2
#final= text[str1:(str2+1)] 
final= text[str1:] 
print float(final)
