#!/usr/bin/python
# Written by Dave Boxall
# Version 1.1 
# Aug 13th 2015
# PGP Key Directory maintenance script

import os

for i in sorted(os.listdir('/home/ec2-user/PublicKeys')):
    if i.endswith(".pub.txt"): 
        fo = open("pk.txt", "a")
        b = i.replace("."," ")
        z = b.split(" ")[0:2]
        q = " ".join(z)
        fo.write('<a href="PublicKeys/'+i+' "class="kinfo">'+q+'</a>\n')
        fo.close()

for i in sorted(os.listdir('/home/ec2-user/Fingerprints')):
    if i.endswith(".fpr.txt"):
        fo = open("fp.txt", "a")
        c = i.replace("."," ")
        e = c.split(" ")[0:2]
        h = " ".join(e)
        fo.write('<a href="Fingerprints/'+i+' "class="kinfo">'+h+'</a>\n')
        fo.close()
    else:
        continue

os.system("sort -k 3 pk.txt > pka.txt")
os.system("sort -k 3 fp.txt > fpa.txt")
os.system("mv pka.txt pk.txt")
os.system("mv fpa.txt fp.txt")

filenames = ['header.txt','pk.txt','middle.txt','fp.txt','footer.txt']
with open('index.html','w') as outfile:
  for fname in filenames:
    with open(fname) as infile:
      for line in infile:
        outfile.write(line)

os.remove('/home/ec2-user/pk.txt')
os.remove('/home/ec2-user/fp.txt')

