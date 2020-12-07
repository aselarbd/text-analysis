FROM node:12.16.1-alpine as build

USER root
WORKDIR /frontend
COPY . /frontend/

RUN npm install --silent
RUN npm install react-scripts@3.0.1 -g --silent

RUN npm run build