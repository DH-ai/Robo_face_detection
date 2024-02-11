# Face detection for rover
This repo is a part of bigger project of making a mars rover, currently in its learning phase.


## Overview
Basically I've used OpenCV and Ros2 Humble in this project where there are two nodes one publishing the image data and other node subscribing to the topic and reciving it and as a exmale of processing on processing side it is detecting edges and faces.


## Getting Started
### Prerequisites
- OpenCV
- Ros2 Humble
- Python 3.13
- Access to webcam

### Installation
- Clone the git repository to any folder you like and make sure you have all the requirments completed. 
- Now for linux go source the setup.bash file as `source install/setup.bash`


### Usage
Now run the command `ros2 run my_webcam_feed webcam_feed` in one terminal and in other terminal `ros2 run my_webcam_feed Processor` 
