from sqlalchemy import Integer, String, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from database.base import Base


class PunishmentModel(Base):
    __tablename__ = 'punishments'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    description: Mapped[String] = mapped_column(String, nullable=False)
    isCompleted: Mapped[bool] = mapped_column(Boolean, default=False)