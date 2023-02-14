import socket
import sys
import requests
import json
import plotly

request_url = "https://www.mediawiki.org/w/api.php?action=query&format=json&prop=revisions&list=allrevisions&meta=siteinfo&continue=&titles=Main%20Page&formatversion=2&rvprop=user%7Ccomment&arvlimit=50&arvdir=newer"

response = requests.get(request_url)
response_json = response.json() # This method is convenient when the API returns JSON
json_formatted_str = json.dumps(response_json, indent=2)

revisions = []

class Revision:
    def __init__(self, timestamps: list, users: list, comments: list):
        self.timestamps = timestamps
        self.users = users
        self.comments = comments


def parse_revisions():

    for page in enumerate(response_json["query"]["allrevisions"]):
        print("Page: ", page[1]["title"])
        
        count = 0

        timestamps = []
        users = []
        comments = []

        for rev in page[1]["revisions"]:
            count += 1
            timestamps.append(rev["timestamp"])
            users.append(rev["user"])
            comments.append("comment")

        print("Number of revisions: ", count, "\n")
    
        revision = Revision(timestamps, users, comments)
        revisions.append(revision)

parse_revisions()

print("Number of total revisions: ", len(revisions))