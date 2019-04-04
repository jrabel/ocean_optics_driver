# ocean_optics_driver
A ROS driver for ocean optics spectrometers

## Getting Started
This ROS driver makes use of python-seabreeze library which builds on the open-source API release by Ocean Optics (Seabreeze) to control their spectrometers. Therefore, you will need to install python-seabreeze as described at the following link: https://github.com/ap--/python-seabreeze

### Prerequisites
1. Install python-seabreeze
2. (Potential) Install catkin_pkg `pip install catkin_pkg`

### Installing
Clone this repository inside a new or pre-existing catkin workspace and simply run the catkin_make command at the workspace level to build.

### Running
1. Be sure to mark the ocean_optics_specs_server.py file as executable.
`chmod +x ocean_optics_specs_server.py`
2. Now you can simply run the ROS service server (python executable) using rosrun with the package name.
`source devel/setup.bash`
`rosrun ocean_optics_driver ocean_optics_specs_server.py`
3. Finally, you can make a call to the ROS service as follows:
  Run Calibration Scan:`rosservice call /ocean_optics_spec_calibration_scan`
  Run Reflectance Scan: `rosservice call /ocean_optics_spec_reflectance_scan`
