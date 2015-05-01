#!/usr/bin/python
# Written by Dave Boxall
# PGP Key Directory maintenance script

import os


for i in sorted(os.listdir('/home/ec2-user/PublicKeys')):
# for i in os.listdir(os.getcwd()):
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

filenames = ['header.txt','pk.txt','middle.txt','fp.txt','footer.txt']
with open('index.html','w') as outfile:
  for fname in filenames:
    with open(fname) as infile:
      for line in infile:
        outfile.write(line)

os.remove('/home/ec2-user/pk.txt')
os.remove('/home/ec2-user/fp.txt')

