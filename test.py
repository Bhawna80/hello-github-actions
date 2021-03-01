import os
import requests
import urllib.request
import json
import time
import re

necessary_inputs = ["TFE_URL","TFE_USER_TOKEN"]#,"WORKSPACE_ID"]

tfe_url = os.getenv("TFE_URL", None)
print(tfe_url)
tfe_token = os.getenv("TFE_TOKEN", None)
print(tfe_token)

#workspace_id = os.getenv("WORKSPACE_ID", None)
#print(workspace_id)

org_org='bhawna_tf'
print(org_org)

#tfe_http_auth_headers = {'Authorization': 'Bearer '+tfe_token +''}

tfe_http_headers = {"Authorization": "Bearer "+tfe_token +"", "Content-Type": "application/vnd.api+json"}

request = requests.request("GET", tfe_url+'/api/v2/organizations/'+org_org+'/workspaces',headers=tfe_http_headers)
#workspace = request.json()
#workspace_settings_request = request.request("GET", tfe_url +'/api/v2/workspaces/'+workspace_id, headers=tfe_http_headers)
#worspace_json=workspace_settings_request.json()
print("before api call")

if "2" in str(request.status_code):
  request_test = request.text
  data = json.loads(request_text)
  data_serialized= json.dump(data, open('data.json',"w"))
  myjsonfile=open('data.json','r')
  jsondata=myjsonfile.read()
  obj=json.loads(jsondata)
  worksepace_list=obj['data']

else:
  print("ERRRRROR")

#for workspace in range(len(workspace_list)):
  #org_workspace_id = workspace_list[workspace].get["id"]
  
  
#else:
  #print("ERRORRRRRR")

#workspace = worspace_json['data']

