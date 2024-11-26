# importing the required packages
import pyautogui
import cv2
import numpy as np

# specify resolution
resolution = (1920, 1080)

# specify video codec
codec = cv2.VideoWriter_fourcc(*"XVID")

# specify name of output file 
filename = "Recording.avi"

# specify frames rate. We can choose any 
# value and experimaent with it 
fps = 60.0

# creating a videoWriter object 
out = cv2.VideoWriter(filename, codec, fps, resolution)

# create an empty window 
cv2.namedWindow("Live", cv2.WINDOW_NORMAL)

# resize this window 
cv2.resizeWindow("Live", 480, 270)

while(True):
    # take screenshot using PyAtoGUI 
    img = pyautogui.screenshot()

    # convert the screenshot to a numpy array 
    frame = np.array(img)

    # convert it from BGR(Blue, Green, Red) to 
    # RGB(Red, Green, Blue)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # write it to the output file 
    out.write(frame)

    # optional: display the recording screen 
    cv2.imshow('Live', frame)

    # Stop recording when we press 'q'
    if cv2.waitKey(1) == ord('q'):
        break

# release the video writer
out.release()

# destroy all windows 
cv2.destroyAllWindows()