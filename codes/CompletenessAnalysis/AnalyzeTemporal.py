import cPickle as pickle

infile = open("/home/projects/ebird/BCR30/SubEBD303137-TruncHis.csv","r")

YearCom = {}
YearInc = {}
YearComCom = {}
YearComRar = {}
YearIncCom = {}
YearIncRar = {}
tt = 0
#outfile2 = open("/home/projects/ebird/BCR30/Complete-Size","w")
for line in infile:
	tt += 1
	if tt ==1: continue
	ss = line.split(",")
	# Year - Complete Count
	Year = int(ss[3])
	Complete = ss[2]
	common = int(ss[5])
	rare = int(ss[6])
	if Complete=="1":
		if Year in YearCom: YearCom[Year] += 1
		else: YearCom[Year] = 1
		if common>0:
			if Year in YearComCom: YearComCom[Year] += 1
			else: YearComCom[Year] = 1
		if rare>0:
			if Year in YearComRar: YearComRar[Year] += 1
			else: YearComRar[Year] = 1
	else:
		if Year in YearInc: YearInc[Year] += 1
		else: YearInc[Year] = 1
		if common>0:
			if Year in YearIncCom: YearIncCom[Year] += 1
			else: YearIncCom[Year] = 1
		if rare>0:
			if Year in YearIncRar: YearIncRar[Year] += 1
			else: YearIncRar[Year] = 1
outfile1 = open("/home/projects/ebird/BCR30/Year-Comp-Analysis-TruncHis.csv","w")
outfile1.write("Year,Com,Incomp,InRate\n")
for i in range(1,14):
	outfile1.write( str(i) + "," + str(YearCom[i]) + "," + str(YearInc[i]) + "," + str(float(YearInc[i])/(float(YearCom[i]) + float(YearInc[i]))) + "\n")

outfile3 = open("/home/projects/ebird/BCR30/Year-Comp-ComRar-Analysis-TruncHis.csv","w")
outfile3.write("Year,CompCommon,CompRare,IncompCommon,IncompRare\n")
for i in range(1,13):
	sumbase = float(YearCom[i] + YearInc[i])
	outfile3.write(str(i) + "," + str(float(YearComCom[i])/sumbase) + "," + str(float(YearComRar[i])/sumbase) + "," + str(float(YearIncCom[i])/sumbase) + "," + str(float(YearIncRar[i])/sumbase) + "\n" )
