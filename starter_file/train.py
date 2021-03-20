from sklearn.linear_model import LogisticRegression
import argparse
import os
import numpy as np
from sklearn.metrics import mean_squared_error
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
import pandas as pd
from azureml.core.run import Run
from azureml.data.dataset_factory import TabularDatasetFactory

dataset_path = "https://raw.githubusercontent.com/claudiabringaseverett/nd00333-capstone/master/starter_file/heart.csv"
ds = TabularDatasetFactory.from_delimited_files(path = dataset_path)

x_df = data.to_pandas_dataframe().dropna()

run = Run.get_context()

y_df = x_df.pop("status")

# TODO: Split data into train and test sets.
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.3)

def main():
    # Add arguments to script
    parser = argparse.ArgumentParser()

    parser.add_argument('--C', type=float, default=1.0, help="Inverse of regularization strength. Smaller values cause stronger regularization")
    parser.add_argument('--max_iter', type=int, default=100, help="Maximum number of iterations to converge")

    args = parser.parse_args()

    run.log("Regularization Strength:", np.float(args.C))
    run.log("Max iterations:", np.int(args.max_iter))

    model = LogisticRegression(C=args.C, max_iter=args.max_iter).fit(x_train, y_train)

    accuracy = model.score(x_test, y_test)
    
    os.makedirs('outputs',exist_ok=True)
    
    joblib.dump(model, 'outputs/model.joblib')
    
    run.log("Accuracy", np.float(accuracy))

if __name__ == '__main__':
    main()
