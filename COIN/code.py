import cv2 
import numpy as np
import os
import time

def Transform():
    imgpath = os.path.join("images", "pic3.jpg")
    img = cv2.imread(imgpath)

    if img is None:
        print("Image load failed")
        return

    start = time.time()

    # ✅ 1. resize（最重要）
    img = cv2.resize(img, (640, 480))

    # ✅ 2. 灰階
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # ✅ 3. 輕量模糊
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # ❌ 不需要 Canny（已移除）

    # ✅ 4. Hough Circle（正確輸入）
    circles = cv2.HoughCircles(
        blur,
        cv2.HOUGH_GRADIENT,
        dp=1.2,
        minDist=80,
        param1=100,
        param2=30,
        minRadius=30,
        maxRadius=120
    )

    if circles is not None:
        circles = np.uint16(np.around(circles))

        for (x, y, r) in circles[0, :]:
            # 畫圓
            cv2.circle(img, (x, y), r, (0, 0, 255), 2)

            # bounding box
            x1, y1 = x - r, y - r
            cv2.rectangle(img, (x1, y1), (x+r, y+r), (0,255,0), 2)

            cv2.putText(img, f"({x1},{y1})",
                        (x1, y1-5),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.5, (0,255,0), 2)

    end = time.time()
    print(f"Time: {end-start:.4f} sec")

    cv2.imshow("Result", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    Transform()