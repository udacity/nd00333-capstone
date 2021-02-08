# HR Analytics: Job Change of Data Scientists

This project is designed to predict whether an employee will leave the current job for a new company. For this, two models will be created using Azure ML:
1. Using AutoML to get the best algorithm
2. Using Logistic Regression and tuning the parameters using HyperDrive.
The best model will then be deployed using Azure Container Instance which can later be consumed using REST Api.

## Project Set Up and Installation
The project requires access to AzureML Studio.

Steps to be followed:
1.Using  the dataset provided in this repository, create a new dataset in the Azure ML studio in default Blob Storage.
2. Create a new compute target.
2.Import the notebooks attached in this repository in the Notebooks section in Azure ML studio.
3.Run the autoML and hyperdrive notebooks using the details given in the notebooks.
4.Run endpoint.py file to consume the endpoint created and get back the predicted results.

## Dataset

The dataset is taken from kaggle : "https://www.kaggle.com/arashnic/hr-analytics-job-change-of-data-scientists".

The task is to predict whether the employee will leave the current job or not, based on the following factors-

1. enrollee_id : Unique ID for candidate
2. city: City code
3. city_ development _index : Developement index of the city (scaled)
4. gender: Gender of candidate
5. relevent_experience: Relevant experience of candidate
6. enrolled_university: Type of University course enrolled if any
7. education_level: Education level of candidate
8. major_discipline :Education major discipline of candidate
9. experience: Candidate total experience in years
10. company_size: No of employees in current employer's company
11. company_type : Type of current employer
12. lastnewjob: Difference in years between previous job and current job
13. training_hours: training hours completed
14. target: 0 – Not looking for job change, 1 – Looking for a job change

### Accessing the Data
The data can be accessed by downloading the data into local server and then uploading it to Dataset subsection of Microsoft AzureML.

//////////////////////////////////////////////dataaa

## Automated ML

Automated Machine Learning is the process of automating the time-consuming, iterative tasks of ML model development. It allows to build the models with high scale efficiency & productivity all while sustaining the model quality. In case of classification problem, many models such as XGBoost, RandomForest, StackEnsemble, VotingEnsemble etc. are compared

AutoML Configuration used for this project:
1. The task is Binary classification, hence we use 'accuracy' as primary metric.
2. Cross validation of 6 folds is choosen, as it gave better accuracy than 3 or 4 fold.
3. Iterations are processed concurrently so as to speed up our training time.
4. Early stopping is enabled to prevent overfitting.
5. Experiment timeout is set to be 30 minutes.
6. Featurization parameter is set to be "auto" for auto feature scaling.

### Results
After comparing 37 algorithms, the Best model obtained is Voting Ensemble with an Accuracy of 80.17%

The screenshot of the details of various algorithms is shown below:
//////////////////////////////////////////////////////////////1.aml

Best Run model-ID and accuracy, along with other parameters:
///////////////////////////////////////////////////////////////2.aml
//////////////////////////////////////////////////////////////////////////3.aml


The model can be imporved by increasing the number of iterations or trying for various cross-validation folds.
Deep learning/neural network based classification can also be used for better results.


## Hyperparameter Tuning
Since the problem involved Binary classification, Logistic Regression has been used as it is simple to train and works well as compared to other complex algorithms.
The two parameters: '--C' (Inverse of regularization strength. Smaller values cause stronger regularization) and '--max_iter' (Maximum number of iterations to converge) are selected for tuning using HyperDrive.
- The choice used for C are (0.001, 0.01, 0.1, 1, 10, 100, 200), while that for max iterations are (50,100,150,200,250,300).


### Results
Here's the screenshot of best results and optimized parameters obtained using HyperDrive:
/////////////////////////////1.hdrun
Rundetails Widget:
/////////2.hdrundetails
///////////////////////////////////////3.hdrundetails


## Model Deployment
The model choosen with AutoML is choosen for deployment:
Azure Container Instance is used for deployment of the model as webservice.
The details for method of deployment can be found in automl.ipynb under Model Deployment section.

The number of cpu cores and memory for the web service has been set to 1 and 1GB respectively.

We can see the deployment state set as healthy below, stating that model has deployed successfully. This model can now be consumed using REST Api by sending HTTP requests to it.
/////////////////////////1.deployment
/////////////////////////////////////2.deployment

y.Now we can consume the endpoint using scoring URL genereated after deployment.
The sample input to the endpoint is as below. This can also be found in endpoint.py file of the repository.
//////////////////////////////////////////////////////////////endpoint

### Result
///////////////finalres

## Screen Recording
Here's a link of Screencast demonstrating the consuming of the Deployed model: https://1drv.ms/u/s!Avt8pJRrCCqEhmNaZOPPxJfcpQlh?e=8Y7BYf
