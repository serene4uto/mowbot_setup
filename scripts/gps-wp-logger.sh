export DISPLAY=:0
xhost +local:docker

docker exec -it -e DISPLAY=:0.0 -w /workspaces/mowbot_ros2_devcontainer/mowbot_ws mowbot_humble /bin/bash -c "\
        cd /workspaces/mowbot_ros2_devcontainer/mowbot_ws \
        && . ./install/setup.bash \
        && ros2 launch mowbot_navigation nav_gps_waypoints_logger.launch.py rl:=true \
    "