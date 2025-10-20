from urllib import parse

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from app.core.config.db_config import db_config
from app.core.config.project_config import project_config
from app.core.utils.constants import ProjectEnvironmentConstants, ProjectPlatformConstants

load_dotenv()

db_name = None
db_user = None
db_password = None
db_host = (
    db_config.DB_HOST
    if project_config.PROJECT_PLATFORM == ProjectPlatformConstants.LOCAL.value
    else db_config.DB_DOCKER_HOST
)
db_port = None
db_driver = db_config.DB_DRIVER

if project_config.PROJECT_ENV == ProjectEnvironmentConstants.DEV.value:
    db_name = db_config.DB_NAME_DEV
    db_user = db_config.DB_USER_DEV
    db_password = parse.quote_plus(db_config.DB_PASSWORD_DEV)
    db_port = db_config.DB_PORT_DEV
elif project_config.PROJECT_ENV == ProjectEnvironmentConstants.TEST.value:
    db_name = db_config.DB_NAME_TEST
    db_user = db_config.DB_USER_TEST
    db_port = db_config.DB_PORT_TEST
    db_password = parse.quote_plus(db_config.DB_PASSWORD_TEST)
elif project_config.PROJECT_ENV == ProjectEnvironmentConstants.PROD.value:
    db_name = db_config.DB_NAME_PROD
    db_user = db_config.DB_USER_PROD
    db_password = parse.quote_plus(db_config.DB_PASSWORD_PROD)
    db_port = db_config.DB_PORT_PROD


SQLALCHEMY_DATABASE_URL = f"{db_driver}://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

engine = create_engine(url=SQLALCHEMY_DATABASE_URL, pool_recycle=3600, pool_timeout=30)

SessionLocal = scoped_session(sessionmaker(bind=engine, autoflush=False, autocommit=False))
