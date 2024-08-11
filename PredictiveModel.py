import polars as pl
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from DataExtraction import GetSalesData
from DataProcessing import ProcessData

def BuildAndTrainModel():
    # ETL
    salesDataFrame = GetSalesData()
    processedDataFrame = ProcessData(salesDataFrame)

    # Prepare
    features = processedDataFrame.select(['TotalAmount']).to_pandas()
    target = features['TotalAmount']
    features = features[['TotalAmount']]
    
    XTrain, XTest, YTrain, YTest = train_test_split(features, target, test_size=0.2, random_state=42)
    
    # Training
    model = LinearRegression()
    model.fit(XTrain, YTrain)
    
    # Predict
    predictions = model.predict(XTest)
    
    # test
    meanSquaredErrorValue = mean_squared_error(YTest, predictions)
    print(f"Mean Squared Error: {meanSquaredErrorValue}")

if __name__ == "__main__":
    BuildAndTrainModel()
