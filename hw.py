print("this file launches to check TestDataset.csv on the same directory \n \
      if this file doesnt exist it must be added \
      the \" characters in the file must be erased and whitespace characters replaced with _ character \
      to test functionality without this file run load.py\
      functionality of load.py was tested on AWS with 0.58 accuracy on validation")

from pyspark.ml.tuning import CrossValidatorModel
from pyspark.ml import PipelineModel
from pyspark.sql.functions import col, round
from pyspark.sql.types import IntegerType, FloatType

#this file launches to check TestDataset.csv on the same directory
# if this file doesnt exist it must be added
# to test functionality without this file run load.py



from pyspark.sql import SparkSession
spark = SparkSession.builder \
    .appName("Classification Models") \
    .getOrCreate()
validation_data = spark.read.csv("ValidationDataset2.csv", header=True, inferSchema=True, sep=";")

from pyspark.ml.feature import VectorAssembler
vector_assembler = VectorAssembler(inputCols=validation_data.columns[:-1], outputCol="features")  
validation_data = vector_assembler.transform(validation_data)


from pyspark.ml.classification import LogisticRegressionModel

from pathlib import Path
lr = LogisticRegressionModel.load(str(Path.cwd()) + "/save2/lr")
## Fit the pipeline to new data
lr_predictions = lr.transform(validation_data)



from pyspark.ml.evaluation import MulticlassClassificationEvaluator
evaluator = MulticlassClassificationEvaluator(labelCol="quality", metricName="accuracy")
lr_accuracy = evaluator.evaluate(lr_predictions)
print("Logistic Regression Accuracy:", lr_accuracy)