from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core.configuration.config import Config
class DatabaseConnect:
# The centralized class for the database connections and sessions

    def __init__(self) -> None:
        self.session = None

    def connect_db(self):
        config = Config()
        db_config = config.load_config()['database']
        DATABASE_URL = f"postgresql://{db_config['username']}:{db_config['password']}@{db_config['hostname']}:{db_config['port']}/{db_config['database']}"
        engine = create_engine(DATABASE_URL)
        session = sessionmaker(bind=engine)
        return session
    
    def create_engine(self):
        config = Config()
        db_config = config.load_config()['database']
        DATABASE_URL = f"postgresql://{db_config['username']}:{db_config['password']}@{db_config['hostname']}:{db_config['port']}/{db_config['database']}"
        engine = create_engine(DATABASE_URL)
        return engine
