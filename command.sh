git clone git@github.com:Suprajashetty/AzurePipelineProject.git

python -m venv ~/.flask-ml-azure
source ~/.flask-ml-azure/bin/activate

az webapp up -n cicdpipelinewebapp

az webapp log tail --resource-group Azuredevops --name cicdpipelinewebapp