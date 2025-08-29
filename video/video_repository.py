from typing import Optional, Sequence
from sqlalchemy import select, and_, func
from sqlalchemy.ext.asyncio import AsyncSession
from video import Video
from video_dto import VideoKey, VideoSearchQuery

class VideoRepository:
    async def get_video_by_key(self, db: AsyncSession, key: VideoKey) -> Optional[Video]:
        stmt = select(Video).where(
            Video.dev_serial == key.dev_serial,
            Video.dch_ch == key.dch_ch,
            Video.dch_media == key.dch_media,
            Video.srv_serial == key.srv_serial,
            Video.rec_time == key.rec_time,
            Video.rec_min == key.rec_min,
            Video.begin_sec == key.begin_sec,
            Video.time_index == key.time_index,
            Video.utc == key.utc,
        )
        res = await db.execute(stmt)
        return res.scalar_one_or_none()

    async def get_all_video(self, db: AsyncSession, q: VideoSearchQuery) -> Sequence[Video]:
        conds = []
        if q.dev_serial is not None: conds.append(Video.dev_serial == q.dev_serial)
        if q.dch_ch    is not None: conds.append(Video.dch_ch    == q.dch_ch)
        if q.dch_media is not None: conds.append(Video.dch_media == q.dch_media)
        if q.srv_serial is not None: conds.append(Video.srv_serial == q.srv_serial)
        if q.from_time is not None: conds.append(Video.rec_time >= q.from_time)
        if q.to_time   is not None: conds.append(Video.rec_time <= q.to_time)

        stmt = (
            select(Video)
            .where(and_(*conds)) if conds else select(Video)
        ).order_by(Video.rec_time.desc()).limit(q.limit).offset(q.offset)

        res = await db.execute(stmt)
        return res.scalars().all()

    async def count(self, db: AsyncSession) -> int:
        stmt = select(func.count()).select_from(Video)

        result = await db.execute(stmt)

        return int(result.scalar_one())
