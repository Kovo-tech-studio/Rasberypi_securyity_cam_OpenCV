import cv2

#img counter
count = 0

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# To capture video from webcam. 
cap = cv2.VideoCapture(0)
# To use a video file as input 
# cap = cv2.VideoCapture('filename.mp4')

while True:
    # Read the frame
    _, img = cap.read()
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Draw the rectangle around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 51, 0), 2)
        # Check if the face detection is True.
        if  faces.any() == True:
            print("Face detected")
            #take picture of your face
            print("Image "+str(count)+"saved")
            file='C:/Users/techn/Desktop/img'+str(count)+'.jpg'
            cv2.imwrite(file, img)
            count +=1

            if count >= 10:
                print("starting mail bot")
                count = 0
                import smtplib
                import random
                from email.mime.text import MIMEText
                from email.mime.multipart import MIMEMultipart
                from email.mime.base import MIMEBase
                from email import encoders

                #random select img
                X = random.randint(0,9)
                print(X)

                sender_email = "your email"
                rec_email = "reciver email"
                password = "your pass"

                #gmail.text
                subject ='!Security massage!'
                message = "We found someone who you might do not know."

                #___________________
                #subject inport
                msg = MIMEMultipart()
                msg['From'] = sender_email
                msg['To'] = rec_email
                msg['Subject'] = subject

                msg.attach(MIMEText(message,'plain'))
                #file
                filename='img5.jpg'
                attachment  =open(filename,'rb')
    
                part = MIMEBase('application','octet-stream')
                part.set_payload((attachment).read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition',"attachment; filename= "+filename)


                msg.attach(part)
                text = msg.as_string()
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(sender_email, password)
                print("Login success")

                server.sendmail(sender_email, rec_email, text)
                print("Email has been sent to ", rec_email)

                server.quit()

                




            
                
                
        
    # Display
    cv2.imshow('img', img)
    # Stop if escape key is pressed
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break

# Release the VideoCapture object
cap.release()


