import numpy as np
import cv2 as cv
import socket

addr = ("127.0.0.1", 65534)
buf = 512
width = 640
height = 480
cap = cv.VideoCapture(0)
cap.set(3, width)
cap.set(4, height)
code = 'start'
code = code + (buf - len(code)) * 'a'


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
