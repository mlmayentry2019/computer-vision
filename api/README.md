# API Project

API for Recommendation system

## Docker

### Development

- Use GitBash to run these commands below 

```
docker build -t hoanglt705/computer-vision-api:0.1 .
docker run -d -p 5000:5000 hoanglt705/computer-vision-api:0.1


### Usage

- Download the docker image from Docker Hub

```
docker pull hoanglt705/computer-vision-api:0.1
docker run -d -p 5000:5000 hoanglt705/computer-vision-api:0.1
curl X POST -F 'image=@tomato.jpg' http://localhost:5000/image/predict
```
