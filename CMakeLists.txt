cmake_minimum_required(VERSION 2.8.3)
project(ocean_optics_driver)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  genmsg
  message_generation
)


## Generate services in the 'srv' folder
add_service_files(
  FILES
  OceanOptics.srv
)

generate_messages(
  DEPENDENCIES
)

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES refl_spec
  CATKIN_DEPENDS roscpp rospy std_msgs
  DEPENDS system_lib
)

