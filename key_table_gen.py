#!/usr/bin/python

import os, sys

for i in sorted(os.listdir('/home/ec2-user/PublicKeys')):
    if i.endswith(".pub.txt"):
        fo = open("pk.txt", "a")
        b = i.replace("."," ")
        z = b.split(" ")[0:2]
        q = " ".join(z)
        fo.write('<p><a href="PublicKeys/'+i+' "class="kinfo">'+q+'</a></p>\n')
        fo.close()

for i in sorted(os.listdir('/home/ec2-user/Fingerprints')):
    if i.endswith(".fpr.txt"):
        fo = open("fp.txt", "a")
        c = i.replace("."," ")
        e = c.split(" ")[0:2]
        h = " ".join(e)
        fo.write('<p><a href="Fingerprints/'+i+' "class="kinfo">'+h+'</a></p>\n')
        fo.close()
    else:
        continue

os.system("sort -k 3 pk.txt > pka.txt")
os.system("sort -k 3 fp.txt > fpa.txt")
os.system("mv pka.txt pk.txt")
os.system("mv fpa.txt fp.txt")

inputfiles = ['pk.txt']
with open("pkb.txt","w") as outfile:
  for fname in inputfiles:
    with open(fname) as infile:
      for index, line in enumerate(infile):
        x = line.split(" ")
        if (len(x) > 2):
          q  = x[2]
          r = q[:1]
          outfile.write('<H2><BOLD>'+r+'</BOLD></H2>\n'+line+'\n')
        else:
          print('Something when wrong with line %s: %s' % (index, line))
outfile.close() 
infile.close()

os.system("cat pkb.txt | awk '!x[$0]++'>pkc.txt")
os.system("mv pkc.txt pk.txt") 

inputfiles = ['fp.txt']
with open("fpb.txt","w") as outfile:
  for fname in inputfiles:
    with open(fname) as infile:
      for index, line in enumerate(infile):
        x = line.split(" ")
        if (len(x) > 2):
          q  = x[2]
          r = q[:1]
          outfile.write('<H2><BOLD>'+r+'</BOLD></H2>\n'+line+'\n')
        else:
          print('Something when wrong with line %s: %s' % (index, line))
outfile.close()
infile.close()

os.system("cat fpb.txt | awk '!x[$0]++'>fpc.txt")
os.system("mv fpc.txt fp.txt") 

filenames = ['header.txt','pk.txt','middle.txt','fp.txt','footer.txt']
with open('index.html','w') as outfile:
  for fname in filenames:
    with open(fname) as infile:
      for line in infile:
        outfile.write(line)

os.remove('pk.txt')
os.remove('fp.txt')
os.remove('pkb.txt')
os.remove('fpb.txt')
