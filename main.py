# Import necessary libraries
import machine  # MicroPython hardware control
import network  # Network configuration and management
import time     # Time-related functions
import socket   # Socket module for creating a socket server
import urequests  # Module for making HTTP requests
import struct


# WiFi network configuration
# WIFI_SSID =  "Proximus-Home-CBD0"  # WiFi network name (SSID)
# WIFI_PASSWORD = "wf9wzu96z4cmx"   # WiFi network password
#WIFI_SSID =  "electroProjectWifi"  # WiFi network name (SSID)
#WIFI_PASSWORD = "M13#MRSE"   # WiFi network password
WIFI_SSID =  "OnePlus Nord"  # WiFi network name (SSID)
WIFI_PASSWORD = "baptiste"   # WiFi network password
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

TCP_SERVER_ADDRESS = "192.168.232.248"
TCP_SERVER_PORT = 12345
UDP_SERVER_ADDRESS = "192.168.232.248"
UDP_SERVER_PORT = 12000

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Crée une socket UDP
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


counter = 1  # Commencez avec 1 au lieu de 0
while True:
    # Envoie via UDP
    udp_message = str(counter)
    udp_socket.sendto(udp_message.encode(), (UDP_SERVER_ADDRESS, UDP_SERVER_PORT))

    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        tcp_socket.connect((TCP_SERVER_ADDRESS, TCP_SERVER_PORT))
        tcp_message = str(counter)
        tcp_socket.send(tcp_message.encode())
    except Exception as e:
        print("Error sending TCP data:", e)
    finally:
        tcp_socket.close()
        
    # Attendez avant d'envoyer la prochaine fois
    time.sleep(0.01)
    # Incrémente le compteur
    counter += 10
    if counter > 250:
        
        counter=0
    #ok