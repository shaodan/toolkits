#! /bin/bash
sudo ifconfig wlan0 down
sudo killall wpa_supplicant
sudo wpa_supplicant -B -c wpa_tsinghua.conf -i wlan0
sleep 2;
sudo ifconfig wlan0 up
sudo route del default
sudo dhclient3 -e IF_METRIC=100 -pf /var/run/dhclient.wlan0.pid -lf /var/lib/dhcp3/dhclient.wlan0.leases wlan0
#sudo route del default
sudo route add -net 166.111.0.0 netmask 255.255.0.0 gw 192.168.1.22
sudo route add -net 59.66.0.0 netmask 255.255.0.0 gw 192.168.1.22
#sudo route add 1.1.1.1 dev wlan0
#sudo route add 59.66.4.50 dev wlan0
sudo route add 166.111.8.120 dev wlan0
sudo route -A inet6 add ::/0 dev wlan0
./mytuwl.py
