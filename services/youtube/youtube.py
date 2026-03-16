from googleapiclient.discovery import build
import os
import dotenv
import logging

logger = logging.getLogger(__name__)
dotenv.load_dotenv()

class YoutubeService:
    def __init__(self):
        self.api_key = os.getenv("YOUTUBE_API_KEY", "")
        
        try:
            self.youtube = build('youtube', 'v3', developerKey=self.api_key)
            logger.info("YouTube service initialized successfully.")
        except Exception as e:
            logger.error(f"Error initializing YouTube service: {e}")

    def search_videos(self, query, max_results=5):
        request = self.youtube.search().list(
            q=query,
            part='snippet',
            type='video',
            maxResults=max_results
        )
        response = request.execute()
        return response.get('items', [])