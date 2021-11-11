# Wine-Project:
 


![main_page](/static/img/index_background.jpg)  


## wine quality builder
Wine quality refers to the factors that go into producing a wine, as well as the indicators or characteristics that tell you if the wine is of high quality. The wine industry is investing in new technologies for both wine making and selling processes. Wine certification and quality assessment are key elements within this context. Quality evaluation is often part of the certification process and can be used to improve wine making (by identifying the most influential factors) and to stratify wines such as premium brands (useful for setting prices). When you know what influences and signifies wine quality, you’ll be in a better position to make good purchases. In our project we will focus on the prediction of wine quality using machine Learning Models (supervised and unsupervised learning).
We leveraged data from two datasets, related to red and white variants of the "Vinho Verde" wine, from the north of Portugal. 
In our datasets, there is 1599 observation for the red wine and 4898 for the white wine. In each dataset there are 12 variables: fixed acidity, volatile acidity, citric acid, residual sugar chlorides, free sulfur dioxide, total sulfur dioxide, density, pH, sulphates, alcohol %, quality. We used Tableau for the visualizations and correlation analysis of those features.
In our models we analyzed the effects of selected features based on physicochemical (input) variables by using Random Forest Classifier. We build two models: for red wine and white wine to predict the quality score of the wine (output variable). The model assumes that for the good quality wine (as a Good Choice from our model) the score is 6 and higher (from scale 1 to 10). We also used KMeans model, with PCA on the red wine dataset and visualized the clusters.
In addition, we tried to build a model for prediction of the quality based on the wine price, variety and country of origin. Our prediction comes with   % accuracy.
## Data Sources
•	https://archive.ics.uci.edu/ml/datasets/Wine+Quality (winequality-red.csv, winequality-white.csv) (P. Cortez, A. Cerdeira, F. Almeida, T. Matos and J. Reis.) Modeling wine preferences by data mining from physicochemical properties. In Decision Support Systems, Elsevier, 47(4):547-553, 2009.)
•	Bonus: https://www.kaggle.com/christopheiv/winemagdata130k Use selected variables from this data set (price, region, country...), to build the machine learning model to be able to predict quality of wine.
## Data ETL, EDA and Visualization
Data from both datasets were loaded into jupyter notebook and ETL process was performed to identify possible missing values and inconsistencies in our data.
We decided to use Tableau for further exploration of those datasets. All twelve variables in two datasets were considered for correlation analysis and visualization to identify features which correlate the most with the quality. 

## White Wine Visualizations


 
Using box and whisper charts we compared each physiochemical percentage against the quality of wine. The quality ranged from 1-9 ( 9 being the best quality rating), and looked at the amount of a specific type a chemical in the quality rating.  The chemicals with the greatest amount of outliers were fixed acidity, chlorides, and citric acid.  This can tell that the lower the quality of wine, the greater amount of these particular chemicals we can find.


