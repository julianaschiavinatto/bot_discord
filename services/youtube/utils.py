from dataclasses import dataclass

@dataclass
class Video:
    title: str
    channel_title: str | None
    provider: str | None

    def __str__(self):
        return f"{self.title} - {self.channel_title}\n"
    

async def parse_search_response(response) -> list[Video]:
    videos = []
    for item in response:
        video = Video(
            title=item['snippet']['title'],
            channel_title=item['snippet'].get('channelTitle'),
            provider="Youtube"
        )
        videos.append(video)

    return videos