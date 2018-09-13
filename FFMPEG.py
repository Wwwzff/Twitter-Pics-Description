import glob as gb
import cv2

fourcc = cv2.VideoWriter_fourcc(*'mp4v')

#input path of the pics
img_path=gb.glob("D:\\EC601\\*.jpg")

#output video will be in the same path as the python file 
#define the output name, resolution, fps and etc. of the video
videoWriter=cv2.VideoWriter('result.mp4',fourcc,6,(1024,512))

for path in img_path:
    img=cv2.imread(path)
    img=cv2.resize(img,(1024,512))
    videoWriter.write(img)
