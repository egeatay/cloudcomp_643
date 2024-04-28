import boto3
import os


qurl = "https://sqs.us-east-1.amazonaws.com/339712835019/proj.fifo"
tbw = ""

s3          = boto3.client("s3", region_name="us-east-1")
sqs         = boto3.client("sqs", region_name="us-east-1")
rekognition = boto3.client("rekognition", region_name="us-east-1")



def s3load(key, dir):
    s3.download_file("njit-cs-643", key, dir)

def getq():
    response = sqs.receive_message(
        QueueUrl=qurl,
        MaxNumberOfMessages=10
    )
    return response

def gettext(dir):
    with open(dir, "rb") as f:
        return rekognition.detect_text(Image={"Bytes": f.read()})



list = [item["Body"] for item in getq()["Messages"]]

os.makedirs("images", exist_ok=True)

for key in list:
    if key == "-1":
        break
    localdir = os.path.join("images", os.path.basename(key))
    s3load(key, localdir)
    response = gettext(localdir)

    if len(response['TextDetections']) > 1:
        currenttexts = [text['DetectedText'] for text in response['TextDetections']]
        tbw += "\nfile " + key + " has both a car and text. The text contains: " + str(currenttexts) + "\n"

f = open("output.txt", "w")
f.write(tbw + "\n")
f.close()

print("all done")
