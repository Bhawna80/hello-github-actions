import os
import requests
import urllib.request
import json
import time
import re

necessary_inputs = ["TFE_URL","TFE_USER_TOKEN","WORKSPACE_ID"]

tfe_url = os.getenv("TFE_URL", None)
tfe_token = os.getenv("TFE_TOKEN", None)
workspace_id = os.getenv("WORKSPACE_ID", None)

tfe_http_auth_headers = {'Authorization': 'Bearer '+tfe_token +''}
tfe_http_headers = {"Authorization": "Bearer "+tfe_token +"", "Content-Type": "application/vnd.api+json"}

workspace_settings_request = request.request("GET", tfe_url +'/api/v2/workspaces/'+workspace_id, headers=tfe_http_headers)
worspace_json=workspace_settings_request.json()

if "2" in str(workspace_settings_request.status_code):
  workspace_name = workspace_json['data']['attributes']['name']
  print("\n[INFO] Workspace data obtained for: "+ workspace_name)
else:
  print("ERRORRRRRR")

workspace = worspace_json['data']

