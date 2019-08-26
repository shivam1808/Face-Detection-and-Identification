# Face-Detection-and-Identifiaction
Detect and Identify faces using Python with the help of some libraries provided by python i.e., opencv2, pillow, pickle etc.
Download the database for images :
https://drive.google.com/open?id=1Z2njbjPumD84iFTfl58V8GhNTi_q9EV7

<img src="https://s3-us-west-2.amazonaws.com/static.pyimagesearch.com/opencv-face-recognition/opencv_face_reco_animation.gif" alt="alt text" align="middle"/>

In this project, you will learn how to use OpenCV to perform face recognition. To build our face recognition system, we’ll first perform face detection, extract face from the frame, train a face recognition model, and then finally recognize faces in both images and video streams with OpenCV.

# Project structure
Once you’ve grabbed the zip from the “Downloads” section of this post, go ahead and unzip the archive and navigate into the directory.

Here are quite a few moving parts for this project — take the time now to carefully read this section so you become familiar with all the files in today’s project.

Our project has two directories and four files in the root folder:</br>

cascades/ : Contains harcasscade file. </br>
images/ : Contains several test images that we’ll use to verify the operation of our model.</br>

How to use:</br>
Step 1: Input images in the images folder.</br>
Step 2: Run Face-Train.py file to create trainer for new images and labels.pickle file.</br>
Step 3: Run Face_Recognition.py file.
