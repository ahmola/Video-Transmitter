from typing import Optional
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer, VARCHAR, BIGINT, DATETIME
from v1.api_server.models.base import Base

# Entity(Spring JPA의 @Entity와 유사)
class Video(Base):
    __tablename__ = "fxidx_00186b8"

    # primary key
    dch_ch = mapped_column(Integer, primary_key=True)
    dch_media = mapped_column(Integer, primary_key=True)
    srv_serial = mapped_column(Integer, primary_key=True)
    rec_min = mapped_column(BIGINT, primary_key=True)
    time_index = mapped_column(Integer, primary_key=True, default=0)
    utc = mapped_column(Integer, primary_key=True, default=0)
    begin_sec = mapped_column(Integer, primary_key=True)

    # column
    dev_serial = mapped_column(Integer, nullable=False)
    end_sec = mapped_column(Integer, nullable=False)
    rec_time = mapped_column(Integer)
    file_path = mapped_column(String)
    path_type = mapped_column(Integer)
    rec_type = mapped_column(Integer)
    rec_size = mapped_column(Integer)
    frame_index = mapped_column(VARCHAR(128))
    vfs_property = mapped_column(String)
    ins_time = mapped_column(DATETIME)
    mod_time = mapped_column(DATETIME)