import cv2
import os


cap = cv2.VideoCapture("src/my_webcam_feed/my_webcam_feed/feed/img%01d.jpg")

i = 56
while True:
    ret, f = cap.read()
    # cv2.imshow("ds",f)
    print ("playes",i)
    
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break
    os.remove(f"src/my_webcam_feed/my_webcam_feed/feed/img{i}.jpg")
    print("removed",i)
    i+=1

cap.release()
cv2.destroyAllWindows()