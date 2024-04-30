# cloud steps

# how to create an AWS program that uses Spark to train an ML model and runs a program to see its accuracy

Log in to AWS

Create a new EMR cluster (with hadoop and spark) with 1 master node and 4 task EC2 nodes

SSH into the EMR cluster primary node

Upload the training and validation files

Install pyspark and numpy with pip

Write the pyspark code for training and save the model on a folder.
Run this code so the model is trained in parallel on the 4 ec2 nodes of the cluster

Write the pyspark code for loading the model and running on the given file
Run this code

