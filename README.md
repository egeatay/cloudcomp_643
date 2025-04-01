# Cloud Computing Framework

An image recognition pipeline in AWS, using two EC2 instances, S3, SQS, and Rekognition. 

Built using Python on Amazon Linux VMs.



## Sample diagram of the first framework:

![image](https://github.com/user-attachments/assets/91c82ae0-0d85-4d84-ba59-4882fa082d03)

 - Instance A reads images from an S3 bucket and performs object detection. 
 - When a car is detected using Rekognition, the index of that image is stored in SQS.
 - Instance B reads indexes of images from SQS as soon as posted, and performs text recognition on them using Rekognition.
 - The two instances work in parallel: while instance A is processing image 3, instance B can be processing previously posted image 1.
 - When instance A terminates its image processing, it adds a termination signal to the queue.
 - When instance B finishes, it prints the indexes of the images that have both cars and text along with the actual text.

# Parallel ML in EMR with Spark

A quality prediction ML model in Spark over AWS. The model is trained in parallel using 4 EC2 instances in EMR. The model is then saved to a file and inferenced on a separate singe EC2 instance.
