#!/bin/bash

# Specify the full path to the Docker executable
DOCKER=$(which docker)

# Copy the directory from the container to the local machine
$DOCKER cp my_bd_a1_container:/home/doc-bd-a1/service-result/ "E:/NU CS/Spring - 2024 Courses/CSCI 461 Introduction to Big Data/Assignment 1 CSCI461/test final"

# Stop the container
$DOCKER stop my_bd_a1_container
