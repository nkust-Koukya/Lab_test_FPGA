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

    thresh, output = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)
    
    erode_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
    erode = cv2.erode(output, erode_kernel)
    dilate = cv2.dilate(erode, erode_kernel)

    output = cv2.GaussianBlur(dilate, (5,5), 2)

    circles = cv2.HoughCircles(output,cv2.HOUGH_GRADIENT_ALT,dp=1.5,minDist=output.shape[0]//15,param1=300,param2= 0.9 ,minRadius=10,maxRadius=100)

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

def video(output):
    video_path = os.path.join( "videos","coin3.mp4")
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error opening video file")
        exit()
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out_draw = cv2.VideoWriter('draw.mp4', fourcc, fps, (width, height))
    out_dilate = cv2.VideoWriter('dilate.mp4', fourcc, fps, (width, height))
    if not out_draw.isOpened() or not out_dilate.isOpened():
        print("Error creating video writer")
        cap.release()
        exit()
    while True:
        ret , frame = cap.read()
        if not ret:
            break
        frame , dilate= Transform(frame)
        dilate_color = cv2.cvtColor(dilate, cv2.COLOR_GRAY2BGR)
        if output == True:
            out_dilate.write(dilate_color)
            out_draw.write(frame)
        cv2.imshow("Video", frame)
        cv2.imshow("Dilate", dilate)
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break
    cap.release()
    out_dilate.release()
    out_draw.release()

if __name__ == "__main__":
    output_video = True
    video(output_video)