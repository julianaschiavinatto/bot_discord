import asyncio

from services.youtube.utils import parse_search_response
from services.youtube.youtube_service import YoutubeService

async def main():
    youtube = YoutubeService()

    youtube_results = await youtube.search_videos("voy a llevarte pa pr", max_results=5)
    parsed_results = await parse_search_response(youtube_results)

    print(parsed_results)

if __name__ == "__main__":
    asyncio.run(main())