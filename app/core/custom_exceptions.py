class ObjectAlreadyExistsException(Exception):
    """Exception for already existing objects."""


class FailedToSaveObjectException(Exception):
    """Exception for failure to save objects."""


class InvalidFilterError(Exception):
    """Exception for invalid filter passed."""


class InvalidFilterOperatorError(Exception):
    """Exception for invalid operator passed."""


class InvalidSortError(Exception):
    """Exception for invalid sort passed."""


class InvalidSortModeError(Exception):
    """Exception for invalid sort mode passed."""


class InvalidQueryParamsJSONFormatError(Exception):
    """Exception for invalid query parameters json format."""


class InvalidPaginationOptionError(Exception):
    """Exception for invalid pagination options."""


class InvalidPaginationValueError(Exception):
    """Exception for invalid pagination value."""


class EntityDoesNotExistsError(Exception):
    """Exception for when an entity does not exist."""
