import urllib2

x = urllib2.urlopen('http://ec2-52-30-7-5.eu-west-1.compute.amazonaws.com:81/key')
keys = x.read();
keyset = keys.split(":")

for key in keyset:
  print ("> " + key)
