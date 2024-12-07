# roscore &
# sleep 5
rosrun rosserial_arduino serial_node.py /dev/ttyACM0 _baud:=9600 &
# roslaunch depthai_ros_driver cam.launch &
rosrun rose_tvmc_msg interface.py
