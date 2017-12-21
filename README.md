![Origae-6](doc/origae-6.png)
# AI Eyes
This is a project to understand video contents from more than one 4K (at least 4K) cameras. The default live environment is based on ubuntu 16.04(x86_64) and all source codes are developed on macos 10.13.2(x86_64).

## Features
- [x] able to detect camera installed locally.
- [ ] able to register a camera remotely.
- [x] able to download video from internet.
- [x] able to lable video contents manually.
- [ ] able to train video with various algorithms.
- [x] able to detect video contents.
- [x] able to identify video contents.
- [ ] able to classify video contents.
- [ ] able to segment video contents.
- [ ] able to trace the people's pose.
- [ ] able to verify the result.
- [ ] more functionalities.

## Source Codes Structure
- 1-detect-local-camera.py: this is to demonstrate how to invoke a local video camera.
- 2-download-internet-video.py: this is to demonstrate how to leverage youtube-dl to download online video streams into local files.
- 3-label-images: this is an open source tools to label image and generate label json file. After pip install labelme, type labelme to try it.
- 4-find-faces.py: this is to demonstrate how to use dlib to detect faces, identify object. All test images are local.
- 5-find-faces-from-camera.py: this is to demonstrate how to use dlib to detect and identify object in video in a real-time manner.
- 6-find-faces-from-videofiles.py: the same demonstration as 5-find-faces-from camera.py but the input source is from video files in order to have rich testing data.
- 7-opencv and 7-opencv_contrib: basic framework opencv.
- 8-youtube-dl: basic framework youtube and other video downloader.
- 9-dlib: basic framework of object detection and identification.
- 10-openpose: basic framework of people movement tracking.
- 11-nvcaffe and 11-digits: NVIDIA video training platform with caffe/tensorflow/pytorch.
- 12-darknet: light-wieght c framework for real-time object identification without any other framework. Even though it works fine with opencv or openmp or cudnn or cuda.
- 13-ffmpeg: 
- aieyes: the main system project. all kinds of integration can be found here.
- doc: some documents and images and pdf files to support AIEyes.

## Installations
I just recorded what I have done with my Macbook Pro as a reference and you need to take care of your case.
1. reinstall MacOS 10.13.2 in order to have a clean OS. (if you would like follow this installation steps, this is a must-do.)
2. install Homebrew.
```bash
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
echo "export PATH=/usr/local/bin:$PATH" >> ~/.bash_profile
source ~/.bash_profile
```
3. install python2 and python3 with brew and use virtualenv as python version isolation tool. I don't use anaconda or other stuff.
```bash
brew install python
brew install python3
brew link python
brew linkapps python3
# Install virtual environment
pip install virtualenv virtualenvwrapper
echo "# Virtual Environment Wrapper"
echo "VIRTUALENVWRAPPER_PYTHON=/usr/local/bin/python2" >> ~/.bash_profile
echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.bash_profile
source ~/.bash_profile
  
############ For Python 2 ############
# Create virtual environment
mkvirtualenv facecourse-py2 -p python2
workon facecourse-py2
  
# Now install python libraries within this virtual environment
pip install numpy scipy matplotlib scikit-image scikit-learn ipython pandas
  
# Quit virtual environment
deactivate
######################################
  
############ For Python 3 ############
# Create virtual environment
mkvirtualenv facecourse-py3 -p python3
workon facecourse-py3
  
# Now install python libraries within this virtual environment
pip install numpy scipy matplotlib scikit-image scikit-learn ipython pandas
  
# Quit virtual environment
deactivate
######################################
```
4. install opencv. Before that you need to install Xcode. 
```bash
sudo xcodebuild -license
sudo xcode-select --install
brew tap homebrew/science
brew info opencv
brew install opencv --with-contrib --with-python3 --HEAD
cd /usr/local/Cellar/python3/3.6.3/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages
cp cv2.cpython-36m-darwin.so ~/.virtualenvs/yourproject/python3.6/lib/site-packages/
pip3 install numpy
```
5. install youtube downloader.
```bash
sudo -H pip install --upgrade youtube-dl
```
6. install labelme via the following commands.Before that install docker following the official website installation guide. Then you could label a picture manually.
```bash
source py3.6.3/bin/activate
brew install qt || brew install pyqt  # qt4 is deprecated
pip install PyQt5
pip install labelme
```
7. install face_recognition and models. Before that, install dlib please.
```bash
pip install face_recognition
pip install face-recognition-models
```
8. install nvcaffe based on [installation guide](doc/BuildCaffe.md). 
## How to run
```bash
python3 -m digits
```