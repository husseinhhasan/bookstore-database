# Building and Deploying a Containerized Python Application with Flask and MongoDB on Azure Kubernetes Service (AKS)

## Overview
This project showcases the practical application of cloud computing by deploying a web application using Azure Kubernetes Service (AKS). The project specifically focuses on constructing a containerized Python application with Flask as the web framework and MongoDB for database management. By leveraging these technologies and configuring them appropriately, the project demonstrates the creation of a robust and scalable application.

## Project Participants
- Hussein Hasan - 2105026

## Project Scope
The scope of the project includes the following key aspects:
- Setting up Azure Cosmos DB for MongoDB and uploading data
- Developing a Python application for CRUD operations on the MongoDB database
- Containerizing the application using Docker
- Creating and configuring Azure Kubernetes Service (AKS)
- Deploying the application on AKS

## Project Steps
1. **MongoDB Setup**
   - Create an 'Azure Cosmos DB for MongoDB' resource on Azure Portal.
   - Upload the data (a book collection named bookstore) to the resource using MongoDB Compass Desktop application.

2. **Python Application**
   - Write a Python script to perform CRUD operations on the bookstore database.
   - Utilize Flask framework for web application development.
   - Create HTML and CSS files for the web interface.
   - Containerize the application using a Dockerfile.

3. **Azure Kubernetes Services (AKS)**
   - Create an 'Azure Kubernetes Service (AKS)' resource on Azure Portal with proper configurations.

4. **Application Deployment on AKS**
   - Create and apply the following YAML files:
     - `deployment.yaml`
     - `service.yaml`
     - `configmap.yaml`
   - Run commands to apply the app deployment on the cluster and configure it.

5. **Policy**
   - Create and apply a `policy.yaml` file to control access to the service.

## Accessing the Application
- The containerized Python application can be accessed through the following link when the Kubernetes service is running: [http://20.105.119.215/](http://20.105.119.215/)
- Alternatively, a local version of the app may be used by executing the attached Python script and following the link in the output.

## Results
A functional and containerized Python application with Flask framework and MongoDB instance was successfully created. The application manages a bookstore inventory, allowing users to perform CRUD operations through a practical interface.

