from enum import Enum


class FacilityType(Enum):
    """Enum for facility types."""

    CHPS = "chps"
    TEACHING_HOSPITAL = "teaching-hospital"
    DISTRICT_HOSPITAL = "district-hospital"
    HOSPITAL = "hospital"
    CLINIC = "clinic"
    HEALTH_CENTER = "health-centre"
    LEPROSARIUM = "leprosarium"
    MATERNITY_HOME = "maternity-home"
    POLYCLINIC = "polyclinic"
    PSYCHIATRIC_HOSPITAL = "psychiatric-hospital"
    REGIONAL_HOSPITAL = "regional-hospital"
    UNIVERSITY_HOSPITAL_CLINIC = "university-hospital-clinic"


class FacilityOwnership(Enum):
    """Enum for facility ownerships."""

    CHAG = "chag"
    GOVERNMENT = "government"
    MINES = "mines"
    OTHER_FAITH_BASED = "other-faith-based"
    PRIVATE = "private"
    QUASI_GOVERNMENT = "quasi-government"
