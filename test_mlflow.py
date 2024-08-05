from mlflow import log_metric,log_param,log_artifact


# # mlflow ui


if __name__ == '__main__':
    log_param("threshold", 3)
    log_param("verbosity","DEBUG")

    # basically saving information that can be usefull for the model

    log_metric("timestamp",10000)
    log_metric("TTC", 33)

    # we ca log an artifact

    # log_artifact("reduces_dataset.csv")

# from mlflow import 