import cv2 
import numpy as np
import os
import time


def show_image(title, img):
    cv2.imshow(title, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def Transform(img):

    if img is None:
        print("Image load failed")
        return

    start = time.time()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    thresh, output = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
    
    erode_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
    erode = cv2.erode(output, erode_kernel)

    dilate = cv2.dilate(erode, erode_kernel)


    output = cv2.GaussianBlur(dilate, (5,5), 2)
    circles = cv2.HoughCircles(output,cv2.HOUGH_GRADIENT,dp=1.5,minDist=output.shape[0]//8,param1=100,param2= 50 ,minRadius=0,maxRadius=100)

    if circles is not None:
        circles = np.uint16(np.around(circles))

        for (x, y, r) in circles[0, :]:
            cv2.circle(img, (x, y), r, (0, 0, 255), 2)

            x1, y1 = x - r, y - r
            cv2.rectangle(img, (x1, y1), (x+r, y+r), (0,255,0), 2)

            cv2.putText(img, f"({x1},{y1})",
                        (x1, y1-5),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.5, (0,255,0), 2)

    end = time.time()
    print(f"Time: {end-start:.4f} sec")

    return img , output

def video():
    video_path = os.path.join( "videos","coin2.mp4")
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error opening video file")
        exit()
    while True:
        ret , frame = cap.read()
        if not ret:
            break
        frame , dilate= Transform(frame)
        cv2.imshow("Video", frame)
        cv2.imshow("Dilate", dilate)
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break

if __name__ == "__main__":
    video()