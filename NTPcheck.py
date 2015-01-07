#!/usr/bin/python
#Script written by Quam Sodji
#Copyright 2014 Quam Sodji
#Script checks for NTP vulnerability patch via casper

import subprocess
import platform

def check_ntp():
     check = subprocess.check_output(["what", "/usr/sbin/ntpd"])  
     o = check.strip()
     p = o.split()
     t = p[2]
     c = t.split(":")
     result = c[1]
     return result

applied_patch = ["ntp-77.1.1","ntp-88.1.1","ntp-92.5.1"]
#Find the OS version the client is running

osvers = platform.mac_ver()[0]

#The NTP fix is only available for the following OSX versions
Needed_vers = ["10.10.2", "10.10.1", "10.9.5", "10.8.5"]

if not osvers in Needed_vers:
       Status = "No:OS is %s"%osvers
else:       
     result = check_ntp()

     if result in applied_patch:
        Status =  "Yes"
     else:
          apply_update = subprocess.check_output(["softwareupdate", "--install", "OS X NTP Security Update-1.0"])
          value_one = check_ntp()
          if value_one in applied_patch:
             Status = "Yes"
          else:
               Status = apply_update

    
print "<result>%s</result>" %Status
