import bluetooth

# Search for nearby Bluetooth devices
print("Searching for nearby Bluetooth devices...")
nearby_devices = bluetooth.discover_devices(lookup_names=True, duration=8)

# Print nearby devices
print("Found {} nearby devices:".format(len(nearby_devices)))
for addr, name in nearby_devices:
    print("  - {}: {}".format(addr, name))

# Connect to ESP32 Bluetooth device
esp32_mac_address = 'EC:DA:3B:36:37:56'
print("Connecting to ESP32 with MAC address:", esp32_mac_address)
sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((esp32_mac_address, 1))

try:
    while True:
        # Receive data from ESP32
        data = sock.recv(1024)
        print("Received:", data.decode())
except KeyboardInterrupt:
    sock.close()
    print("Bluetooth connection closed")
