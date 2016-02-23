import os
import datetime

def ToTimedTxt(ifilename):
	splitted = ifilename.rsplit(os.extsep, 1)
	output = open("".join([splitted[0],"2", ".",splitted[1]]), 'w')
	with open(ifilename, 'r') as f:
		freq = float(f.readline().split("}")[2])
		for line in open(ifilename):
			spline = line.split("}", 2)
			output.write("".join([str(datetime.timedelta(microseconds=round(float(spline[0][1:])*1000000/freq)))[:-2],":",spline[2]]))
			
def ToSrt(ifilename):
	subcounter = 1
	splitted = ifilename.rsplit(os.extsep, 1)
	output = open("".join([splitted[0],"2", ".","srt"]), 'w')
	with open(ifilename, 'r') as f:
		freq = float(f.readline().split("}")[2])
		for line in open(ifilename):
			spline = line.split("}", 2)
			output.write("%d\n" % subcounter)
			output.write("".join([str(datetime.timedelta(microseconds=round(float(spline[0][1:])*1000000/freq)))," --> ", str(datetime.timedelta(microseconds=round(float(spline[1][1:])*1000000/freq))), "\n"]))
			output.write(spline[2]+"\n")
			subcounter = subcounter+1

# if __name__ == "__main__":
s = raw_input("Give file:")
ToTimedTxt(s)
ToSrt(s)