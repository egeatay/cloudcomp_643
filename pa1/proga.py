import boto3
import os


qurl = "https://sqs.us-east-1.amazonaws.com/339712835019/proj.fifo"
thresholdnum = 90
iter = 0


s3          = boto3.client("s3", region_name="us-east-1")
sqs         = boto3.client("sqs", region_name="us-east-1")
rekognition = boto3.client("rekognition", region_name="us-east-1")


def getlist():
    objects = s3.list_objects(Bucket="njit-cs-643", Prefix="")
    return objects.get("Contents", [])

def s3load(key, dir):
    dir = os.path.join("images", os.path.basename(key))
    s3.download_file("njit-cs-643", key, dir)

def getlabels(dir):
    with open(dir, "rb") as f:
        return rekognition.detect_labels(Image={"Bytes": f.read()})

def filter(response):
    for label in response["Labels"]:
        if label["Name"] == "Car":
            return label["Confidence"] > thresholdnum
    return False

def push(msg, id):
    response = sqs.send_message(
        QueueUrl=qurl,
        MessageBody=f"{msg}",
        MessageDeduplicationId=f"{id}",
        MessageGroupId=f"{id}"
    )



os.makedirs("images", exist_ok=True)

for image in getlist():
    key = image["Key"]
    localdir = os.path.join("images", os.path.basename(key))
    s3load(key, localdir)
    response = getlabels(localdir)
    if filter(response):
        push(key, iter)
        iter += 1

push("-1", iter+1)
print("all done")
