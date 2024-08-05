# Face-Landmarks-and-metrics-calculator

Welcome to the **Face Landmarks and Metrics Calculator** project! This tool calculates various facial metrics using a webcam or video file. It uses MediaPipe for facial landmark detection and OpenCV for image processing. 

## Contents

- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Setup and Usage](#setup-and-usage)
- [Example](#example)
- [Calibration](#calibration)

## Introduction

This project calculates various facial metrics using a webcam or video file. It leverages the MediaPipe library for facial landmark detection and OpenCV for image processing. The metrics calculated include:

1. **Distance between left eye and right eye**
2. **Face length**
3. **Forehead size**
4. **Size of the mouth**

You can choose which metric to calculate or opt to display only facial landmarks with connections.

## Features

- Real-time facial landmark detection
- Measurement of facial metrics in centimeters
- Option to display only facial landmarks and connections

## Requirements

- Python 3.x
- OpenCV
- MediaPipe

## Setup and Usage

**Project Structure**
- **camera_processing.py**: Contains the code for processing the camera feed and calculating metrics.
- **user_interaction.py**: Contains the code for user interaction and selecting the metrics to calculate.
- **main.py**: The main script that integrates user interaction with camera processing.

## Example
Here's an example of what happens when you run the application:

A. You will be prompted to select one of the following options:

1. Distance between left eye and right eye
2. Face length
3. Forehead size
4. Size of the mouth
5. Only display facial landmarks and connections

B. After selecting an option, the camera will start, and the selected metric(s) will be calculated and displayed in real-time.

## Calibration

To convert measurements from pixels to centimeters, you need to calibrate the pixel size. This is done by measuring a known reference object and adjusting the PIXEL_SIZE_CM value in camera_processing.py.




