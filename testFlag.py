from railfence import decrypt
import sys

cipher = "WECRLTEERDSOEEFEAOCAIVDEN"
for i in range(2,int(sys.argv[1])):
	print "key = %d"%i, decrypt(cipher,i,0);
