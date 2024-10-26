# Component of machine learning pipeline

## 1. Data Ingestion: 
        taking data from different sources to ingest in the system. like cloud, api, datawarehouse
        1. Split dataset for train and test
        1. train , validation( used from dataingestion to model training) and test( to be used only in model training step.- want to create realistic scenario for model testing. coz when we deploy our model, in real world, it does not have any information about the dataset that will be used for prediction.)

## 2. Data Validation: 
        2.1 Schema Validation
            2.1.1: Filename
            2.1.2: data type validation
            2.1.3: Column name 
            2.1.4: number of column the file has
            2.1.5: null check
            2.1.6: duplicate data 
            2.1.7: outliers/anomalies #outlier is one kind of anomaly.
            2.1.8: imbalance data check
            2.1.9: Data Range
            2.1.10: Domain value eg. categorical data ie. Gender : max to max male, female and others -- some other value --came 
                                     it should be the expected value. 


            2.1.9: Data Drift #when old statistics is not matching to new dataset statistics -- data distribution has become different now.
            what is statistics: used for summarising the data , to know the distribution. 

## 3. EDA:
        Perfom EDA to understand the data.

## 4. Data Transformation/Feature Enginerring(Transformation to get ready for modelling): (use jupyter notebook)
      1. one hot encoding
      2. Standard Scaling
      3. Min-max scalar
      4. Custom Trnasformation

      Output: pickle object of feature engineering.

      test dataset is also passed here. 
      Tranform function

## 5. Model Training (jupyter notebook)
     1. Hyperparameter tuning
     2. Model selection (on the based of accuracy.)
     3. Model comparison(xgboost vs random forest)

     Output: pickle object of model training.


## 6. Model Evaluation
        1. Test Dataset for model evaluation 
        2. Model comparison (model already in production/real-time ie. called Base model vs newly trained model)
        minimum expectation shuld be achieved that newly trained model should be 3% more accurate the one in production model.

## 7. Push Model
      Replace the production model with newly trained model 



Prediction Pipeline


Real world dataset -> pickle object of feature engineering transform function -> transfomed dataset -> pickle object of model training -> predict function -> prediction
        

      