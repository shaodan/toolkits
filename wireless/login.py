#! /usr/bin/python
import sys
import httplib, urllib
import urllib2
# import md5

'''
def hex_md5(pass) :
    md5(pass)
    return 1
def get_vip :
    return 1
uname = "XX"
passwd = "XXXX"
vip = "20"
data = "action=login&username=XX&password=XXXX&vip=20"
params = urllib.urlencode({"action":"login", "username":uname,"password":passwd,"vip":vip})
headers = {"Accept":"text/html","User-Agent":"Mozila","Content-type":"application/x-www-form-urlencoded"}
# website = "166.111.8.120"
website = "wireless.tsinghua.edu.cn"
path = "cgi-bin/login"
conn = httplib.HTTPConnection(website)
conn.request("POST", path, params, headers)
r = conn.getresponse()
print r.status, r.reason
data = r.read()
print data
conn.close()
'''

# urllib2 provides extra functionality, namely the [urlopen()] function to specify headers(normally you'd have had to use httplib in the past)
# which is far more verbose. More importantly though, urllib2 provides the [Request] class, which allows for a more declarative approch to doing a request
# urllib2 and urllib both rely on httplib to implement http requests

uname = "xx"
passwd = "xxxx"
if len(sys.argv) > 1 :
  vip = sys.argv[1]
else:
  vip = "20"
print "vip" + vip
ap_mac = '04:c5:a4:08:dc:10'

site = 'http://wireless.tsinghua.edu.cn/'
auth_path = 'cgi-bin/cisco_auth'
url = site + auth_path
data = urllib.urlencode({"action":"login", "username":uname,"password":passwd,"vip":vip})

req = urllib2.Request(url, data)
req.add_header('User-Agent', 'Mozilla/5.0 (X11; Linux i686; rv:7.0.1 Gecko/20100101 Firefox/7.0.1')
req.add_header('Accept', 'text/html')
req.add_header('Content-Type', "application/x-www-form-urlencoded; charset=UTF-8")
req.add_header('Referer', site+'index_'+vip+'.html?ap_mac='+ap_mac)
res= urllib2.urlopen(req)
# print res.status, res.reason
#f = open('$HOME/log', 'w+')
#f.write(res.read())
print res.read().decode('gb2312')
#f.close()
res.close()
