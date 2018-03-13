#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
  Copyright by shaodan.cn
  2011.10.20 - 2012.12.12
  shaodan.cn@gmail.com

  Module for Accessing Tsinghua Wireless Network
'''

import sys, urllib, urllib2, hashlib, re, getpass
import ConfigParser

# Module for Wireless Parameters Fetching
def get_ap_mac() :
  '''test if ap_mac can be used for login post'''
  html = do_get('http://1.1.1.1/login.html').decode('gb2312')
  mc = re.search('ap_mac=(\S{17})', html)
  return mc.group(1)

def get_vip() :
  '''test if we can calculate vip from net-address'''
  # return '20'
  html = do_get('http://1.1.1.1/login.html').decode('gb2312')
  mc = re.search('index_(\d+)\.html', html)
  return mc.group(1)
  '''it seems that between vip and real ip there exists an mapping that the first 4 bit of the 3rd cluster of real ip plus 6 equals to vip
  i.e. 224 = (11100000)2 -> 1110(14) +6 -> 20'''

# Module for Http Request
# urllib2 provides extra functionality, namely the [urlopen()] function to specify headers(normally you'd have had to use httplib in the past)
# which is far more verbose. More importantly though, urllib2 provides the [Request] class, which allows for a more declarative approch to doing a request
# urllib2 and urllib both rely on httplib to implement http requests
def do_get(url) :
  res = do_http(url, 'GET')
  return res

def do_post(url, data) :
  post_data = urllib.urlencode(data)
  code = do_http(url, 'POST', post_data)
  return code

def do_http(url, method='', data='', referer=''):
  if method == 'GET':
    req = urllib2.Request(url)
  elif method == 'POST':
    req = urllib2.Request(url, data)
    req.add_header('User-Agent', 'Mozilla/5.0 (X11; Linux i686; rv:7.0.1 Gecko/20100101 Firefox/7.0.1')
    req.add_header('Accept', 'text/html')
    req.add_header('Content-Type', "application/x-www-form-urlencoded; charset=UTF-8")
    # req.add_header('Referer', referer)
  try :
    res = urllib2.urlopen(req)
    ret = res.read()
    res.close()
  except :
    ret = '-1'
    print '!!%s request to %s exception\n' % method, url
  finally :
    return ret

# Module for Log in/out Action
def encrypt(passwd) :
  '''encrypt password with md5'''
  return hashlib.md5(passwd).hexdigest()

def return_code(code) :
#  result = {
#    '0' : lambda : print ''
#    '1' : lambda : print ''
#  }[code]()
  print 'return code %s' % code

def login() :
  # Config file instance
  config_file = "mytuwl.cfg"
  config = ConfigParser.SafeConfigParser()
  update_config = False
  try :
    config.read(config_file)
    if config.has_section("User"):
      if config.has_option("User", "name") :
        uname = config.get('User', 'name')
      if config.has_option('User', 'passwd') :
        passwd = config.get('User', 'passwd')
    else :
      config.add_section("User")
  except :
    update_config = False
    print '!!failed to read config file\n'

  if not "uname" in locals().keys() :
    uname = raw_input("user:")
    update_config = True
  if not "passwd" in locals().keys() :
    passwd = encrypt(getpass.getpass('password: '))
    update_config = True

  vip = get_vip()
  # ap_mac = get_ap_mac()

  site = 'http://wireless.tsinghua.edu.cn/'
  auth_path = 'cgi-bin/cisco_auth'
  url = site+auth_path
  data = {"action":"login", "username":uname, "password":passwd, "vip":vip}

  code = do_post(url, data)
  return_code(code)

  if code == '0' and update_config :
    try :
      config.set("User", "name", uname)
      config.set("User", "passwd", passwd)
      config.write(open(config_file, 'w'))
    except :
      print "!!failed to write config file!!"

def logout() :
  site = 'http://wireless.tsinghua.edu.cn/'
  auth_path = 'cgi-bin/cisco_auth'
  url = site+auth_path
  data = {'action':'logout', 'vip': get_vip()}
  code = do_post(url, data)
  return_code(code)

# Module for Record Ap-Mac & Vip list to guess mapping rule
# or IP & Vip Mapping-rule

# Main Module
if __name__ == "__main__" :
  if len(sys.argv) < 2 :
    login()
  else :
    logout()
