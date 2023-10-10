import cv2
trained_face_data=cv2.CascadeClassifier(r'C:\Users\arnav\Desktop\Codes\Python\AI_projects\haarcascade_frontalface_default.xml')

#select image to detect faces
#img = cv2.imread(r'C:\Users\arnav\Desktop\Codes\Python\AI_projects\avg.png')
webcam = cv2.VideoCapture(0)

while True:
    #read current frames
    successful_frame_read, frame =webcam.read()
    face_coordinates = trained_face_data.detectMultiScale(frame)
    for (x,y,w,h) in face_coordinates:
         cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0),3)
         a=x
         b=y+(h/2)
         cv2.putText(frame,"Human",(a,y+h),cv2.FONT_HERSHEY_SIMPLEX,1,(0, 0, 0),1,cv2.LINE_AA,)
    cv2.imshow('Face Detected', frame)
    key = cv2.waitKey(1)
    if key==113 or key==81:
         break

webcam.release()
print("Code ended sucessfully")



"""
# to convert to grey scale
greyscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# detect faces
face_coordinates = trained_face_data.detectMultiScale(greyscaled_img)

#print face coordiantes
#print(face_coordinates)# array type
# draw rectangles

for (x,y,w,h) in face_coordinates:
    cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0),3)


cv2.imshow('Face Detected', img)

# will wait unti a key is pressed 
cv2.waitKey()

print("code completed!!!")
"""