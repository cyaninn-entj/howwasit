import numpy as np
import pandas as pd
import cv2

img = cv2.imread("white_black.jpg")
#이미지 불러오기

index=["color", "color_name", "hex", "R", "G", "B"]
csv = pd.read_csv('colors.csv', names=index, header=None)
#read_csv 메소드를 사용하여 colors.csv 파일을 프로그램으로 가져 오겠습니다 . 
#다운로드 한 csv 파일에는 열 이름이 없으므로 프로그램에서 정의 할 것입니다. 이 프로세스를 데이터 조작이라고합니다.

clicked = False
r = g = b = xpos = ypos = 0
#다음 단계에서는 두 가지 기능을 정의합니다. 응용 프로그램이 원활하게 작동하려면 전역 변수가 필요합니다. 
#함수로 작업 할 때 전역 변수가 어떻게 도움이 될 수 있는지 알게 될 것입니다.

def recognize_color(R,G,B):
    minimum = 10000
    for i in range(len(csv)):
        d = abs(R- int(csv.loc[i,"R"])) + abs(G- int(csv.loc[i,"G"]))+ abs(B- int(csv.loc[i,"B"]))
        if(d<=minimum):
            minimum = d
            cname = csv.loc[i,"color_name"]
    return cname
#이 함수는 이미지 영역을 더블 클릭하면 호출됩니다. 색상 이름과 해당 색상의 RGB 값을 반환합니다. 마법이 일어나는 곳입니다!

def mouse_click(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global b,g,r,xpos,ypos, clicked
        clicked = True
        xpos = x
        ypos = y
        b,g,r = img[y,x]
        b = int(b)
        g = int(g)
        r = int(r)
#이 함수는 더블 클릭 프로세스를 정의하는 데 사용됩니다. 응용 프로그램 부분을 만들 때 필요합니다.

cv2.namedWindow('Color Recognition App')
cv2.setMouseCallback('Color Recognition App', mouse_click)

while(1):
    cv2.imshow("Color Recognition App",img)
    if (clicked):
        #cv2.rectangle(image, startpoint, endpoint, color, thickness)-1 fills entire rectangle 
        cv2.rectangle(img,(20,20), (750,60), (b,g,r), -1)
        #Creating text string to display( Color name and RGB values )
        text = recognize_color(r,g,b) + ' R='+ str(r) +  ' G='+ str(g) +  ' B='+ str(b)
        
    #cv2.putText(img,text,start,font(0-7),fontScale,color,thickness,lineType )
        cv2.putText(img,text,(50,50),2,0.8,(255,255,255),2,cv2.LINE_AA)
#For very light colours we will display text in black colour
        if(r+g+b>=600):
            cv2.putText(img, text,(50,50),2,0.8,(0,0,0),2,cv2.LINE_AA)
            
        clicked=False

#Break the loop when user hits 'esc' key    
    if cv2.waitKey(20) & 0xFF ==27:
        break
cv2.destroyAllWindows()
