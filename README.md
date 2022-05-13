
# AzurePipelineProject

# Overview

This project demostrates Azure CI/CD pipeline to build, test, and operationalize an ML API that makes housing price predictions in Boston based on a set of criteria. . The project utilizes Azure Web Apps to host the ML price predictions API, Github Actions for continuous integration (CI) and Azure Pipelines for continuous delivery (CD).

# Project Plan

Create below for the project plan:

Trello Task Board link :

https://trello.com/invite/b/m7Wq2VqH/6ef89351ce698a1d86ae6ade794fece8/devops

or

https://trello.com/b/m7Wq2VqH/devops

A link to a spreadsheet that includes the original and final project plan:

https://github.com/Suprajashetty/AzurePipelineProject/blob/main/project-management-template.xlsx

# Instructions

# Architectural Diagram

![image](https://user-images.githubusercontent.com/98746837/168204887-fccfe33d-36ea-4e06-81c6-2ec504bf9d8c.png)

# Azure Subscription and account

An Azure subscription will be needed in order to run this project. Make use of cloud lab already provided by udacity.

# Setup and Configure Azure Cloudshell

1. Log into the Azure Portal.
2. Click on the Azure Cloud Shell icon at the top
3. Select Bash/powershell on the Welcome to Azure Cloud Shell window.
4. Cloud Shell will be launched
5. At the Cloud Shell prompt, enter in the below command to create SSH key

ssh-keygen -t rsa

6. Click enter until you get ssh key.
7. At the Cloud Shell prompt, enter in the following command to get SSH key that was generated above

cat ./.ssh/id_rsa.pub

8. Copy the output of the command
9. Log into Github and create a new repository.
10. At the top right of the Github project click on the profile icon and select settings.
11. Click on SSH and GPG key.
12. Click on New SSH Key.
13. Paste the output of id_rsa.pub in the Key input box and give the key a title.
14. Click on Add SSH Key.

# Clone Github Project In Azure Cloud Shell

While logged into the Github go to the following url and copy the Github clone SSH command:

https://github.com/Suprajashetty/AzurePipelineProject

Open the Azure Cloud Shell and in the Cloud shell prompt, enter in the below command to clone the project

git clone https://github.com/Suprajashetty/AzurePipelineProject

cd to the folder clonned

![AzureClonningCloudShell](https://user-images.githubusercontent.com/98746837/168072500-151f51a1-8ca4-401f-bc0e-70ff0ddb9952.png)

# Create and run Makefile

Create the makefile which consists of all the coomand like install, test, lint and all.
Open the Azure Cloud Shell and navigate to the project directory. At the Cloud Shell prompt, enter in the following command:

make all

The following image displays the passing tests after running the make all command from the Makefile

![Makeall success](https://user-images.githubusercontent.com/98746837/168071766-b4d35f14-71aa-4472-a86a-773b0a4dd3ee.JPG)

# Test Run

The following image shows the output of a test run using the Github actions.

![githubActionBuild](https://user-images.githubusercontent.com/98746837/168072192-8d87918f-2052-4b16-a02d-c91011709427.JPG)

![githubActionBuild2](https://user-images.githubusercontent.com/98746837/168072208-b74be70a-2a56-4c59-ac58-4c470c13a274.JPG)

# Setup and Configure Azure App Service

Open the Azure Cloud Shell and navigate to the project directory. At the Cloud Shell prompt, enter in the following command:

az webapp up --name "cicdpipelinewebapp" --resource-group Azuredevops --runtime "PYTHON:3.7"

The command will return a url that can be used to verify that the Azure web app is functional.

![webapp create](https://user-images.githubusercontent.com/98746837/168072762-388888fd-3404-4502-ad0f-086a062bdd91.JPG)

Open a browser and go to the url. The following page should be seen which shows the project running:

![webapplaunch](https://user-images.githubusercontent.com/98746837/168072797-67f25523-9168-47e1-8d73-5029d5cdfa69.JPG)

# Azure Pipeline

Create an Azure Devops project and connect it to Azure using the following instructions:

https://docs.microsoft.com/en-us/azure/devops/pipelines/ecosystems/python-webapp?view=azure-devops#create-an-azure-devops-project-and-connect-to-azure

Create a Python python pipeline to deploy App Service using the following instructions:

https://docs.microsoft.com/en-us/azure/devops/pipelines/ecosystems/python-webapp?view=azure-devops#create-a-python-specific-pipeline-to-deploy-to-app-service

Execute the pipeline using the following instructions: 

https://docs.microsoft.com/en-us/azure/devops/pipelines/ecosystems/python-webapp?view=azure-devops#run-the-pipeline

Upon successful execution of the pipeline you should see a comparable output of the pipeline as shown in the image below:

![image](https://user-images.githubusercontent.com/98746837/168073237-f8017a2d-848e-4e1f-b48d-4e67b1cdce10.png)

Upon successful execution of the pipeline you will see that the pipeline automatically updates the Azure Web App with the code from the repository as shown in the image above

From the Azure portal you can also see that the Azure Web App is in a running state:
![image](https://user-images.githubusercontent.com/98746837/168073620-877ff1fc-1b1e-4281-a313-2d52cfef01ec.png)

# Using ML Flask App Predictions and logs

1. Open the Azure Cloud Shell.
2. Edit the make_predict_azure_app.sh file with the Cloud Shell visual studio editor.
3. Modify the url in  make_predict_azure_app.sh file by replacing the URL with the url provided by Azure WebApps.
4. Save the file and exit the editor.
5. At the Cloud Shell Prompt execute the following command:

./make_predict_azure_app.sh

6. The command will return back a prediction. The following image shows wthe output of the command:

![prediction](https://user-images.githubusercontent.com/98746837/168073962-fd344ed6-a627-46d1-9fd5-1ce57a664123.png)

# Azure WebApp Logs

To view the streamed Azure Web App Logs execute the following command:

az webapp log tail  or

https://cicdpipelinewebapp.scm.azurewebsites.net/api/logs/docker

The following images show the results of both streaming the webapp logs and going to the Azure logs directory for Azure Web Apps:

![log](https://user-images.githubusercontent.com/98746837/168074403-43db7849-97eb-4fdf-94b7-fe1a8a9a2f8f.JPG)

![log2](https://user-images.githubusercontent.com/98746837/168074449-153b91a7-58ac-45f1-8e26-1fbb2c47567a.JPG)

# Locust Performance Tests

Run command -

locust -f locustfile.py

![image](https://user-images.githubusercontent.com/98746837/168077107-94e467d9-f370-41a9-93e9-239f05971ba5.png)

# Status Badge

[![Python application test with Github Actions](https://github.com/Suprajashetty/AzurePipelineProject/actions/workflows/pythonapp.yml/badge.svg)](https://github.com/Suprajashetty/AzurePipelineProject/actions/workflows/pythonapp.yml)

# Enhancements

This project can be improved by:

1. Include more testing techniques like load testing to check the performance
2. Use more build jobs such as building Docker Images, building Kubernetes namespaces and clusters
3. Deploying the code on Kubernetes Cluster

# Demo

Yutube link : https://youtu.be/qdOr4Z8jT8M
