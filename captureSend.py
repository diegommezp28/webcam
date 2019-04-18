#!/usr/bin/env python
"""Webcam video streaming



Using OpenCV to capture frames from webcam.
Compress each frame to jpeg and save it.
Using socket to read from the jpg and send
it to remote address.
!!!press q to quit!!!
"""
import numpy as np
import cv2 as cv
import socket

addr = ("127.0.0.1", 4096)
buf = 512
cap = cv.VideoCapture(0)
code = 'start'


def sendFrame(frame):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    data = frame.tostring()
    s.sendto(code.encode('utf-8'), addr)
    for i in range(0, len(data), buf):
        s.sendto(data[i:i+buf], addr)
    s.close()


def captureFunc():
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret:
            cv.imshow('send', frame)
            sendFrame(frame)
            if cv.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break


if __name__ == '__main__':
    captureFunc()
    cap.release()
    cv.destroyAllWindows()
