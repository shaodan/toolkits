#! /usr/bin/python
import httplib, urllib
import urllib2

vip = "20"

site = 'http://wireless.tsinghua.edu.cn/'
auth_path = 'cgi-bin/cisco_auth'
url = site + auth_path
data = urllib.urlencode({"action":"logout", "vip":vip})

req = urllib2.Request(url, data)
req.add_header('User-Agent', 'Mozilla/5.0 (X11; Linux i686; rv:7.0.1 Gecko/20100101 Firefox/7.0.1')
req.add_header('Content-Type', "application/x-www-form-urlencoded")
res= urllib2.urlopen(req)
print res.read().decode('gb2312')
res.close()
