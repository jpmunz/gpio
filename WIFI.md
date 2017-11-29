### Auto connect to Wi-Fi

https://askubuntu.com/questions/412325/automatically-connect-to-a-wireless-network-using-cli/412394

Edit /etc/network/interfaces

```
auto lo
iface lo inet loopback

auto wlan0
iface wlan0 inet static
address 192.168.1.150
netmask 255.255.255.0
gateway 192.168.1.1
wpa-essid SSID_Name
wpa-psk XXXXX
dns-nameservers 8.8.8.8 192.168.1.1
```

### Auto run SSH server

https://askubuntu.com/questions/3913/start-ssh-server-on-boot

```
sudo update-rc.d ssh defaults
```
