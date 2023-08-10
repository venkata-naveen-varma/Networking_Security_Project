import network
import urequests
import utime
import dht
import network
import ubinascii
from machine import Pin
from time import sleep
from pytea import TEA

SSID = "Adeels iPhone"
PASSWORD = "moipassword"

def connect_wifi():
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        sta_if.active(True)
        sta_if.connect(SSID, PASSWORD)
        while not sta_if.isconnected():
            pass
    print('Connected to Wi-Fi! IP:', sta_if.ifconfig()[0])
    return sta_if.ifconfig()[0]

sensor = dht.DHT22(Pin(2))
key = b'WE\r\xd5B\xe4\xf7*\x05,}J\xe4\x97\xdc\xff'

def encrypt_data(content):
    tea = TEA(key)
    e = tea.encrypt(content.encode())
    return e.hex()

def decrypt_data(content):
    tea = TEA(key)
    d = tea.decrypt(content)
    return d.hex()

def get_temperature_and_humidity():
    sensor.measure()
    temp = str(sensor.temperature())
    hum = str(sensor.humidity())
    return temp, hum

def send_data_to_google_sheet(timestamp, mac, temp, hum):
    endpoint = "https://script.google.com/macros/s/AKfycbxWAN5WnDL8WMvzPZWlf7xNvmtj_f4btSJDesg5Ox70neOy-gLZw2Hvem_FeJaXsgXu/exec"
    headers = {"Content-Type": "application/json"}
    data = {
        "timestamp": timestamp,
        "macAddress": mac,
        "temperature": temp,
        "humidity": hum
    }
    encrypted_data = {
        "timestamp": encrypt_data(timestamp),
        "macAddress": encrypt_data(mac),
        "temperature": encrypt_data(temp),
        "humidity": encrypt_data(hum)
    }

    print('Plain payload:', data)
    print('\n')
    print('Encrypted payload:', encrypted_data)
    response = urequests.post(endpoint, headers=headers, json=encrypted_data)
    print('Response status code:',response.status_code)
    response.close()
    print('\n\n')

# Main execution
connect_wifi()

mac_address = str(ubinascii.hexlify(network.WLAN().config('mac'),':').decode())
while True:
    timestamp = str(utime.time())
    temperature, humidity = get_temperature_and_humidity()
    send_data_to_google_sheet(timestamp, mac_address, temperature, humidity)
    sleep(10)
