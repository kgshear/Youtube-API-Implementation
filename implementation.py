# what are you looking for?
# 1. channel
#  "title"
# description
# viewCount
# subscriberCount
# videoCount
#2. video
# what video would you like? (give keyword)
    # return search result
    # get video id from first search result
    # return information about video
    # tags
#     channel title
# description
# default audio langiage
# viewCount
# likeCount
# commentCount

# -*- coding: utf-8 -*-

# Sample Python code for youtube.videos.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/code-samples#python

import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import goo

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

def get_info():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "YOUR_CLIENT_SECRET_FILE.json"

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    request = youtube.videos().list(
        part="snippet,contentDetails,statistics",
        id="Ks-_Mh1QhMc"
    )
    response = request.execute()

    print(response)

if __name__ == "__main__":
    main()



if __name__ == '__main__':
    print("What sort of resource would you like to get?")
    print("1. Channel")
    print("2. Video")
    resource_type = input("Type here:")
    print("-----------------------------------------")

    if (resource_type==1):
        channel_name = input("Alright! What Channel are you looking for?")
        print("Got it! What do you want to know about the channel?")
        print("1. Description")
        print("2. Amount of Views")
        print("3. Amount of Subscribers")
        print("4. Amount of Videos")
        channel_stat = input("Type here:")
        print("-----------------------------------------")
    elif resource_type == 2:
        video_name = input("Alright! What video are you looking for?")
        print("Got it! What do you want to know about the video?")
        print("1. Description")
        print("2. Amount of Views")
        print("3. Amount of Likes")
        print("4. Amount of Comments")
        print("5. Date Published")
        print("6. Channel Name")
        video_stat = input("Type here:")
        print("-----------------------------------------")





