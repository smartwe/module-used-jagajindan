import hcskr
import os
std1 = os.environ['STD1'].split(",")
std2 = os.environ['STD2'].split(",")

hcskr.selfcheck(std1[0], std1[1], std1[2], std1[3], std1[4], std1[5])
hcskr.selfcheck(std2[0], std2[1], std2[2], std2[3], std2[4], std2[5])