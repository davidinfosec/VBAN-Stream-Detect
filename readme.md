# Automatic Audio Streaming with VBAN Packet Detection (Linux VBAN Receiver)

## Introduction

This tutorial guides you through setting up a Python script to detect VBAN audio streams. VBAN is a protocol for streaming audio over a network, commonly used in audio production setups.

Before getting started with implementing the automatic VBAN stream detection script, please consider following along from this blog post, published by Stanley Solutions' Blog. https://blog.stanleysolutionsnw.com/networked-audio-using-vban-and-rpi.html -- His blog post is well deserved of a majority of credit. I have added on some minor tweaks but his work is phenomenal and this repository is built majorly off of his post to modify some things for quality of life and automating tasks.

---
## Requirements

- Raspberry Pi (or similar device), will be receiving the audio
- Ethernet or Wi-Fi connection
- Speakers to send audio out of the 3.5mm jack on the Pi/transmission device
- VBAN-capable audio streaming device (VBAN transmitter via Voicemeeter / VB-Audio Matrix, etc.,), something to transmit from.
- TCPDump
- Python3
- Scapy, Python Library
## Setting Up

Update/Upgrade repositories:
``sudo apt-get update && sudo apt-get upgrade -y``

Install TCPDump:

```
sudo apt-get install TCPDump -y
```

Install Python3
```
sudo apt-get install Python3 -y
```

**Python Libraries**:
    - Install the required Python libraries using pip:

    ```bash
    pip install scapy
    ```

**Download Scripts**:
    - vban.py
    - start_vban.sh

**Download Services**:
    - vbanstart.service
## Running the Script

**VBAN Stream Detection**:
    - Run the `vban.py` script:

    ```bash
    python3 ./vban.py
    ```

## Automatic Startup Services

To ensure the VBAN receiver starts on boot, we'll set up a systemd service:

1. **Create a Service File**:
   - Open a terminal and run the following command to create a new service file:
   ```bash
   sudo nano /etc/systemd/system/vbanstart.service
```

Paste the following content into the file, then save and exit: (Alternatively you can download and copy the service from this repository into the destination)

```
[Unit]
Description=Start VBAN Script on Startup

[Service]
Type=simple
ExecStartPre=/bin/sleep 10
ExecStart=/bin/bash /path/to/start_vban.sh

[Install]
WantedBy=multi-user.target
```

Replace ``/path/to/vban.py`` with the actual path to your vban.py script.

Enable the Service:

Run the following command to enable the service:

```
sudo systemctl enable vbanstart.service
```

This will start the VBAN receiver service on boot.

## Understanding the Script

- `vban.py`: This script uses the `scapy` library to detect VBAN audio streams. It listens for UDP packets on port 6980 and executes actions when a stream is detected. It finds the stream with TCPDump.

## Troubleshooting

- **Library Installation**:
    - Ensure you have installed the required library (`scapy`) using the correct Python environment.

## Conclusion

With this setup, you can automate tasks based on the presence of a VBAN audio stream. This can be extended to perform various actions based on different audio inputs.