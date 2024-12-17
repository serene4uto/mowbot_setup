#!/bin/bash

# Variables
SERVICE_DIR="$(pwd)/services"
SERVICE_FILE="mowbot_uros_agent.service"
TARGET_DIR="/etc/systemd/system"
TARGET_PATH="$TARGET_DIR/$SERVICE_FILE"

# Copy the service file
echo "Copying $SERVICE_FILE to $TARGET_DIR..."
sudo cp "$SERVICE_DIR/$SERVICE_FILE" "$TARGET_PATH"

# Set permissions
echo "Setting permissions for $TARGET_PATH..."
sudo chmod 644 "$TARGET_PATH"

# Reload systemd to recognize the new service
echo "Reloading systemd daemon..."
sudo systemctl daemon-reload

# Enable the service to start on boot
echo "Enabling the service..."
sudo systemctl enable "$SERVICE_FILE"

# Start the service
echo "Starting the service..."
sudo systemctl start "$SERVICE_FILE"

# Verify the service status
echo "Checking service status..."
sudo systemctl status "$SERVICE_FILE"
