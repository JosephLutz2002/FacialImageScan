import cv2


def count_data(image_source):
    grey_image = cv2.cvtColor(image_source,cv2.COLOR_BGR2GRAY)
    
    _, data_thesh = cv2.threshold(grey_image,0,255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    
    contours ,_ = cv2.findContours(data_thesh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    finger_count = 0
    for contour in contours:
        c_area = cv2.contourArea(contour)
        if c_area > 100:
            finger_count+=1
    return finger_count


cap = cv2.VideoCapture(0)
while True:
    ret,frame = cap.read()
    if not ret:
        break
    digits = count_data(frame)
    cv2.putText(frame,f"The number of digitts is {digits}",(10,30),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
    cv2.imshow('Finger Count software',frame)
    
    if cv2.waitKey(1) &0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
    