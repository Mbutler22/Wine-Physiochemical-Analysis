# Wine-Project:
 

## Project Overview

We will leverage data from two datasets, related to red and white variants of the "Vinho Verde" wine, from the north of Portugal. The goal is to model wine quality based on physicochemical tests (e.g. fixed acidity,	volatile, acidity,	citric acid,	residual sugar	chlorides,	free sulfur dioxide,	total sulfur dioxide,	density,	pH,	sulphates,	alcohol	%, quality) by using various Machine Learning Models.  
As mentioned in the resource, there are only physicochemical (inputs) and sensory (the output) variables available (e.g., there is no data about grape types, wine brand, wine selling price, etc.).
We will try to use models to select most relevant variables by testing feature selection methods.

## Data Sources
We will leverage data from two datasets, related to red and white variants of the "Vinho Verde" wine, from the north of Portugal. The goal is to model wine quality based on physicochemical tests using various Machine Learning Models.
As mentioned in the resource, there are only physicochemical (inputs) and sensory (the output) variables available (e.g., there is no data about grape types, wine brand, wine selling price, etc.). We will try to use models to select most relevant variables by testing feature selection methods.

## Data Sources

* https://archive.ics.uci.edu/ml/datasets/Wine+Quality (winequality-red.csv, winequality-white.csv)
(P. Cortez, A. Cerdeira, F. Almeida, T. Matos and J. Reis.)
Modeling wine preferences by data mining from physicochemical properties. In Decision Support Systems, 
Elsevier, 47(4):547-553, 2009.)
* Optional: https://www.kaggle.com/christopheiv/winemagdata130k
Use selected variables from this data set (price, region, country...), to build the machine learning model to 
be able to predict quality of wine.

## White Wine Visualizations


 
Using box and whisper charts we compared each physiochemical percentage against the quality of wine. The quality ranged from 1-9 ( 9 being the best quality rating), and looked at the amount of a specific type a chemical in the quality rating.  The chemicals with the greatest amount of outliers were fixed acidity, chlorides, and citric acid.  This can tell that the lower the quality of wine, the greater amount of these particular chemicals we can find.


![image](https://user-images.githubusercontent.com/83027069/141357625-d95719db-1cfa-440f-8ac0-a66b497a4f97.png)

 


The scatter plots above measure each amount of a specific physiochemical in relation to the amount of alcohol based on the quality of the wine.  The greater the alcohol content is, the greater the chemical content appears to be.  For example, the greater the quality of wine is, the more alcohol and less sugar it has.

![image](https://user-images.githubusercontent.com/83027069/141357716-5498d017-1e4f-4c0b-a7a8-c19d02b0a854.png)



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
