# YOLOV3 & Tensorflow object detection and report human movements in persian
Yolov3 is an algorithm that uses deep convolutional neural networks to perform object detection. This repository implements Yolov3 using TensorFlow <br>
<div dir="rtl">
الگوریتم‌های مختلفی برای پیاده‌سازی سیستم تشخیص اشیا در نظر گرفته شدند، اما در نهایت، الگوریتم YOLO به عنوان الگوریتم اصلی بر پیاده‌سازی این سیستم در نظر گرفته شد. دلیل انتخاب الگوریتم YOLO، سرعت بالا و قدرت محاسباتی آن و همچنین، وجود منابع آموزشی زیاد برای راهنمایی کاربران هنگام پیاده‌سازی این الگوریتم است. 
<div> <br>

![example](https://github.com/nimadorostkar/human-detection/blob/master/data/images/simple.gif)

## Getting started
<div dir="ltr">

#### Pip
```bash
pip install -r requirements.txt

```
### Downloading official pretrained weights <div>
###  <div dir="rtl">  از لینک های زیر dataset رو میتونید دانلود کنید   <div>
<div dir="ltr">
For Linux: Let's download official yolov3 weights pretrained on COCO dataset. 

```
# yolov3
wget https://pjreddie.com/media/files/yolov3.weights -O weights/yolov3.weights

# yolov3-tiny
wget https://pjreddie.com/media/files/yolov3-tiny.weights -O weights/yolov3-tiny.weights
```
For Windows:
You can download the yolov3 weights by clicking [here](https://pjreddie.com/media/files/yolov3.weights) and yolov3-tiny [here](https://pjreddie.com/media/files/yolov3-tiny.weights) then save them to the weights folder.

  
### Saving your yolov3 weights as a TensorFlow model.
Load the weights using `load_weights.py` script. This will convert the yolov3 weights into TensorFlow .ckpt model files!

```
# yolov3
python load_weights.py

# yolov3-tiny
python load_weights.py --weights ./weights/yolov3-tiny.weights --output ./weights/yolov3-tiny.tf --tiny
```

After executing one of the above lines, you should see .tf files in your weights folder.


## Running just the TensorFlow model
The tensorflow model can also be run not using the APIs but through using `detect.py` script. 

Don't forget to set the IoU (Intersection over Union) and Confidence Thresholds within your yolov3-tf2/models.py file

### Usage examples
Let's run an example or two using sample images found within the data/images folder. 
```bash
# yolov3
python detect.py --images "data/images/dog.jpg, data/images/office.jpg"

# yolov3-tiny
python detect.py --weights ./weights/yolov3-tiny.tf --tiny --images "data/images/dog.jpg"

# webcam
python detect_video.py --video 0

# video file
python detect_video.py --video data/video/paris.mp4 --weights ./weights/yolov3-tiny.tf --tiny

# video file with output saved (can save webcam like this too)
python detect_video.py --video path_to_file.mp4 --output ./detections/output.avi
```
Then you can find the detections in the `detections` folder.
<br>

![demo](https://github.com/nimadorostkar/human-detection/blob/master/data/images/detection0.jpg)

![demo](https://github.com/nimadorostkar/human-detection/blob/master/data/images/detection1.jpg)

![demo](https://github.com/nimadorostkar/human-detection/blob/master/data/images/detection2.jpg)

<div>
