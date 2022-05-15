# npy-visualizer
Package that converts npy files into ROS pointclouds that can be used for processing and visualisation 

## Installation

1. Clone the repository in the ```src``` folder of your ```catkin_ws``` and run ```catkin_make```
2. Source the workspace by running ```source devel/setup.bash``` in at the top of the workspace

### Running
1. Edit the launch file to include the directory containing your npy file names and a txt file with the name of all the npy files
2. Run ```roslaunch npy_visualizer lidar_viz.launch``` or ```roslaunch src/npy_visualizer/launch/lidar_viz.launch ```

Note: The pointclouds are published with the frame id ```lidar_link``` which can be changed in the ```npy_visualize.py``` script

