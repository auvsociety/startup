#!/bin/bash

source /opt/ros/noetic/setup.bash
source /home/jetson/ws/x/devel/setup.bash

echo "hello world"
roslaunch "/home/jetson/startup/launch/rosbag.launch"



