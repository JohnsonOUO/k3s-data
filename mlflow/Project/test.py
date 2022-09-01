import os
import mlflow
from mlflow import log_metric, log_param, log_artifact

if __name__ == "__main__":
    #mlflow.set_tracking_uri("http://10.20.0.109:31499")
    # Log a parameter (key-value pair)
    log_param("param1", 2.5)
    log_param("param2", 4)# Log a metric; metrics can be updated throughout the run
    log_metric("foo", 1)
    log_metric("foo", 2)
    log_metric("foo", 5)# Log an artifact (output file)
    with open("output1.txt", "w") as f:
        f.write("first file!")
    with open("output2.txt", "w") as f:
        f.write("second file!")
    log_artifact("output1.txt")
    log_artifact("output2.txt")
