import cv2 
import rclpy
import cv_bridge
from sensor_msgs.msg import Image

from rclpy.node import Node


class ImageProcessor(Node):
    def __init__(self):
        super().__init__("Processor")

        self.img_sub  = self.create_subscription(Image,)