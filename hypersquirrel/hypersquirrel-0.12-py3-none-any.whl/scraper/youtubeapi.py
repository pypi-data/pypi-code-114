from os import environ

import requests


def get_external_id(htmltext: str):
    split = htmltext.split("channel_id=")
    if len(split) > 1:
        return split[1].split('"')[0]
    return None


def get_defacto_upload_id(external_id: str):
    return "UU" + external_id.lstrip("UC")


def get_upload_id(external_id):
    url = "https://www.googleapis.com/youtube/v3/channels"
    body = requests.get(url, params={
        "part": "contentDetails",
        "id": external_id,
        "key": environ.get("YOUTUBE_APIKEY")
    }).json()

    return body["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]


def get_all_videos(upload_id: str):
    url = "https://www.googleapis.com/youtube/v3/playlistItems"
    params = {
        "playlistId": upload_id,
        "key": environ.get("YOUTUBE_APIKEY"),
        "part": "snippet",
        "maxResults": 50
    }

    while True:
        body = requests.get(url, params=params).json()

        for item in body["items"]:
            snippet = item["snippet"]
            video_id = snippet["resourceId"]["videoId"]
            yield {
                "fileid": video_id,
                "filename": snippet["title"],
                "sourceurl": f"https://youtube.com/watch/{video_id}",
                "thumbnailurl": snippet["thumbnails"]["medium"]["url"]
            }

        next_page_token = body.get("nextPageToken")

        if not next_page_token:
            break

        params["pageToken"] = next_page_token


def scrape_youtubeapi(url):
    r = requests.get(url)
    external_id = get_external_id(r.text)
    upload_id = get_defacto_upload_id(external_id)
    yield from get_all_videos(upload_id)
