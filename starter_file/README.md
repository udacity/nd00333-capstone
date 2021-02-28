# Heart Failure Prediction

This Capstone Project is the last project of the Azure Machine Learning nanodegree and I'm going to use the Heart Disease dataset to predict the disease. In this project, two models are created in the following way:
  1. First, Using AutoML model
  2. Then, using a customized model and tuning its hyperparameters with HyperDrive

After these steps are performed, we compare the performance of both models and deploy the best model. 

<hr/>

## TABLE OF CONTENTS
* [Project Set Up and Installation](#project-set-up-and-installation)
* [Projct Architecture](@project-architecture)
* [Dataset](#dataset)
  * [Overview](#overview)
  * [Task](#task)
  * [Access](#access)
* [Automated ML](#automated-ml)
  * [Results](#results)
* [Hyperparameter Tuning](#hyperparameter-tuning)
  * [Results](#results)
* [Model Deployment](#model-deployment)
* [Screen Recording](#screen-recording)
* [Standout Suggestions](standout-suggestions)
* [References](#references)
<hr/>

## Project Set Up and Installation
This project is done using Azure ML lab and a workspace was already provided to us. In order to start we need to do the following:
````
- Set up a compute instance, give it a name such `project-compute` with `STANDARD_DS3_V2` size.
- Create a ML compute cluster with `STANDARD_DS12_V2`, 1 minimun node and 6 maximum number of nodes.
````

## Dataset

### Overview
For this project, I am using the [Heart disease dataset](https://www.kaggle.com/ronitf/heart-disease-uci) from Kaggle. The term “heart disease” refers to several types of heart conditions. The most common type of heart disease in the United States is coronary artery disease (CAD), which affects the blood flow to the heart. Decreased blood flow can cause a heart attack. Sometimes heart disease may be “silent” and not diagnosed until a person experiences signs or symptoms of a heart attack, heart failure, or an arrhythmia. When these events happen, symptoms may include:

**Heart attack**: Chest pain or discomfort, upper back or neck pain, indigestion, heartburn, nausea or vomiting, extreme fatigue, upper body discomfort, dizziness, and shortness of breath.<br />
**Arrhythmia**: Fluttering feelings in the chest (palpitations).<br />
**Heart failure**: Shortness of breath, fatigue, or swelling of the feet, ankles, legs, abdomen, or neck veins.<br />

What are the risk factors for heart disease?
High blood pressure, high blood cholesterol, and smoking are key risk factors for heart disease. About half of Americans (47%) have at least one of these three risk factors. Several other medical conditions and lifestyle choices can also put people at a higher risk for heart disease, including:

- Diabetes
- Overweight and obesity
- Unhealthy diet
- Physical inactivity
- Excessive alcohol use

<p align="center">
<img src="heart1.png") /></p>
<p align="center">Figure 1. Heart Disease Information</p>


This database contains 76 attributes, but all published experiments refer to using a subset of 14 of them. In particular, the Cleveland database is the only one that has been used by ML researchers to this date. This is a classification problem, with input features as a variety of parameters, and the target variable DEATH_EVENT which is a binary variable, predicting whether heart disease is present or not (1=yes, 0=no). The input features along with meanings, measurement units, and intervals of each feature as described below:
````
Attribute information:

1.age
2.sex
3.chest pain type (4 values)
4.resting blood pressure
5.serum cholestoral in mg/dl
6.fasting blood sugar > 120 mg/dl
7.resting electrocardiographic results (values 0,1,2)
8.maximum heart rate achieved
9.exercise induced angina
10.oldpeak = ST depression induced by exercise relative to rest
11.the slope of the peak exercise ST segment
12.number of major vessels (0-3) colored by flourosopy
13.thal: 3 = normal; 6 = fixed defect; 7 = reversable defect
````

### Task
The goal of this project is to train the model to predict whether these individuals have Parkinson's disease or not.

### Access
I uploaded the .csv file into the repo for easy access. To access on Azure notebooks, we need to download it from an external link.
````
from azureml.data.dataset_factory import TabularDatasetFactory
dataset_path = "https://raw.githubusercontent.com/claudiabringaseverett/nd00333-capstone/master/starter_file/parkinsons.csv"
ds = TabularDatasetFactory.from_delimited_files(path = dataset_path)
````

## Automated ML
*TODO*: Give an overview of the `automl` settings and configuration you used for this experiment

### Results
*TODO*: What are the results you got with your automated ML model? What were the parameters of the model? How could you have improved it?

*TODO* Remeber to provide screenshots of the `RunDetails` widget as well as a screenshot of the best model trained with it's parameters.

## Hyperparameter Tuning
*TODO*: What kind of model did you choose for this experiment and why? Give an overview of the types of parameters and their ranges used for the hyperparameter search


### Results
*TODO*: What are the results you got with your model? What were the parameters of the model? How could you have improved it?

*TODO* Remeber to provide screenshots of the `RunDetails` widget as well as a screenshot of the best model trained with it's parameters.

## Model Deployment
*TODO*: Give an overview of the deployed model and instructions on how to query the endpoint with a sample input.

## Screen Recording
*TODO* Provide a link to a screen recording of the project in action. Remember that the screencast should demonstrate:
- A working model
- Demo of the deployed  model
- Demo of a sample request sent to the endpoint and its response

## Standout Suggestions
*TODO (Optional):* This is where you can provide information about any standout suggestions that you have attempted.

## References
Centers for Disease Control and Prevention. Underlying Cause of Death, 1999–2018. CDC WONDER Online Database. Atlanta, GA: Centers for Disease Control and Prevention; 2018. Accessed March 12, 2020.

Virani SS, Alonso A, Benjamin EJ, Bittencourt MS, Callaway CW, Carson AP, et al. Heart disease and stroke statistics—2020 update: a report from the American Heart Associationexternal icon. Circulation. 2020;141(9):e139–e596.

Figure 1. Fist Choice Neurology. https://www.healthcentral.com/condition/heart-disease



