import requests
import csv
import pandas as pd
group_name = "KPMG-UK/teams/ie-gcp"
access_token = "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"

url = f"https://api.github.com/orgs/{group_name}/repos"
headers = {"Authorization": f"Bearer {access_token}"}

repos = []
page = 1

while True:
    response = requests.get(url, headers=headers, params={"page": page})
    if response.status_code == 200:
        new_repos = response.json()
        if len(new_repos) == 0:
            break
        else:
            repos.extend(new_repos)
            page += 1
    else:
        print("Error retrieving repositories:", response.text)
        break

print(f"Retrieved {len(repos)} repositories:")
# for repo in repos:
    # print(repo["name"])

# writing all the repos to a csv file

'''with open("List_repos.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Description", "URL"])

    for repo in repos:
        writer.writerow([repo["name"], repo["description"], repo["html_url"]])
'''
#writing to excel file using pandas 

# Create a DataFrame to store the repo data
data = {"Name": [], "Description": [], "Language": []}
for repo in repos:
    data["Name"].append(repo['name'])
    data["Description"].append(repo['description'])
    data["Language"].append(repo['language'])
    # data["Stars"].append(repo['stargazers_count'])
    # data["Forks"].append(repo['forks_count'])

df = pd.DataFrame(data)

# Write the DataFrame to an Excel file
with pd.ExcelWriter("repos_list.xlsx") as writer:
    df.to_excel(writer, index=False)