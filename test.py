import mlflow
print("Printing tracking URI scheme:", mlflow.get_tracking_uri())

mlflow.set_tracking_uri("http://127.0.0.1:5000")
print("\nPrinting new tracking URI scheme:", mlflow.get_tracking_uri())
