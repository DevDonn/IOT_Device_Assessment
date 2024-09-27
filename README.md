# IoT Device Security Assessment using Bluetooth Communication

## Project Overview
This project simulates an IoT device that communicates via Bluetooth using Python and PyBluez. It demonstrates how to set up a basic Bluetooth server (IoT device) and client, exchange data, and capture traffic for security assessment using Wireshark. The goal is to identify potential vulnerabilities like unencrypted communication or weak encryption in IoT device communication.

## Features
- Simulates an IoT device using Bluetooth RFCOMM protocol.
- Establishes communication between a Python-based client and server.
- Captures Bluetooth traffic using Wireshark to assess vulnerabilities.
- Identifies common issues such as unencrypted data transmission or weak security practices.

## Technologies Used
- **Python 3**
- **PyBluez** (Python Bluetooth library)
- **Wireshark** (for traffic capture and analysis)
- **BlueZ** (Linux Bluetooth stack)

## Prerequisites
- A Linux system with Bluetooth capabilities.
- Python 3 installed.
- Bluetooth libraries: PyBluez and BlueZ.
- Wireshark installed for traffic analysis.

## Setup and Installation

1. **Install Dependencies**
   On a Linux system, run the following commands to install the required dependencies:

   ```bash
   sudo apt-get update
   sudo apt-get install python3-pip bluetooth libbluetooth-dev bluez
   pip3 install pybluez
   sudo apt-get install wireshark
   ```

2. **Clone the Repository**
   Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/iot-device-security-assessment.git
   cd iot-device-security-assessment
   ```

3. **Run the IoT Device (Server)**
   Run the Python script to simulate the IoT device that will wait for a Bluetooth connection:

   ```bash
   sudo python3 iot_device_simulation.py
   ```

4. **Run the Bluetooth Client**
   On a separate terminal, run the client script to connect to the simulated IoT device and send data:

   ```bash
   python3 client.py
   ```

5. **Capture Bluetooth Traffic Using Wireshark**
   - Open Wireshark and select the Bluetooth interface (e.g., `bluetooth0`).
   - Start capturing traffic and observe the data being transmitted between the client and server.

## How It Works
- **IoT Device Simulation**: The server script sets up a Bluetooth RFCOMM channel and waits for incoming connections. When the client connects, they exchange data.
- **Security Analysis**: Using Wireshark, the Bluetooth communication is captured and analyzed for vulnerabilities, such as unencrypted transmissions or weak pairing.

## Potential Vulnerabilities
- **Unencrypted Data Transmission**: Data sent between the client and server is not encrypted, which can be exploited by attackers.
- **Weak Authentication**: This setup does not implement any form of authentication, making it susceptible to unauthorized connections.

## Improvements
- Implement basic encryption for communication between the client and server.
- Add secure pairing mechanisms to mitigate unauthorized access.
- Explore other IoT communication protocols for further analysis.

