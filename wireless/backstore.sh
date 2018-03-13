#! /bin/bash
sudo route del default
sudo route add default gw 192.168.1.22 metric 100
sudo route del -net 59.66.0.0 netmask 255.255.0.0
sudo route del -net 166.111.0.0 netmask 255.255.0.0
sudo route del 166.111.8.120
