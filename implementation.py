
import os


import googleapiclient.discovery
import googleapiclient.errors

channel_stat_dict = {"STOP":"", "1":"Description", "2" : "Amount of Views", "3":"Amount of Subscribers",
                             "4": "Amount of Videos"}
vid_stat_dict = {"STOP":"", "1":"Description", "2" : "Amount of Views", "3": "Amount of Likes",
                         "4": "Amount of Comments", "5":"Channel Name", "6":"Video Name"}

def connect_to_api():

    api_service_name = "youtube"

    # the API key necessary to access or change information on youtubes API
    api_key = "AIzaSyDPn22Y3OFLECSg7hiNh92UaTOUaaLGUUw"
    api_version = "v3"

    # creating api client to connect to
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=api_key)
    return youtube


def search_youtube(api_build, keywords, is_channel):
    # setting up HTTPS search for some keyword

    # narrowing search results to one type
    if is_channel:
        search_type = "channel"
    else:
        search_type = "video"
    request = api_build.search().list(
        part="snippet",
        maxResults=1,
        q=keywords,
        type=search_type
    )

    # sending HTTPS request and getting response
    response = request.execute()
    search_id = ""

    # parsing the response for information
    for item in response["items"]:
        if is_channel and item['id']['kind']=="youtube#channel":
            search_id = item['id']['channelId']
        elif not is_channel and item['id']["kind"]=="youtube#video":
            search_id = item["id"]["videoId"]
        else:
            pass

    if search_id:
        return search_id
    else:
        print("No results matching this keyword")
        return None


def get_vid_stats(api_build, vid_id):

    request = api_build.videos().list(
        part="snippet,contentDetails,statistics",
        id=vid_id)

    response = request.execute()

    end_lookup=False

    while not end_lookup:
        print("Select an information type. Type STOP to end.")
        stat_type = input("Type here:")

        while stat_type not in vid_stat_dict:
            print("Stat invalid. Try again")
            stat_type = input("Type here:")

        print("-----------------------------------------")
        my_stat = ""

        if stat_type=="1":
            my_stat = response["items"][0]["snippet"]["description"]
        elif stat_type=="2":
            my_stat = response["items"][0]["statistics"]["viewCount"]
        elif stat_type=="3":
            my_stat = response["items"][0]["statistics"]["likeCount"]
        elif stat_type=="4":
            my_stat = response["items"][0]["statistics"]["commentCount"]
        elif stat_type=="5":
            my_stat = response["items"][0]["snippet"]["channelTitle"]
        elif stat_type=="6":
            my_stat = response["items"][0]["snippet"]["title"]
        elif stat_type== "STOP":
            print("Done retrieving stats")
            end_lookup = True
        else:
            print("Invalid Statistic Type. Retry.", stat_type)
        if my_stat:
            print(f"The {vid_stat_dict[stat_type]} for {video_name} is {my_stat}")



def get_channel_stats(api_build, channel_id):
    request = api_build.channels().list(
        part="snippet,statistics",
        id=channel_id,
        maxResults=1
    )
    response = request.execute()

    end_lookup = False

    while not end_lookup:
        print("Select an information type. Type STOP to end.")
        stat_type = input("Type here:")

        while stat_type not in channel_stat_dict:
            print("Stat invalid. Try again")
            stat_type = input("Type here:")

        print("-----------------------------------------")
        my_stat = ""

        if stat_type == "1":
            my_stat = response["items"][0]["snippet"]["description"]

        elif stat_type == "2":
            my_stat = response["items"][0]["statistics"]["viewCount"]

        elif stat_type == "3":
            my_stat = response["items"][0]["statistics"]["subscriberCount"]

        elif stat_type == "4":
            my_stat = response["items"][0]["statistics"]["videoCount"]
        elif stat_type == "STOP":
            print("Done retrieving stats")
            end_lookup = True
        else:
            print("Invalid Statistic Type. Retry.")
        if my_stat:
            print(f"The {channel_stat_dict[stat_type]} for {channel_name} is {my_stat}")


if __name__ == '__main__':
    build = connect_to_api()

    print("What sort of resource would you like to get?")
    print("1. Channel")
    print("2. Video")
    resource_type = input("Type here:")
    while resource_type != "1" and resource_type != "2":
        print("Invalid resource type. Try again")
        resource_type = input("Type here:")
    print("-----------------------------------------")

    if resource_type=="1":

        channel_name = input("Alright! What Channel are you looking for?")
        print("Got it! What do you want to know about the channel?")
        print("1. Description")
        print("2. Amount of Views")
        print("3. Amount of Subscribers")
        print("4. Amount of Videos")
        channel_id = search_youtube(build, channel_name, True)
        if channel_id:

            get_channel_stats(build, channel_id)
        else:
            print("Unable to retrieve channel data. Try again.")


    elif resource_type == "2":
        video_name = input("Alright! What video are you looking for?")
        print("Got it! What do you want to know about the video?")
        print("1. Description")
        print("2. Amount of Views")
        print("3. Amount of Likes")
        print("4. Amount of Comments")
        print("5. Channel Name")
        print("6. Video Name")
        vid_id = search_youtube(build, video_name, False)
        if vid_id:
            get_vid_stats(build, vid_id)
        else:
            print("Unable to retrieve video data. Try again.")

