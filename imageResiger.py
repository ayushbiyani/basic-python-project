import cv2


src = cv2.imread("nature.jpg" , cv2.IMREAD_UNCHANGED)
# cv2.imshow("title" , src)
scale = 50 
width = int(src.shape[1] * scale / 100)
height = int(src.shape[0] * scale / 100)
dim = (width , height)

output = cv2.resize(src , dim , interpolation = cv2.INTER_AREA)

cv2.imwrite("new.jpg" , output)
cv2.waitKey(0)
cv2.destroyAllWindows
