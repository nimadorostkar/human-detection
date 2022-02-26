from tkinter import *
import tkinter as tk
import os
from PIL import ImageTk, Image





def callback():
    os.system("python detect_video.py --video 0")

# webcam - python detect_video.py --video 0
# video file - python detect_video.py --video data/video/paris.mp4 --weights ./weights/yolov3-tiny.tf --tiny
# video file with output saved (can save webcam like this too) - python detect_video.py --video path_to_file.mp4 --output ./detections/output.avi


root = Tk()
canvas = Canvas(root, width=1200, height=600)
canvas.pack(expand = True, fill = "both")
btn = tk.Button(root, command=callback,
                activebackground = "#33B5E5")
btn.place(height=100, width=100, x=20, y=20)
img1 = ImageTk.PhotoImage(Image.open("data/images/camera.png"))
btn.config(image=img1, width=200, height=100)
img2 = ImageTk.PhotoImage(Image.open("data/images/bk.jpg"))
canvas.create_image(20, 10, anchor=NW, image=img2)
canvas.create_window(600, 550,height=140, width=250, anchor='s', window=btn)
root.mainloop()
