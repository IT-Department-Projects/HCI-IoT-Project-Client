# Attendance Management System Client

## About

This is a project implemented in Python where the RPi is interfaced with the RPi camera module to send images to the main server for marking attendance for students. 

## Python Dependencies

* requests
* sleep

## Environment Setup

* It is preferable if you use Python Virtual Environment.
* Create a new conda environment using the following command:
```
virtualenv venv
```

* Activate the environment by running the following code:
```
source venv/bin/activate
```

* To install the required libraries, run the following commands:
```
pip install -r requirements.txt
```

## Working of the Project

* Create a folder called `data` and add all images that are needed to send to it! This can be used as an initial test step to send images to the server without having to use the RPi camera.  

* The basic usage is `python driver.py <server url> --detection 1` or `python client.py <server url> --recognition 1`.

## Contributors
The Project is created and maintained by 
* [Salman Shah](https://github.com/salman-bhai)
* [Aiman Abdullah](https://github.com/aimananees)
* [Rashika Chowlek](https://github.com/rashika)
* [Renu Chowdhury](https://github.com/RenuChowdhury)
* [Aniket Kumar](https://github.com/aniket)
