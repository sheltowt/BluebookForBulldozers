import pandas as pd

valid = pd.read_csv("/home/play/Example/Kaggle/Bull/Data/Valid.csv")
appendix = pd.read_csv("/home/play/Example/Kaggle/Bull/Data/Machine_Appendix.csv")

valid1 = valid.drop(['ModelID', 'fiModelDesc', 'fiBaseModel', 'fiSecondaryDesc', 'fiModelSeries', 'fiModelDescriptor', 'fiProductClassDesc', 'ProductGroup', 'ProductGroupDesc'], axis=1)



valid1.to_csv("valid_revised.csv")


Machine_Appendix.csv  random_forest_benchmark1000.csv  random_forest_benchmark.csv  train_appendix_reduced.csv  valid_columns_dropped.csv
mean_benchmark.csv    random_forest_benchmark100.csv   train_appendix.csv           Train.csv                   Valid.csv
play@BigDataR in ~/Example/Kaggle/Bull/Data$

 new = pd.merge(valid1, appendix, on='MachineID', how='left')

valid_processed_last3_10.csv

train_appendix_reduced.csv
