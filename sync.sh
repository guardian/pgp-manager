#!/bin/sh

aws s3 cp index.html s3://pgp.theguardian.com/index.html 
cd /home/ec2-user/PublicKeys
aws s3 sync . s3://pgp.theguardian.com/PublicKeys --exclude "Pending/*"
cd /home/ec2-user/Fingerprints
aws s3 sync . s3://pgp.theguardian.com/Fingerprints --exclude "Pending/*"
