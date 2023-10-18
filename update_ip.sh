#!/bin/bash

# Prompt user for new IP address
read -p "Enter the new IP address: " new_ip

# Update the service file with the new IP address
sed -i "s/-i [0-9.]\+/-i $new_ip/" /etc/systemd/system/vbanstart.service

# Reload systemd to apply changes
sudo systemctl daemon-reload

# Restart the service
sudo systemctl restart vbanstart.service

echo "IP address updated to $new_ip. Service restarted."

