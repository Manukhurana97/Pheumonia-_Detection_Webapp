# Pheumonia-_Detection_Webapp
Pneumonia Detection WebApp


![alt text](https://github.com/Manukhurana97/Pheumonia-_Detection_Webapp/blob/master/Output.png)
![alt text](https://github.com/Manukhurana97/Pheumonia-_Detection_Webapp/blob/master/output1.png)


# Overview
This is a simple classification app built on flask(Frontend) and Keras(Backend) .  
The webapp is used to detect Pneumonia Using Deep Learning model.
This model is created by using Inception_V3.


# Technial Aspect
This project is divided into 2 parts 
  1) Training : For training i have used Neural network model to detect the pheumonia.
  2) User end: Flask is used to create the usedend and connect with the NN model.


# Details
This contain the code file with the name pheum
[a link](https://github.com/Manukhurana97/Pheumonia-_Detection_Webapp/blob/master/Pneumonia.ipynb)

###I have used google colab to to train the model.
This code file contain 4 different models .
1) Vgg19
2) Inception V3
3) ResNet 50
4) Manual NN model.


# Dataset
The dataset is Avaliable on Kaggle( https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia/ )


# Technology Used

![](https://forthebadge.com/images/badges/made-with-python.svg)

[<img target="_blank" src="https://keras.io/img/logo.png" width=200>](https://keras.io/) [<img target="_blank" src="https://flask.palletsprojects.com/en/1.1.x/_images/flask-logo.png" width=170>](https://flask.palletsprojects.com/en/1.1.x/) 




## Directory Tree 
```
├── app 
│   ├── __init__.py
│   ├── main.py
│   ├── model
│   ├── static
│   └── templates
│   └── Pneumonia.ipynb
├── config
│   ├── __init__.py
├── processing
│   ├── __init__.py
├── LICENSE
├── README.md
└── wsgi.py
```

# License


Copyright 2020 Manu khurana

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
