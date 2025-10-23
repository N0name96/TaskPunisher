from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


DB_TASKS = 'sqlite:///Data/TaskPunisher.db'


engine = create_engine(
    url=DB_TASKS,
    connect_args=
    {
        "check_same_thread": False
    }
)


SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


def get_db():
    '''get the database session'''

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()