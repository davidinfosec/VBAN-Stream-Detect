# Automatic Audio Streaming with VBAN Packet Detection (Linux VBAN Reciever)

## Introduction

This tutorial guides you through setting up a Python script to detect VBAN audio streams. VBAN is a protocol for streaming audio over a network, commonly used in audio production setups.

## Requirements

- Raspberry Pi (or similar device)
- Ethernet or Wi-Fi connection
- VBAN-capable audio streaming device (VBAN transmitter via Voicemeeter / VB-Audio Matrix, etc.,)

## Setting Up

1. **Python Environment**:
    - Make sure you have Python installed. If not, download and install it from the [official Python website](https://www.python.org/).

2. **Python Libraries**:
    - Install the required Python libraries using pip:
    ```bash
    pip install scapy
    ```

3. **Download Scripts**:
    - Download the Python scripts from the provided repository.

## Running the Script

1. **VBAN Stream Detection**:
    - Run the `vban.py` script:
    ```bash
    python vban.py
    ```

## Understanding the Script

- `vban.py`: This script uses the `scapy` library to detect VBAN audio streams. It listens for UDP packets on port 6980 and executes actions when a stream is detected.

## Troubleshooting

- **Library Installation**:
    - Ensure you have installed the required library (`scapy`) using the correct Python environment.

## Conclusion

With this setup, you can automate tasks based on the presence of a VBAN audio stream. This can be extended to perform various actions based on different audio inputs.


## Automatic Startup Services

To ensure the VBAN receiver starts on boot, we'll set up a systemd service:

1. **Create a Service File**:
   - Open a terminal and run the following command to create a new service file:
   ```bash
   sudo nano /etc/systemd/system/vbanstart.service

Paste the following content into the file, then save and exit:

``
[Unit]
Description=VBAN Receiver Service
After=network.target

[Service]
Type=simple
ExecStart=/usr/bin/python /path/to/vban.py
Restart=always

[Install]
WantedBy=multi-user.target
``

Replace /path/to/vban.py with the actual path to your vban.py script.

Enable the Service:

Run the following command to enable the service:

``sudo systemctl enable vban_receiver.service``

This will start the VBAN receiver service on boot.

