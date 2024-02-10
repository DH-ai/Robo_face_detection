import cv2 
import rclpy
from cv_bridge import CvBridge
from sensor_msgs.msg import Image

from rclpy.node import Node


class ImageProcessor(Node):
    def __init__(self):
        super().__init__("Processor")

        self.img_sub  = self.create_subscription(Image,"no_process_node",self.callback,10)
        self.bridge = CvBridge()
        
        self.count = 1

    def callback(self,msg:Image):

        cv_image = self.bridge.imgmsg_to_cv2(msg)
        # cv2.imwrite(f"src/my_webcam_feed/my_webcam_feed/feed/img{self.count}.jpg",cv_image)
        # self.count = self.count+1
        cv2.imshow("hola",cv_image)

        edges = cv2.Canny(image=cv_image, threshold1=100, threshold2=200) 
 
        cv2.imshow('Canny Edge Detection', edges)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            return 
        
        
        
        self.get_logger().info("Doing Magic")
      
        
      
        
        
        
def main(args=None):
    rclpy.init(args=args)
    node = ImageProcessor()
    rclpy.spin(node=node)
    rclpy.shutdown

if __name__ == '__main__':

    main()  