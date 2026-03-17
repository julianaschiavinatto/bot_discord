import logging
import os

from services.youtube.utils import parse_search_response

from googleapiclient.discovery import build
import dotenv

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

    async def search_videos(self, query, max_results=5):
        logging.info(f"Searching for videos with query: '{query}'")
        request = self.youtube.search().list(
            q=query,
            part='snippet',
            type='video',
            maxResults=max_results
        )
        response = request.execute()
        return await parse_search_response(response.get('items', []))