# Q1
![Question](images/Question.png)
### 辨識影片中的硬幣並繪製框線

### 主要CODE
```python

    轉換成灰階
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)   

    做二值化 閥值設在150
    thresh, output = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
    
    設定膨脹侵蝕的kernal size
    erode_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
    
    侵蝕
    erode = cv2.erode(output, erode_kernel)
    
    膨脹
    dilate = cv2.dilate(erode, erode_kernel)
```

### 左側為輸入影片及添加框後的影片 右側為前處理後的中途影片
![result1](images/result1.png)
