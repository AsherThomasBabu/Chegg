import cv2
 
def funcRotate(degree=0):
    rotation_matrix = cv2.getRotationMatrix2D((width / 2, height / 2), degree, 1)
    rotated_image = cv2.warpAffine(original, rotation_matrix, (width, height))
    return rotated_image

     
original=cv2.imread('C:/Users/ASHER/Desktop/Screenshot 2020-09-24 225527.jpg',1)
height, width = original.shape[:2]

imgrot = funcRotate(degree=35)
cv2.imwrite('C:/Users/ASHER/Desktop/Screenshot 2020-09-24 225527.jpg', imgrot)