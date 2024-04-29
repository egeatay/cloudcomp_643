from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.classification import LogisticRegression, RandomForestClassifier
from pyspark.ml.evaluation import MulticlassClassificationEvaluator

# Create SparkSession
spark = SparkSession.builder \
    .appName("Classification Models") \
    .getOrCreate()

# Read  data
training_data = spark.read.csv("TrainingDataset2.csv", header=True, inferSchema=True, sep=";")
validation_data = spark.read.csv("ValidationDataset2.csv", header=True, inferSchema=True, sep=";")


feature_cols = training_data.columns[:-1]  # Exclude target

vector_assembler = VectorAssembler(inputCols=feature_cols, outputCol="features")
training_data = vector_assembler.transform(training_data)
validation_data = vector_assembler.transform(validation_data)


# Logistic Regression
lr = LogisticRegression(featuresCol="features", labelCol="quality")
lr_model = lr.fit(training_data)
lr_trainingdata = lr_model.transform(training_data)
lr_predictions = lr_model.transform(validation_data)
# Random Forest Classifier
rfc = RandomForestClassifier(featuresCol="features", labelCol="quality")
rfc_model = rfc.fit(training_data)
rfc_trainingdata = rfc_model.transform(training_data)
rfc_predictions = rfc_model.transform(validation_data)


# Evaluate models
evaluator = MulticlassClassificationEvaluator(labelCol="quality", metricName="accuracy")
lr_tr_accuracy = evaluator.evaluate(lr_trainingdata)
print("Logistic Regression Training Accuracy:", lr_tr_accuracy)
lr_accuracy = evaluator.evaluate(lr_predictions)
print("Logistic Regression Accuracy:", lr_accuracy)
rfc_tr_accuracy = evaluator.evaluate(rfc_trainingdata)
print("Random Forest Classifier Training Accuracy:", rfc_tr_accuracy)
rfc_accuracy = evaluator.evaluate(rfc_predictions)
print("Random Forest Classifier Accuracy:", rfc_accuracy)

#lr_model.save("/home/hadoop/saves")
lr_model.save("/home/hadoop/save2/lr")
rfc_model.save("/home/hadoop/save2/rfc")
spark.stop()
