#!/usr/bin/env python3


import cv2
import rclpy
from rclpy.node import Node
from cv_bridge import CvBridge
from sensor_msgs.msg import Image








class imagePublisher(Node):

    
    def __init__(self):
        super().__init__("webcam_node")
        timer = 1/60 #may be it means 20 millisecond  its 5 frame per second if works fine 
        
        self.cap = cv2.VideoCapture(0)
        self.publisher = self.create_publisher(Image,"no_process_node",10)
        self.bridge = CvBridge()

        self.timer =self.create_timer(timer,callback=self.callback)
        
    def callback(self):
        # msg = Image()
        
        ret, frame = self.cap.read()
        if not ret:
            self.get_logger().info(f"Video Capture status {self.cap.read()[0]}")
        else:
            image_msg = self.bridge.cv2_to_imgmsg(frame)
            # msg.data = image_msg
            self.publisher.publish(image_msg)
            self.get_logger().info(f"Feed sent status {self.cap.read()[0]}")
        
            # self.get_logger().info(msg)
        

        
    
   
    

def main (args=None):
    rclpy.init(args=args)
    node = imagePublisher()
    rclpy.spin(node=node)
    rclpy.shutdown

if __name__ == '__main__':

    main()  



# if not  cap.isOpened():
#     print ("Erorr in opening the camera")
#     exit()

# while True:
    
#     ret, frame = cap.read() 
#     # cv2.imshow("lol",frame)

#     img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     ret , thresh = cv2.threshold(img_gray,140,255,cv2.THRESH_BINARY)
#     contours, hierarchy = cv2.findContours(image=thresh, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_NONE)
#     contours2, hierarchy2 = cv2.findContours(image=thresh, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_SIMPLE)
    
    
#     image_copy = frame.copy()
#     image_copy2 = frame.copy()
#     cv2.drawContours(image=image_copy, contours=contours, contourIdx=-1, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)
#     cv2.drawContours(image=image_copy2, contours=contours2, contourIdx=-1, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)
#     # for i, contour in enumerate(contours2): 
#     #     for j, contour_point in enumerate(contour): 
#     #         cv2.circle(image_copy2, ((contour_point[0][0], contour_point[0][1])), 2, (0, 255, 0), 2, cv2.LINE_AA)
            
           

#     if not ret:
#         print("Error: Couldn't read frame.")
#         break
#     # cv2.imshow("image_copy2", image_copy2)
#     cv2.imshow("threshold",thresh)
#     cv2.imshow('Nimage_copy', image_copy)
    
#     # cv2.imwrite('image_thres1.jpg', thresh)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()