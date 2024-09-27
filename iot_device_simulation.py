# iot_device_simulation.py
import bluetooth

def advertise_service():
    # Create Bluetooth socket
    server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    port = bluetooth.PORT_ANY
    server_sock.bind(("", port))
    server_sock.listen(1)

    port = server_sock.getsockname()[1]

    # Advertise a service
    bluetooth.advertise_service(server_sock, "SampleIoTDevice",
                                service_classes=[bluetooth.SERIAL_PORT_CLASS],
                                profiles=[bluetooth.SERIAL_PORT_PROFILE])

    print(f"Waiting for a connection on RFCOMM channel {port}...")

    client_sock, client_info = server_sock.accept()
    print(f"Accepted connection from {client_info}")

    # Receive data from client
    try:
        while True:
            data = client_sock.recv(1024)
            if not data:
                break
            print(f"Received: {data.decode('utf-8')}")
            client_sock.send(b"Acknowledged\n")
    except OSError:
        pass

    print("Disconnected.")
    client_sock.close()
    server_sock.close()

if __name__ == "__main__":
    advertise_service()
