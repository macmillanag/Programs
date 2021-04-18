import cv2 as cv

face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier('haarcascade_eye.xml')
cap = cv.VideoCapture(0)

while (cv.waitKey(1) == -1):
    success, frame = cap.read()
    if success:
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5, minSize=(120, 120))
        for (x, y, w, h) in faces:
            cv.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            roi_gray = gray[y:y+h, x:x+w]
            eyes = eye_cascade.detectMultiScale(roi_gray, 1.03, 5, minSize=(40, 40))
 
            for (ex, ey, ew, eh) in eyes:
                cv.rectangle(frame, (x+ex, y+ey),(x+ex+ew, y+ey+eh), (0, 255, 0), 2)
        
        cv.imshow('Face Detection', frame)
    if cv.waitKey(1) == ord('q'):
        break
cap.release()
cv.destroyAllWindows()