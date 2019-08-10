# API Project

API for Recommendation system

## Docker

### Development

- Use GitBash to run these commands below 

```
cd docker
docker build -t project3/computer-vision-api:0.1 .
docker run -d -p 5000:5000 project3/computer-vision-api:0.1



### Usage

- Download the docker image from Docker Hub

```
docker pull project3/computer-vision-api:0.1
docker run -d -p 5000:5000 project3/computer-vision-api:0.1
#curl localhost:5000/top_trend
```
