# client.py
import bluetooth

def connect_to_service():
    target_name = "SampleIoTDevice"
    target_address = None

    nearby_devices = bluetooth.discover_devices(duration=5, lookup_names=True)

    for addr, name in nearby_devices:
        if name == target_name:
            target_address = addr
            break

    if target_address is None:
        print("Could not find target Bluetooth device nearby.")
        return

    print(f"Found target device with address: {target_address}")

    # Connect to the service
    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    sock.connect((target_address, 1))

    try:
        sock.send("Hello IoT Device\n")
        data = sock.recv(1024)
        print(f"Received: {data.decode('utf-8')}")
    finally:
        sock.close()

if __name__ == "__main__":
    connect_to_service()
