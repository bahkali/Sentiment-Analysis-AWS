# Sentiment - Analysis App
import cv2, time

# Make a capture object 
video= cv2.VideoCapture(0) # or -1

# to record video uncomment the next 2 line
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# out = cv2.VideoWriter('output.avi')

print(video.isOpened())

# ifinty loop 
while(True):
    ret, frame = video.read()
    cv2.imshow('frame', frame)

    # out.write(frame)

    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # cv2.imshow('frame', gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# After release and destroy the object
video.release()
# out.release()
cv2.destroyAllWindows()
print(cv2.__version__)