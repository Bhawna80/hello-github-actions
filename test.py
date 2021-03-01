import os
import requests
import urllib.request
import json
import time
import re

necessary_inputs = ["TFE_URL","TFE_USER_TOKEN"]#,"WORKSPACE_ID"]
org_list=["bhawna_db","mydb_tf"]

tfe_url = 'https://app.terraform.io'
#os.getenv("TFE_URL", None)
print(tfe_url)

tfe_token = 'xJH8KojiPJa3JA.atlasv1.10cyO6tl61Dhty7zuzKUijBhwa6ZOWDrL2yQWR7kCw1YPnhHL0aDbCiwT1fJqkyhg0w'
#tfe_token = os.getenv("TFE_TOKEN", None)
print(tfe_token)

#workspace_id = os.getenv("WORKSPACE_ID", None)
#print(workspace_id)

#org_org='bhawna_tf'
#print(org_org)
workspace_list=""
workspace_list2=""


tfe_http_headers = {"Authorization": "Bearer "+tfe_token +"", "Content-Type": "application/vnd.api+json"}

for org in range(len(org_list)):
  print(org_list[org])
  request = requests.request("GET", tfe_url+'/api/v2/organizations/'+org_list[org]+'/workspaces',headers=tfe_http_headers)
  if "2" in str(request.status_code):
    request_text = request.text
    data = json.loads(request_text)
    data_serialized= json.dump(data, open('data.json',"w"))
    myjsonfile=open('data.json','r')
    jsondata=myjsonfile.read()
    obj=json.loads(jsondata)
    workspace_list=obj['data']
    print("Workspace List is:" )
    print(workspace_list)
  else:
    print("ERRRRROR")


for workspace in range(len(workspace_list)):
  org_workspace_id = workspace_list[workspace].get('id')
  print("Workspace Id: "+org_workspace_id)
  org_workspace_settings_request = requests.request("GET", tfe_url +'/api/v2/workspaces/'+org_workspace_id, headers=tfe_http_headers)
  org_workspace_json = org_workspace_settings_request.json()
  if "2" in str(org_workspace_settings_request.status_code):
    org_workspace_name=org_workspace_json['data']['attributes']['name']
    workspace_terraform_version=org_workspace_json['data']['attributes']['terraform-version']
    print("Workspace Name: "+org_workspace_name)
    print("Workspace Terraform Version: "+workspace_terraform_version)
  else:
    print("ERRRRROR2")
