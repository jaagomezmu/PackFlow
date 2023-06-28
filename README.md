# PackFlow
This repository contains a web app for package management and tracking using Django and Node.js. It includes models for customers, packages, and carriers, along with views, templates, and REST API endpoints for various functionalities. A comprehensive solution for efficient shipment tracking.

## Tree (Deep: 2 levels)

```
.  
├── challenges  
│   ├── fibonacci.py  
│   ├── lambda.py  
│   ├── lookup.py  
│   └── quicksort.py  
├── docker-compose.yml  
├── node-project  
│   ├── Dockerfile  
│   └── node_modules  
├── packflow  
│   ├── Dockerfile  
│   ├── logistics  
│   ├── manage.py  
│   ├── packflow  
│   ├── requirements.txt  
│   └── server-entrypoint.sh  
└── README.md  
  
6 directories, 11 files  
```

The repo consists of 6 directories and 11 files. Here's a brief explanation of each directory and its contents:

- `challenges`: This directory contains various Python files related to different coding challenges. The files included are:
  - `fibonacci.py`: Python script that calculates Fibonacci numbers.
  - `lambda.py`: Python script demonstrating the use of lambda functions.
  - `lookup.py`: Python script showcasing a lookup table implementation.
  - `quicksort.py`: Python script demonstrating a implementation of the QuickSort algorithm.

- `docker-compose.yml`: This file is a Docker Compose configuration file.

- `node-project`: This directory is related to a Node.js project and includes the following files:
  - `Dockerfile`: Dockerfile for building a Docker image for the Node.js project.
  - `node_modules`: Directory containing the dependencies installed for the Node.js project.

- `packflow`: This directory seems to be related to a project named "packflow" and includes the following files:
  - `Dockerfile`: Dockerfile for building a Docker image for the packflow project.
  - `logistics`: App containing logistics-related files.
  - `manage.py`: Python script serving as an entry point for the packflow project.
  - `packflow`: Directory related to the packflow project.
  - `requirements.txt`: File listing the required Python dependencies for the packflow project.
  - `server-entrypoint.sh`: Shell script serving as an entry point for the server.

- `README.md`: This file, the one you're currently reading, provides an overview of the project directory structure and its contents.

Feel free to explore the directories and files for more information about each component of the project.

## How to run The Django Server:

1. Setup postgres in your machine  
2. Create variables for database:  

```
sudo -u postgres psql
CREATE USER packflow_user WITH PASSWORD 'packflow_password';
CREATE DATABASE packflow_db OWNER packflow_user;
GRANT ALL PRIVILEGES ON DATABASE packflow_db TO packflow_user;
ALTER USER packflow_user CREATEDB;
\q
```

3. Create a new environment for python and install requeriments:  

```
python3 -m virtualenv venv # Install virtualenv module  
# Then, browse for manage.py file, at this level execute:  
python3 manage.py migrate
```
4. Run:

```
python manage.py runserver
```

## How to run the node server

1. Install npm in your machine, depends of your OS
2. Change to 'node-poject/'
3. Execute:

```
npm install express
```

4. Install dependencies

```
npm install
```

5. Run:

```
npm start
```

## Extras

- There are shell files to validate the operation of the application.    
- There are docker files to load images of the applications.  

## Comments
- I need a few more hours to finish configuring the compose, my machine betrayed me hahaha, things of life.  
- I made a return branch, to fix an error made on purpose to validate the task.   
