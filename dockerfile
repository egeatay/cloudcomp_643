#FROM python:3.9.16
#CMD [ "python3", "demo.py"]

FROM python:3.9.16

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install numpy, py4j, and pyspark
RUN pip install numpy==1.26.4 py4j==0.10.9.7 pyspark==3.5.1

# Run demo.py when the container launches
CMD ["python", "hw.py"]


#Downloading numpy-1.26.4-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (18.2 MB)
#Successfully installed numpy-1.26.4


#Downloading pyspark-3.5.1.tar.gz (317.0 MB)
#Collecting py4j==0.10.9.7
  #Downloading py4j-0.10.9.7-py2.py3-none-any.whl (200 kB)

  #Successfully installed py4j-0.10.9.7 pyspark-3.5.1