![image](https://user-images.githubusercontent.com/83027069/141357625-d95719db-1cfa-440f-8ac0-a66b497a4f97.png)

 


The scatter plots above measure each amount of a specific physiochemical in relation to the amount of alcohol based on the quality of the wine.  The greater the alcohol content is, the greater the chemical content appears to be.  For example, the greater the quality of wine is, the more alcohol and less sugar it has.

![image](https://user-images.githubusercontent.com/83027069/141357716-5498d017-1e4f-4c0b-a7a8-c19d02b0a854.png)


The graph below shows the content percentage of fixed acidity, sulphate, sugar, and alcohol ranging from high amounts to low amounts based on the quality.  The lower the quality of wine, the higher sugar and acid amounts.  This is an indication that the better quality of alcohol, the more expensive it is thus using more sulphates and less sugar.  More expensive wine is usually not very sweet and contains a very high alcohol percentage.


![White Wine per content % Dashboard](https://user-images.githubusercontent.com/83027069/141358951-98653b4c-a055-42f7-b381-9283d1195474.png)


## Red Wine Visualizations

The first Dashboard describes various parameters which defines quality of red wine. The quality of red wine is categorized as strong, medium and light on the basis of alcohol content and various parameters responsible in defining the quality as Strong, Medium and Light.

<img width="1055" src="https://user-images.githubusercontent.com/81253160/141364906-1240357e-24a1-4dce-b1c0-5d07bde01c0d.png">


Second Dashboard defines the Quality of Red Wine on various chemical parameters and their correlation with quality.

<img width="1055" src="https://user-images.githubusercontent.com/81253160/141365162-c353022b-d99f-4a4c-9e9d-effeea4e6cc0.png">


-Less significance in defining quality of Red wine:- Fixed Acidity, Chlorides, Citric Acid, Density, PH, Volatile Acidity.
-More significance in defining quality of Red wine :- Alcohol percentage, Free sulfur Dioxide, Residual sugar,  sulphates, Total Sulfur Dioxide.


Third Dashboard is a pie representation of the dataset which defines that we have more strong wine quality data and less light quality data. When you hover over the graph, you can see the parameters and their content in various type of quality.

<img width="1055"  src="https://user-images.githubusercontent.com/81253160/141365394-28986866-ee8e-45d6-b74d-b307143a6cf7.png">

Last Dashboard is quality defining over alcohol percentage. Quality is the dependent variable and is other factors are independent variable which are responsible for defining the quality of red wine as strong, medium and light. 

<img width="1080" src="https://user-images.githubusercontent.com/81253160/141365561-cd2042f0-294b-4880-983f-b4414928adbd.png">

In tableau quality is defined as strong, medium and light which relates to good quality and bad quality in machine learning model.

I found out that some parameters which has lower significance in overall quality of red wine has high significance in defining strong quality of like PH which has a high significance in strong quality of red wine


## Machine Learning
Our clean data from both datasets were used to build up two separate models – for red wine and white wine to predict the quality of the wine. We decided to use LogisticRegression Model first to get overview of our predictions. With accuracy about 74% from this model we decided to build additional models. With all 11 variables as an input these models performed as follows:

- White Wine Dataset:

Model: KNeighborsClassifier

Train score: 0.8448135039477267
Test Score: 0.7665306122448979

Model: RandomForestClassifier

Train score: 1.0
Test Score: 0.8375510204081633

Model: ExtraTreesClassifier

Train score: 1.0
Test Score: 0.8318367346938775

Model: AdaBoostClassifier

Train score: 0.7854614756329975
Test Score: 0.7648979591836734

Model: SVC

Train score: 0.8126871766947998
Test Score: 0.7787755102040816

- Red Wine Dataset:

Model: KNeighborsClassifier

Train score: 0.8198498748957465 
Test Score: 0.7025 

Model: RandomForestClassifier 

Train score: 1.0 
Test Score: 0.81 

Model: ExtraTreesClassifier

Train score: 1.0 
Test Score: 0.8125 

Model: AdaBoostClassifier 

Train score: 0.8006672226855713 
Test Score: 0.75 

Model: SVC

Train score: 0.8023352793994996
Test Score: 0.76


The models did a good job in achieving decent accuracy scores. Based on our results we decided to use RandomForest Classifier, where the accuracy to predict quality of the wine was 83% for the white wines dataset and 81% for the red wine dataset. For each model we applied feature importance calculation to choose which of the features of our data are most helpful towards our goal – faster training, interpretability and also to help to validate the relevant variables for our models. Then we selected the top N most important features using selection mechanism (SelectFromModel).

### Feature importance for datasets:

- White wine:

 ![features](/static/img/white_wines_features.png)
 
-  Red Wine:
 
 ![features](/static/img/red_wine_features.png) 



The selection method derived from our models the most important features, which we used in the next step to build another model to predict quality of wines.
For the white wines four features were selected: alcohol, volatile acidity, density and free sulfur dioxide, for red wines five features were selected: alcohol, sulphates, volatile acidity, total sulfur dioxide and density.
On our website, we accept the selected features as an input for each model and the selection is uploaded and ran through machine learning models. The quality output as a “Good Choice” predict that the wine will be within a good quality range, and on the other end ”...there are better wines” output indicate that predicted quality is below the range for good wines.  

### K-means Model
In our K-means model we used the data about the red wine and tried to predict similar clusters based on 12 variables (fixed acidity, volatile acidity, citric acid, residual sugar chlorides, free sulfur dioxide, total sulfur dioxide, density, pH, sulphates, alcohol %, quality).
We performed dimensionality reduction using PCA method. The reduced data was used as an input for our K-means Model.
The number of groups is represented by K. One of the most challenging tasks in this clustering algorithm is to choose the right values of K. We used Elbow method to identify the right value for K. K -means clustering aims to converge on an optimal set of cluster centers - centroids. The results with clusters and centroids are showed in our K-means graph.
The k-means graph shows clusters been created by associating every observation with the mean closest to it. The centroids marked by X becomes the new mean of each cluster.

 ### Bonus: World Wines Model

We wanted to tackle the data about world wines from Kaggle, and try to build a model which could give the quality output based on the price of the wine, country of origin and variety of the wine. Those are information the consumers are usually considering before they choose a wine to buy. So, what will be the quality of the wine, can we predict the good quality of the wine based on our model?

The dataset originally contains information 129,971 wines. After ETL process, we keep data about 84,881 wines, with selected columns for country, price and variety as an input variables and points as an output variable. Points were in the range from 80 to 100, and there were transform to binary classification, with 0 value for range below 85.7 and 1 and a good quality for the range from 85.7 to 100 (based on the distribution of the data).
For the price information was necessary to use bins (price range was from $4.00 - $3,300.00), as for the final input for the machine learning model.
Data about 33 wine’s varieties from 7 countries are used for the model to predict the quality in RandomForest Classifier Model, which works with 73% accuracy to predict the quality of the wine.  



## Technologies

* Python (Flask, Json, Matplotlib, Numpy, Pandas, Seaborn, Sklearn)
* JavaScript (D3)
* HTML/ CSS (Bootstrap)
* Tableau
* Heroku



## Project Outline

1. Shuchi  - ETL: Extract Data from : csv files, json,Excel files
2. Dasa/Tinu/Joshua - Use Pandas Jupyter Notebook for data preprocessing and selection of 
the features for input to machine learning models
3. Dasa/Joshua/Tinuola - Machine Learning : we plan to use LinearRegression, 
RandomForestClassifier, Deep Neural to train models and evaluate 
models using testing data to choose the model with highest 
performance score 
4. Melissa/Dasa/Joshua - HTML/CSS : build up webpage with user data selection based on our features 
5. Shuchi/Megan - Tableau: – visualization :( Red Wine Visualizations - Shuchi, White Wine Visualizations - Megan)
6. Dasa/Joshua/Melissa - Flask
7. Megan - Heroku 


## Heroku Website Deployment

https://wine-quality-testing.herokuapp.com/index.html

## Team Members
* Melissa Diep
* Shuchi Khandelwal
* Megan Butler
* Tinuola Adepoju
* Joshua Pohl
* Dasa Simo
