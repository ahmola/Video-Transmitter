from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from ..db import get_db
from video_dto import VideoKey, VideoOut, VideoSearchQuery, VideoListOut
from video_repository import VideoRepository
from video_service import VideoService

router = APIRouter(prefix="/video", tags=["video"])

#