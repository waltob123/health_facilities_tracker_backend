from abc import ABC, abstractmethod
from typing import Any, Generic, Type, TypeVar

from sqlalchemy.orm import Session

ModelType = TypeVar("ModelType")
RepositoryType = TypeVar("RepositoryType")


class BaseRepositoryFactory(ABC, Generic[ModelType, RepositoryType]):
    """A base factory for creating repositories."""

    @classmethod
    @abstractmethod
    def create(cls, *args, **kwargs) -> Any:  # type: ignore
        """Create a new repository."""

    @classmethod
    def _default_create(
        cls, *, db_session: Session, model: Type[ModelType], repository_class: Type[RepositoryType]
    ) -> RepositoryType:  # type: ignore
        """Default method to create a new repository.

        Args:
            db_session (Session): The database session.
            model: The model to create the repository for.
            repository_class: The repository class to create.
        """
        return repository_class(db_session=db_session, model=model)  # type: ignore
