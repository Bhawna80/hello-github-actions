import os
import requests
import urllib.request
import json
import time
import re

necessary_inputs = ["TFE_URL","TFE_USER_TOKEN"]#,"WORKSPACE_ID"]

tfe_url = 'https://app.terraform.io'
#os.getenv("TFE_URL", None)
print(tfe_url)

tfe_token = 'xJH8KojiPJa3JA.atlasv1.10cyO6tl61Dhty7zuzKUijBhwa6ZOWDrL2yQWR7kCw1YPnhHL0aDbCiwT1fJqkyhg0w'
#tfe_token = os.getenv("TFE_TOKEN", None)
print(tfe_token)

#workspace_id = os.getenv("WORKSPACE_ID", None)
#print(workspace_id)

org_org='bhawna_tf'
print(org_org)

#tfe_http_auth_headers = {'Authorization': 'Bearer '+tfe_token +''}

tfe_http_headers = {"Authorization": "Bearer "+tfe_token +"", "Content-Type": "application/vnd.api+json"}
print("before api call")
request = requests.request("GET", tfe_url+'/api/v2/organizations/'+org_org+'/workspaces',headers=tfe_http_headers)
#workspace = request.json()
#workspace_settings_request = request.request("GET", tfe_url +'/api/v2/workspaces/'+workspace_id, headers=tfe_http_headers)
#worspace_json=workspace_settings_request.json()
print("post api call")
print(request.status_code)

workspace_list=""

if "2" in str(request.status_code):
  request_text = request.text
  data = json.loads(request_text)
  data_serialized= json.dump(data, open('data.json',"w"))
  myjsonfile=open('data.json','r')
  jsondata=myjsonfile.read()
  obj=json.loads(jsondata)
  workspace_list=obj['data']
  print(workspace_list)
  print(len(workspace_list))
else:
  print("ERRRRROR")

print("workspace_list:::")
print(workspace_list)
for workspace in range(len(workspace_list)):
  print("inside")
  print(workspace)
  print(workspace_list[0])
  print(workspace_list[workspace])
  org_workspace_id = workspace_list[workspace].get["id"]
  print("org_workspace_id: "+org_workspace_id)
  print("before 2nd call")
  org_workspace_settings_request = requests.request("GET", tfe_url +'/api/v2/workspaces/'+workspace_id, headers=tfe_http_headers)
  print("post call")
  org_workspace_json = org_workspace_settings_request.json()
  print(org_workspace_settings_request.status_code)

  if "2" in str(org_workspace_settings_request.status_code):
    org_workspace_name=org_workspace_json['data']['attributes']['name']
    print("org_workspace_name: "+org_workspace_name)
  else:
    print("ERRRRROR2")

#workspace = worspace_json['data']

