from sqlalchemy.orm import Session

from app.database.session import SessionLocal


def db_session_dependency() -> Session:  # type: ignore
    """Dependency that provides a database session.

    Yields:
        Generator[Session, None, None]: A database session.
    """
    db_session = SessionLocal()
    try:
        yield db_session
    finally:
        db_session.close()
