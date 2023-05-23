import sys
import argparse
import cv2
def extractImages(pathIn, pathOut):
    count = 0
    vidcap = cv2.VideoCapture('D:/Desktop/yolov5/runs/detect/exp26/testkhoii13.mp4')
    success, image = vidcap.read()
    success = True
    while success:
          vidcap.set(cv2.CAP_PROP_POS_MSEC, (count * 50))  # added this line
          success, image = vidcap.read()
          resized_img = cv2.resize(image, (640, 640))
          print('Read a new frame: ', success)
         # img_save = resize_img.save("D:/Desktop/data_doantotnghiep/fire_img2/test_khoi_%d.png" % count, image)
          cv2.imwrite("D:/Desktop/data_doantotnghiep/test_khoi/testkhoi_ngoaitroi%d.png" % count, image)  # save frame as JPEG file
          #cv2.imshow('Resized Frame', resize_img)
          count = count + 1
if __name__ == "__main__":
      a = argparse.ArgumentParser()
      a.add_argument("--pathIn", help="path to video")
      a.add_argument("--pathOut", help="path to images")
      args = a.parse_args()
      print(args)
      extractImages(args.pathIn, args.pathOut)
