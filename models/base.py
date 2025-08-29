from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

# ORM Base, 모든 모델의 부모(메타데이터 보유)
class Base(DeclarativeBase): pass