from sqlalchemy.orm import declarative_base, Mapped, mapped_column
from sqlalchemy import String

Base = declarative_base()


class Post(Base):
    __tablename__ = "post"
    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str]
    code: Mapped[str] = mapped_column(String(6))
