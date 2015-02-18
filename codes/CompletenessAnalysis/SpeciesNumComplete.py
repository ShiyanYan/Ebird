import cPickle as pickle
infile = open("/home/projects/ebird/BCR30/SubEBD303137-TruncHis.csv","r")
tt = 0
SpecCom = {}
SpecTot = {}
for line in infile:
	tt += 1
	if tt==1: continue
	ss = line.split(",")
	Com = ss[2]
	SpecNum = int(ss[8])
	if SpecNum in SpecTot: SpecTot[SpecNum] += 1
	else: SpecTot[SpecNum] = 1
	if Com == "1":
		if SpecNum in SpecCom: SpecCom[SpecNum] += 1
		else: SpecCom[SpecNum] = 1
outfile = open("/home/projects/ebird/BCR30/SpecVComp.csv","w")
outfile.write("SpecNum,ComRate\n")
for key in sorted(SpecTot):
	if (key in SpecCom) and (SpecTot[key]>5):
		r = float(SpecCom[key]) / float(SpecTot[key])
		outfile.write(str(key) + "," + str(r) + "\n")
		print key,r
