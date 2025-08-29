from typing import Optional
from pydantic import BaseModel, Field, ConfigDict
from sqlalchemy import DATETIME


# 단건 조회용
class VideoKey(BaseModel):
    dev_serial: int = Field(...)
    dch_ch: int = Field(...)
    dch_media: int = Field(...)
    srv_serial: int = Field(...)
    rec_time: int = Field(...)
    rec_min: int = Field(...)
    begin_sec: int = Field(...)
    time_index: int = Field(0)
    utc: int = Field(0)

# 목록 조회용 검색 dto
class VideoSearchQuery(BaseModel):
    dev_serial: Optional[int] = None
    dch_ch: Optional[int] = None
    dch_media: Optional[int] = None
    srv_serial: Optional[int] = None
    from_time: Optional[int] = Field(None, description="rec_time >= from_time")
    to_time: Optional[int] = Field(None, description="rec_time <= to_time")
    limit: int = Field(50, ge=1, le=500)
    offset: int = Field(0, ge=0)

class VideoOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    dev_serial: int
    dch_ch: int
    dch_media: int
    srv_serial: int
    rec_time: int
    rec_min: int
    begin_sec: int
    end_sec: int
    time_index: int
    utc: int
    file_path: Optional[str] = None
    path_type: Optional[int] = None
    rec_type: Optional[int] = None
    rec_size: Optional[int] = None
    frame_index: Optional[str] = None
    vfs_property: Optional[str] = None
    ins_time: Optional[DATETIME] = None
    mod_time: Optional[DATETIME] = None

class VideoListOut(BaseModel):
    videos : list[VideoOut]
    count : int