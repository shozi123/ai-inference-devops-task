#!/bin/bash

while true
do
    docker ps | grep ai-inference || docker run -d -p 8000:8000 ai-inference
    sleep 10
done
