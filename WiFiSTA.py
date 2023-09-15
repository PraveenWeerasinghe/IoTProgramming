import network

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.scan()
wlan.isconnected() 
wlan.connect('Praveen', 'praveen@123')
wlan.ifconfig()
wlan.status()
