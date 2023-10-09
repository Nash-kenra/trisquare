from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core.configuration.config_singleton import config_singleton


class DatabaseConnect:
    # The centralized class for the database connections and sessions

    def __init__(self) -> None:
        self.session = None

    def create_engine(self):
        config = config_singleton()
        db_config = config.load_config()["database"]
        DATABASE_URL = f"postgresql://{db_config['username']}:{db_config['password']}@host.docker.internal:{db_config['port']}/{db_config['database']}"
        engine = create_engine(DATABASE_URL)
        return engine

    def connect_db(self):
        engine = self.create_engine()
        session = sessionmaker(bind=engine)
        return session

    
