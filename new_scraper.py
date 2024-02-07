import csv
from googleapiclient.discovery import build

# Initialize YouTube API client
api_key = ''
youtube = build('youtube', 'v3', developerKey=api_key)

def get_channel_stats(channel_id):
    request = youtube.channels().list(
        part='snippet,contentDetails,statistics,brandingSettings,topicDetails',
        id=channel_id
    )
    response = request.execute()

    # Check if response contains 'items' and is not empty
    if 'items' in response and response['items']:
        for item in response['items']:
            stats = {
                'title': item['snippet']['title'],
                'description': item['snippet']['description'],  # Added
                'view_count': item['statistics']['viewCount'],
                'subscriber_count': item['statistics']['subscriberCount'],
                'video_count': item['statistics']['videoCount'],
                'country': item.get('brandingSettings', {}).get('channel', {}).get('country', 'N/A'),  # Added
                'topics': item.get('topicDetails', {}).get('topicCategories', [])  # Added
            }

            return stats
    else:
        print(f"No data found for channel ID: {channel_id}")
        return None

# List of channel IDs you're interested in
channel_ids = [
    'UCX6OQ3DkcsbYNE6H8uQQuVA', 'UC-lHJZR3Gqxm24_Vd_AJ5Yw', 'UCbCmjCuTUZos6Inko4u57UQ', 
    'UCpEhnqL0y41EpW2TvWAHD7Q', 'UCk8GzjMOrta8yxDcKfylJYw', 'UCJplp5SjeGSdVdwsfb9Q7lQ', 
    'UCvlE5gTbOvjiolFlEm-c_Ow', 'UCJ5v_MCY6GNUBTO8-D3XoAg', 'UCu7Hg0f3rxqZ6qs-188ZbjQ', 
    'UCOmHUn--16B90oW2L6FRR3A', 'UC295-Dw_tDNtZXFeAPAW6Aw', 
    'UCLkAepWjdylmXSltofFvsYQ', 'UC6-F5tO8uklgE9Zy8IvbdFw', 'UCppHT7SZKKvar4Oc9J4oljQ', 'UC3IZKseVpdzPSBaWxBxundA', 
    'UCcdwLMPsaU2ezNSJU1nFoBQ', 'UCP6uH_XlsxrXwZQ4DlqbqPg', 'UCffDXn7ycAzwL2LDlbyWOTw', 
    'UCaayLD9i5x4MmIoVZxXSv_g', 'UCJrDMFOdv1I2k8n9oK_V21w', 'UCt4t-jeY85JegMlZ-E5UWtA', 
    'UC3gNmTGu-TTbFPpfSs5kNkg', 'UC22nIfOTM7KLIQuFGMKzQbg', 'UC1ciY6kR3yj3kaKZ6R7ewAg', 
    'UC56gTxNs4f9xZ7Pa2i5xNzg', 'UCfM3zsQsOnfWNUppiycmBuw', 'UCbTLwN10NoCU4WDzLf1JMOA', 
    'UCEdvpU2pFRCVqU6yIPyTpMQ', 'UCqECaJ8Gagnn7YCbPEzWH6g', 'UC4NALVCmcmL5ntpV0thoH6w', 
    'UC0C-w0YjGpqDXGB8IHb662A', 'UC9CoOnJkIBMdeijd9qYoT_g', 'UCF1JIbMUs6uqoZEY1Haw0GQ', 
    'UCYWOjHweP2V-8kGKmmAmQJQ', 'UC4JCksJF76g_MdzPVBJoC3Q', 'UC2tsySbe9TNrI-xh2lximHA', 
    'UCe9JSDmyqNgA_l2BzGHq1Ug', 'UClZkHt2kNIgyrTTPnSQV3SA', 'UCYiGq8XF7YQD00x7wAd62Zg', 
    'UC3MLnJtqc_phABBriLRhtgQ', 'UCmBA_wu8xGg1OfOkfW13Q0Q', 'UC6-F5tO8uklgE9Zy8IvbdFw', 
    'UCIwFjwMjI0y7PDBVEO9-bkQ', 'UC55IWqFLDH1Xp7iu1_xknRA', 'UCBnZ16ahKA2DZ_T5W0FPUXg', 
    'UCqJ5zFEED1hWs0KNQCQuYdQ', 'UCJg19noZp7-BYIGvypu_cow', 'UCV4xOVpbcV8SdueDCOxLXtQ', 
    'UCYLNGLIzMhRTi6ZOLjAPSmw', 'UCj0O6W8yDuLg3iraAXKgCrQ', 'UCvh1at6xpV1ytYOAzxmqUsA', 
    'UCJrOtniJ0-NWz37R30urifQ', 'UCrnQFuUabBHaw-BRhPo8xEA', 'UCYvmuw-JtVrTZQ-7Y4kd63Q', 
    'UC4rlAVgAK0SGk-yTfe48Qpw', 'UC3KQ5GWANYF8lChqjZpXsQw', 'UCQZfFRohQ7UX-0CdXl-6pwQ', 
    'UC6gVx_vALsYT-z_u1djJbBQ', 'UCWi_65E_L8tQZ34C6wVAlpQ', 'UCZJ7m7EnCNodqnu5SAtg8eQ', 
    'UCOnIJiQuk1fDSp6p1GCZy3A', 'UCOsyDsO5tIt-VZ1iwjdQmew', 'UCJplp5SjeGSdVdwsfb9Q7lQ', 
    'UCcgqSM4YEo5vVQpqwN-MaNw', 'UC4tS4Q_Cno5JVcIUXxQOOpA', 'UCQ7x25F6YXY9DvGeHFxLhRQ', 
    'UC_gV70G_Y51LTa3qhu8KiEA', 'UCECJDeK0MNapZbpaOzxrUPA', 'UCIPPMRA040LQr5QPyJEbmXA', 
    'UCj22tfcQrWG7EMEKS0qLeEg', 'UCw7xjxzbMwgBSmbeYwqYRMg', 'UCLsooMJoIpl_7ux2jvdPB-Q', 
    'UCKAqou7V9FAWXpZd9xtOg3Q', 'UCtW7qWjpCZ8zps-Cf2NF26w', 'UCwHE1kM1CPJd_pI9FQ0-4dg', 
    'UCoQm-PeHC-cbJclKJYJ8LzA', 'UCXazgXDIYyWH-yXLAkcrFxw', 'UC3ZkCd7XtUREnjjt3cyY_gg', 
    'UCRWFSbif-RFENbBrSiez1DA', 'UCNUQK9mQoqi4yNXw2_Rj6SA', 'UCsT0YIqwnpJCM-mx7-gSA4Q', 
    'UCM9r1xn6s30OnlJWb-jc3Sw', 'UCvlE5gTbOvjiolFlEm-c_Ow', 'UCpEJRZdSpdVZ8vh63T9I2KQ', 
    'UC5c9VlYTSvBSCaoMu_GI6gQ', 'UCKe6w0exI94U-RzqAyoY1VA', 'UC7_YxT-KID8kRbqZo7MyscQ', 'UCKqH_9mk1waLgBiL2vT5b9g', 'UCam8T03EOFBsNdR0thrFHdQ', 'UCV306eHqgo0LvBf3Mh36AHg', 'UCh7EqOZt7EvO2osuKbIlpGg', 'UCbTVTephX30ZhQF5zwFppBg', 'UCYzPXprvl5Y-Sf0g4vX-m6g', 'UCS5Oz6CHmeoF7vSad0qqXfw', 'UCpB959t8iPrxQWj7G6n0ctQ', 'UC0DZmkupLYwc0yDsfocLh0A', 'UCAW-NpUFkMyCNrvRSSGIvDQ', 'UCo_IB5145EVNcf8hw1Kku7w', 'UCHa-hWHrTt4hqh-WiHry3Lw', 'UCmh5gdwCx6lN7gEC20leNVA'
]

# Open the file for writing
with open('youtube_channels_stats.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    
    # Update the header row to include new fields
    writer.writerow([
        'Title', 
        'Description',  # New field
        'View Count', 
        'Subscriber Count', 
        'Video Count', 
        'Country',  # New field
        'Topics'  # New field
    ])

    # Iterate over each channel ID to fetch data and write it to the CSV
    for channel_id in channel_ids:
        data = get_channel_stats(channel_id)
        if data:
            # Ensure to convert list of topics to a string, if necessary
            topics_str = ', '.join(data['topics']) if data['topics'] else 'N/A'
            
            writer.writerow([
                data['title'], 
                data['description'],  # New data
                data['view_count'], 
                data['subscriber_count'], 
                data['video_count'], 
                data['country'],  # New data
                topics_str  # New data, converted to string
            ])

print("Data written to youtube_channels_stats.csv")

