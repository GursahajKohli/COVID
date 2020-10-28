# COVID Prediction Web APP

Coronavirus disease 2019 (COVID-19) is a contagious respiratory and vascular disease. 
It is caused by becoming infected with severe acute respiratory syndrome coronavirus 2, which is a specific type of coronavirus. 
Common symptoms include fever, cough, fatigue, shortness of breath or breathing difficulties, and loss of smell and taste.

![Corona Virus](https://img.theweek.in/content/dam/week/news/health/images/2020/1/1/COVID-19-Virus-Structure-Diagram-Coronavirus-SARS-CoV-2019-nCoV-virus-sheme-sliced-model-RNA-shut.jpg)

This project is divided in two stages:
1. First stage deals with visualization of cases across the globe, from the day it started till today.
2. Second stage of our project deals with estimating if a patient has COVID or not, depending on his chest X-ray.

![COVID Spread across the globe](https://scitechdaily.com/images/COVID-19-Coronavirus-Map-March-19.jpg)

# Objective

Objective of this project is as follows:
1. First to see the number of cases at a particular point of time around the globe. 
That can be visualized through a timeline graph that can be dragged to any particular date to see the intensity of the cases of any country around the globe.

2. Next, we can ask the user to see if the patient is having COVID or not by uploading his chest X-ray. 
The deep learning model based on convolutional neural network will help us predict if the patient suffers from the COVID disease or not.

# Implementation

**1. Implementation for visualizing the cases**

This web app is used to visualize the cases happening through the world.
This shows how, when and which country was affected by what number in the period of time
We used plotly express to represent this information
The intensity of the cases can be seen by the intensity of the color and the color scale depicting the range of the cases. We can also see the cases by hovering the cursor.
When we hover the pointer, we can get the exact number of cases of that country on the exact date on which we want from the timeline.
The working can be seen in the GitHub link

![Working of Visualization](https://github.com/GursahajKohli/COVID/blob/master/Covid_Prediction_App/ezgif.com-gif-maker%20(3).gif)


**2. Implementation of COVID Detection through chest X-ray images**

Using CNN, we devised a method in which we were able to detect if the patient was covid positive or not, by scanning the chest X-ray
We got an accuracy of 97-98% on our deep learning model
Although it was a good accuracy, but still it **can’t be treated as a diagnostic model** as it may leave some essential points that must be considered but are not detected by the model.

![Detection of cases](https://github.com/GursahajKohli/COVID/blob/master/Covid_Prediction_App/ezgif.com-gif-maker%20(4).gif)

# Results

1. We were able to visualize the World map implementation and we could see that how the color on various countries first grew very dark and then later on lightened that showed the inclination and declination of the cases with time, which can be seen in the screenshot as well.

2. Secondly, while predicting if the patient is COVID positive or COVID negative, we were able to achieve an accuracy of 97-98% which is a tremendous result as by this we assure that majority of the results would be what the patient’s actual state is.
We even tested our model on certain images that were not included in our training model and not even tested in our test set, but still got amazing results for it.



