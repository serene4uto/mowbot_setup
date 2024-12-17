export DISPLAY=:0
xhost +local:docker

docker exec -it -e DISPLAY=:0.0 -w /workspaces/mowbot/mowbot_ws mowbot_humble /bin/bash -c "\
        cd /workspaces/mowbot/mowbot_ws \
        && . ./install/setup.bash \
        && ros2 launch mowbot_navigation nav_gps_waypoints_follower.launch.py mapviz:=true rviz:=true rl:=true\
    "