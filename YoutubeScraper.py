from googleapiclient.discovery import build
import csv

class YoutubeScraper:
    def __init__(self, api_key, ids) -> None:
        self.ids = ids
        self.api_key = api_key
        self.youtube = build('youtube', 'v3', developerKey=api_key)

    def get_channel_stats(self, id):
        if not self.isHandle(id):
            request = self.youtube.channels().list(
            part='snippet,contentDetails,statistics,brandingSettings,topicDetails',
            id=id
            )
        else:
            request = self.youtube.channels().list(
            part='snippet,contentDetails,statistics,brandingSettings,topicDetails',
            forHandle=id
            )
        response = request.execute()
        
        # Check if response contains 'items' and is not empty
        if 'items' in response and response['items']:
            for item in response['items']:
                stats = {
                    'title': item['snippet']['title'],
                    'view_count': item['statistics']['viewCount'],
                    'subscriber_count': item['statistics']['subscriberCount'],
                    'video_count': item['statistics']['videoCount']
                }
                return stats
        else:
            print(f"No data found for channel Handle/ID: {id}")
            return None
    
    def print_responses(self):
        for id in self.ids:
            response = self.get_channel_stats(id)
            for item in response['items']:
                print(item['statistics'])
                print(item['snippet'])

    def isHandle(self, id):
        return id[0] == "@"
    
    def write_to_csv(self, fileName):
        with open(fileName, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Title', 'View Count', 'Subscriber Count', 'Video Count'])

            for channel_id in self.ids:
                data = self.get_channel_stats(channel_id)
                if data:
                    try:
                        writer.writerow([data['title'], data['view_count'], data['subscriber_count'], data['video_count']])
                    except:
                        print("Error writing line to csv")

        print(f"Data written to {fileName}")

        
'''

Response Form
{
    'kind': 'youtube#channelListResponse', 
    'etag': 'PsIHtpl9K616T5ldfHLoaXFuWsY', 
    'pageInfo': {'totalResults': 1, 'resultsPerPage': 5}, 
    'items': [
        {
        'kind': 'youtube#channel', 
        'etag': '0FgPnbM_DNMEAv1r0AAarBrxGQc', 
        'id': 'UC5c9VlYTSvBSCaoMu_GI6gQ', 
        'snippet': 
            {
                'title': 'Total Gaming', 
                'description': "Hi Gamers,  I'm AJAY! Here you will see me playing PC games and Mobile Games having some fun.\n\nI Playing Free Fire, Call Of Duty Mobile, Pubg And GTA 5 With You On Total Gaming Channel.\n\nFully Indian Gamer With Hindi Commentary.\n\nYoutube Started 2 December 2018.\n\nBusiness Email: business@totalgaming.in\n\nFor Contact: Join My Discord :- http://bit.ly/totalgamingdiscprd",
                'customUrl': '@totalgaming093', 
                'publishedAt': '2018-10-09T18:21:53Z', 
                'thumbnails': { 
                    'default': {
                        'url': 'https://yt3.ggpht.com/ytc/AIf8zZSS262qsZXYQwuo2ajP-JCp_5XSPJ9_NorTenliGg=s88-c-k-c0x00ffffff-no-rj', 
                        'width': 88, 'height': 88
                        }, 
                    'medium': {
                        'url': 'https://yt3.ggpht.com/ytc/AIf8zZSS262qsZXYQwuo2ajP-JCp_5XSPJ9_NorTenliGg=s240-c-k-c0x00ffffff-no-rj', 
                        'width': 240, 
                        'height': 240
                        }, 
                    'high': {
                        'url':'https://yt3.ggpht.com/ytc/AIf8zZSS262qsZXYQwuo2ajP-JCp_5XSPJ9_NorTenliGg=s800-c-k-c0x00ffffff-no-rj', 
                        'width': 800, 'height': 800}
                        }, 
                    'localized': {
                        'title': 'Total Gaming', 
                        'description': "Hi Gamers,  I'm AJAY! Here you will see me playing PC games and Mobile Games having some fun.\n\nI Playing Free Fire, Call Of Duty Mobile, Pubg And GTA 5 With You On Total Gaming Channel.\n\nFully Indian Gamer With Hindi Commentary.\n\nYoutube Started 2 December 2018.\n\nBusiness Email: business@totalgaming.in\n\nFor Contact: Join My Discord :- http://bit.ly/totalgamingdiscprd"}, 
                        'country': 'IN'
                        }, 
                    'contentDetails': {
                        'relatedPlaylists': {'likes': '', 'uploads': 'UU5c9VlYTSvBSCaoMu_GI6gQ'}
                        }, 
                    'statistics': {
                        'viewCount': '5207118889', 
                        'subscriberCount': '39500000', 
                        'hiddenSubscriberCount': False, 
                        'videoCount': '890'
                    }, 
                    'topicDetails': {
                        'topicIds': ['/m/0403l3g', '/m/02ntfj', '/m/025zzc', '/m/0bzvm2'], 
                        'topicCategories': [
                            'https://en.wikipedia.org/wiki/Role-playing_video_game', 
                            'https://en.wikipedia.org/wiki/Action-adventure_game', 
                            'https://en.wikipedia.org/wiki/Action_game', 
                            'https://en.wikipedia.org/wiki/Video_game_culture']
                        }, 
                    'brandingSettings': {
                        'channel': {'title': 'Total Gaming', 'description': "Hi Gamers,  I'm AJAY! Here you will see me playing PC games and Mobile Games having some fun.\n\nI Playing Free Fire, Call Of Duty Mobile, Pubg And GTA 5 With You On Total Gaming Channel.\n\nFully Indian Gamer With Hindi Commentary.\n\nYoutube Started 2 December 2018.\n\nBusiness Email: business@totalgaming.in\n\nFor Contact: Join My Discord :- http://bit.ly/totalgamingdiscprd", 
                        'keywords': '"total gaming" "mobile game" "pc game" gameplay "hindi gameplay"', 
                        'unsubscribedTrailer': 'dPQHxM3ugl0', 
                        'country': 'IN'
                    }, 
                    'image': {
                        'bannerExternalUrl': 'https://yt3.googleusercontent.com/LG2AWsoDnyYaz2xzABk0xHawdJmQGX0fODxNsHCTd7Ioa259OavmSu3xM9nxOS4AojKSiiKWqMc'
                    }
                }
            }
        ]
    }

'''