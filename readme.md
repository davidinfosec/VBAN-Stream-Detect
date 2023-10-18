# Automatic Audio Streaming with VBAN Packet Detection (Linux VBAN Receiver)

## Introduction

This tutorial guides you through setting up a Python script to detect VBAN audio streams. VBAN is a protocol for streaming audio over a network, commonly used in audio production setups.

Before getting started with implementing the automatic VBAN stream detection script, please consider following along from this [blog post](https://blog.stanleysolutionsnw.com/networked-audio-using-vban-and-rpi.html), published by Stanley Solutions' Blog. His blog post is well deserved of a majority of credit. I have added on some minor tweaks but his work is phenomenal and this repository is built majorly off of his post to modify some things for quality of life and automating tasks.

## Requirements

- Raspberry Pi (or similar device), will be receiving the audio
- Ethernet or Wi-Fi connection
- Speakers to send audio out of the 3.5mm jack on the Pi/transmission device
- VBAN-capable audio streaming device (VBAN transmitter via Voicemeeter / VB-Audio Matrix, etc.,), something to transmit from.
- TCPDump
- Python3
- Scapy, Python Library

# Setting Up

On your VBAN Transmitter, pick and remember a stream name. In my example, my stream is "StereoPi", correlating with the blog post mentioned above from Stanley Solutions. You will have to change the scripts to account for whatever the name is. This repository may eventually have a bash script to help you with this change. Stay posted.

## Update/Upgrade repositories:

```bash
sudo apt-get update && sudo apt-get upgrade -y
```

## Install TCPDump

```bash
sudo apt-get install TCPDump -y
```

## Install Python3

```bash
sudo apt-get install Python3 -y
```

## Install Python Libraries

```bash
sudo pip install scapy
```

## Download Scripts
- vban.py
- start_vban.sh
## Download Services
- vbanstart.service

## Running the Script

**VBAN Stream Detection**:
    - Run the `vban.py` script:

```bash
python3 ./vban.py
```

## Automatic Startup Services:

To ensure the VBAN receiver starts on boot, we'll set up a systemd service:

1. **Create a Service File**:
   - Open a terminal and run the following command to create a new service file:
```bash
sudo nano /etc/systemd/system/vbanstart.service
```

Paste the following content into the file, then save and exit: (Alternatively you can download and copy the service from this repository into the destination)

```bash
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

## Enable The Service:

```bash
sudo systemctl enable vbanstart.service
```

You can also use ``systemctl start`` or ``systemctl stop``.


Script to Manually Change Stream IP:
You can use the update_ip.sh script to manually enter a stream IP if one was not automatically found or if you prefer a different stream source:

Make the script executable:

```bash
sudo chmod +x update_ip.sh
```

Run the script
```bash
sudo ./update_ip.sh
```

Enter the desired IP address when prompted. Wait for the service to restart.

---

## Understanding the Script

- `vban.py`: This script uses the `scapy` library to detect VBAN audio streams. It listens for UDP packets on port 6980 and executes actions when a stream is detected. It finds the stream with TCPDump.

## Troubleshooting

- **Library Installation**:
    - Ensure you have installed the required library (`scapy`) using the correct Python environment.
 
- **Not working on restart**:
    - If not working on restart, try adding some sleep time on the service before it starts. The network devices may need time to come up and propogate an IP address before TCPDump can start looking for VBAN packets. 

## Conclusion

With this setup, you can automate tasks based on the presence of a VBAN audio stream. This can be extended to perform various actions based on different audio inputs.
