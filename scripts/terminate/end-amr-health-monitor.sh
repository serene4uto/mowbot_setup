#!/bin/bash

# Define Docker container name
CONTAINER_NAME="mowbot_humble"

# Function to kill a process tree
kill_process_tree() {
    local PID=$1
    docker exec "$CONTAINER_NAME" bash -c "pstree -p $PID | grep -oP '\(\d+\)' | grep -oP '\d+' | xargs kill -9"
}

# Function to find and kill ROS2 processes
kill_ros2_process() {
    local PATTERN=$1
    echo "Searching for processes matching: $PATTERN"
    ROS2_PID=$(docker exec "$CONTAINER_NAME" pgrep -f "$PATTERN")
    
    if [ -z "$ROS2_PID" ]; then
        echo "No process found for pattern: $PATTERN in container $CONTAINER_NAME."
        return 1
    fi

    echo "Found process with PID: $ROS2_PID for pattern: $PATTERN"
    echo "Killing process tree..."
    kill_process_tree "$ROS2_PID"
    if [ $? -eq 0 ]; then
        echo "Successfully killed process tree for pattern: $PATTERN."
    else
        echo "Failed to kill process tree for pattern: $PATTERN."
    fi
}

# Kill the ros2 launch command
kill_ros2_process "ros2 launch mowbot_bringup bringup.launch.py"

# Kill the ros2 run command
kill_ros2_process "ros2 run py_mowbot_utils system_monitor"
