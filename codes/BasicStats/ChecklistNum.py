inputfile = open("/home/projects/ebird/BCR30/EBD-BCR30.txt","r")
outfile = open("/home/projects/ebird/BCR30/CheckListNum.csv","w")
outfile.write("ObserID,Count\n")
dic = {}
tt = 0
for line in inputfile:
	ss = line.split("\t")
	tt += 1
	if tt % 1000000 == 0: print tt,"Complete"
	if tt==1:
		width = len(ss)
		for i in range(0,width):
			if ss[i] == "OBSERVER ID": ObserIndex = i
		continue
	UserID = ss[ObserIndex]
	if UserID in dic:
		dic[UserID] += 1
	else:
		dic[UserID] = 1

for UserID in dic:
	outfile.write(UserID + "," + str(dic[UserID]) + "\n")
