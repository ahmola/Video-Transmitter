from sqlalchemy.ext.asyncio import AsyncSession

from video_dto import *
from video_repository import VideoRepository

class VideoService:
    def __init__(self, repo: VideoRepository):
        self.repo = repo

    async def get_video(self, db: AsyncSession, key: VideoKey) -> VideoOut:
        video = await self.repo.get_video_by_key(db, key)
        return VideoOut.model_validate(video) if video else None

    async def get_all_video(self, db: AsyncSession, q: VideoSearchQuery) -> VideoListOut:
        video_list = await self.repo.get_all_video(db, q)
        return VideoListOut.model_validate(video_list) if video_list else None

    async def count(self, db: AsyncSession) -> int:
        return await self.repo.count(db)