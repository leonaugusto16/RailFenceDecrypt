from railfence import decrypt 
import sys

cipher = "AaY--rpyfneJBeaaX0n-,ZZcs-uXeeSVJ-sh2tioaZ}slrg,-ciE-anfGt.-eCIyss-TzprttFliora{GcouhQIadctm0ltt-FYluuezTyorZ-"

for i in range(2,int(sys.argv[1])):
	print "Key = %d"%i,decrypt(cipher,i,0);
