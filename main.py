import pyterprise
import requests
import time
import csv

tfe_token = 'xJH8KojiPJa3JA.atlasv1.10cyO6tl61Dhty7zuzKUijBhwa6ZOWDrL2yQWR7kCw1YPnhHL0aDbCiwT1fJqkyhg0w'
client = pyterprise.Client()
print(client)

# Supply your token as a parameter and the url for the terraform enterprise server.
# If you are not self hosting, use the one provided by hashicorp.
client.init(token=tfe_token, url='https://app.terraform.io/api/v2/organizations/bhawma_tf/workspaces')
print(client)

workspaces = client.list_workspace_ids('bhawna_tf')

# Set the organization
# org = client.set_organization(id='bhawna_tf')

#org = client.get_organization('bhawna_tf')
#print(org)

#workspace = org.get_workspace('hello-github-actions_dev')
print(workspaces)
# Get a list of all workspace objects in an organization.
#for workspace in org.list_workspaces():
    #print(workspace)

# Print some workspace attributes. Additionally you can access all attributes 
# as a dictionary by printing  the 'workspace' object at top level.                     
# print(org.name, workspace.name, workspace.id, workspace.created_at)
