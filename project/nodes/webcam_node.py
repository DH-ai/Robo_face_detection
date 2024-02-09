import cv2


cap = cv2.VideoCapture(0)




if not  cap.isOpened():
    print ("Erorr in opening the camera")
    exit()


while True:
    
    ret, frame = cap.read() 
    # cv2.imshow("lol",frame)

    img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ret , thresh = cv2.threshold(img_gray,140,255,cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(image=thresh, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_NONE)
    contours2, hierarchy2 = cv2.findContours(image=thresh, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_SIMPLE)
    
    
    image_copy = frame.copy()
    image_copy2 = frame.copy()
    cv2.drawContours(image=image_copy, contours=contours, contourIdx=-1, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)
    cv2.drawContours(image=image_copy2, contours=contours2, contourIdx=-1, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)
    # for i, contour in enumerate(contours2): 
    #     for j, contour_point in enumerate(contour): 
    #         cv2.circle(image_copy2, ((contour_point[0][0], contour_point[0][1])), 2, (0, 255, 0), 2, cv2.LINE_AA)
            
           

    if not ret:
        print("Error: Couldn't read frame.")
        break
    # cv2.imshow("image_copy2", image_copy2)
    cv2.imshow("threshold",thresh)
    cv2.imshow('Nimage_copy', image_copy)
    
    # cv2.imwrite('image_thres1.jpg', thresh)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()