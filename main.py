# Import necessary libraries
import machine  # MicroPython hardware control
import network  # Network configuration and management
import time     # Time-related functions
import socket   # Socket module for creating a socket server
import urequests  # Module for making HTTP requests

# WiFi network configuration
# WIFI_SSID =  "Proximus-Home-CBD0"  # WiFi network name (SSID)
# WIFI_PASSWORD = "wf9wzu96z4cmx"   # WiFi network password
WIFI_SSID =  "electroProjectWifi"  # WiFi network name (SSID)
WIFI_PASSWORD = "M13#MRSE"   # WiFi network password
# LED pin configuration
led = machine.Pin(2, machine.Pin.OUT)  # Configure a LED connected to GPIO pin 2

# Connect to the WiFi network
print('Connecting to the WiFi network...')
wlan = network.WLAN(network.STA_IF)  # Activate station (STA) mode for WiFi connection
wlan.active(True)  # Enable WiFi
wlan.connect(WIFI_SSID, WIFI_PASSWORD)  # Connect to the specified WiFi network

# Wait for the WiFi connection
while not wlan.isconnected():
    led.on()  # Turn on the LED to indicate connection attempt
    time.sleep(0.5)  # Wait for 0.5 seconds
    led.off()  # Turn off the LED
    time.sleep(0.5)  # Wait for another 0.5 seconds

led.on()  # Turn on the LED (connection successful)
time.sleep(3)  # Wait for 3 seconds to indicate successful connection
print('Connected to the WiFi network')
ip = wlan.ifconfig()
print("IP info (IP address, mask, gateway, DNS):")
print(ip)
led.off()  # Turn off the LED