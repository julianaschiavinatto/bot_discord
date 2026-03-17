import asyncio
from services.youtube.youtube_service import YoutubeService

async def main():
    youtube = YoutubeService()
    query_list = await youtube.search_videos("voy a llevarte pa pr", max_results=5)
    print(query_list)

if __name__ == "__main__":
    asyncio.run(main())