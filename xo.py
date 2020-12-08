import cv2
import numpy as np
cv2.namedWindow('XOgame')
now='X'
curnum=[1,2,3,4,5,6,7,8,9]
def winning():
    if( curnum[0]==curnum[1] and curnum[0]==curnum[2]):
                  print(now,end=" ")
                  print("won the match")
    if( curnum[0]==curnum[3] and curnum[0]==curnum[6]):
                  print(now,end=" ")
                  print("won the match")
    if( curnum[1]==curnum[4] and curnum[1]==curnum[7]):
                  print(now,end=" ")
                  print("won the match")
    if( curnum[2]==curnum[5] and curnum[2]==curnum[8]):
                  print(now,end=" ")
                  print("won the match")
    if( curnum[6]==curnum[7] and curnum[6]==curnum[8]):
                  print(now,end=" ")
                  print("won the match")
    if( curnum[3]==curnum[4] and curnum[3]==curnum[5]):
                  print(now,end=" ")
                  print("won the match")
    if( curnum[0]==curnum[4] and curnum[0]==curnum[8]):
                  print(now,end=" ")
                  print("won the match")
    if( curnum[2]==curnum[4] and curnum[2]==curnum[6]):
                  print(now,end=" ")
                  print("won the match")

def click_event(event,x,y,flag,param):
    if event==cv2.EVENT_LBUTTONDOWN:
         print(x,y)
         global now
         global curnum
             
         if (x<200 and y<200):
             a=50;b=50;c=150;d=150;e=50;f=150;g=150;h=50;i=0
         if (x>200 and y<200 and x<400):
             a=250;b=50;c=350;d=150;e=350;f=50;g=250;h=150;i=1
         if (x>400 and y<200 and x<600):
             a=450;b=50;c=550;d=150;e=550;f=50;g=450;h=150;i=2
         if (x<200 and y>200 and y<400):
             a=50;b=250;c=150;d=350;e=150;f=250;g=50;h=350;i=3
         if (x<400 and y>200 and x>200 and y<400):
             a=250;b=250;c=350;d=350;e=350;f=250;g=250;h=350;i=4
         if (x>400 and y>200 and x<600 and y<400):
             a=450;b=250;c=550;d=350;e=550;f=250;g=450;h=350;i=5
         if (x<200 and y>400 and y<600):
             a=50;b=450;c=150;d=550;e=150;f=450;g=50;h=550;i=6
         if (x<400 and y>400 and x>200 and y<600):
             a=250;b=450;c=350;d=550;e=350;f=450;g=250;h=550;i=7
         if (x>400 and y>400 and x<600 and y<600):
             a=450;b=450;c=550;d=550;e=550;f=450;g=450;h=550;i=8
         global img
         if(now=='X'):
             img=(cv2.line(img,(a,b),(c,d),(255,255,255),3))
             img=(cv2.line(img,(e,f),(g,h),(255,255,255),3))
             curnum[i]='X'
             winning()
             now='O'
         else:
             img=(cv2.circle(img,((a+c)//2,(b+d)//2),50,(255,255,255),3))
             curnum[i]='O'
             winning()
             now='X'
         cv2.imshow('XOgame',img)
img=np.zeros((600,600,3),np.uint8)
img=cv2.line(img,(200,0),(200,600),(255,255,255),5)
img=cv2.line(img,(400,0),(400,600),(255,255,255),5)
img=cv2.line(img,(0,200),(600,200),(255,255,255),5)
img=cv2.line(img,(0,400),(600,400),(255,255,255),5)
cv2.imshow('XOgame',img)
cv2.setMouseCallback('XOgame',click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()
