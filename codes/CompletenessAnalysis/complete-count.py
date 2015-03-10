import sys
inp = "/home/projects/ebird/BCR30/EBD-NOBCR.txt"
inputfile = open(inp,'r')

tt = 0
checklisttot = 0
ar = 0
lastSampleId = ""
for line in inputfile:
    tt += 1
    if tt ==1:
        print line.split("\t")[37]
        continue
 #   if tt>100: break
    if tt % 10000000==0: print str(tt) + " Complete!"
    ss = line.split("\t")
    sampleID = ss[30]
    arV = ss[37]
    if sampleID != lastSampleId:
        checklisttot += 1
        if arV=="1":
            ar += 1
        lastSampleId = sampleID

print "Total CheckList Number = " + str(checklisttot)
print "Total Complete CheckList Number = " + str(ar)
