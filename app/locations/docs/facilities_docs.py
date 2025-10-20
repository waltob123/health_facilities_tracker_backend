create_facility_docs = """
### This endpoint is used to create a new facility.

The following facilities have the authority to get all facilities:

- `Super Administrator`

### Path Parameters:
- None

### Query Parameters:
- None

### Request Body:
{\n
    "name": "string"\n
    "sub_district_id": "string"\n
    "facility_type": "string"\n
    "ownership": "string"\n
    "longitude": "float"\n
    "latitude": "float"\n
    "altitude": "float"\n
}

### Response Body
- General response schema
"""

get_all_facilities_docs = """
### This endpoint is used for getting all facilities.

The following facilities have the authority to get all facilities:

- `all`

### Path Parameters:
- None

### Query Parameters:
- filters: A JSON string representing the filters to apply.
    - Allowed filters and their operators:
        - name: eq, like
        - sub_district_name: eq, like
        - district_name: eq, like
        - region_name: eq, like
        - facility_type: eq, like
        - ownership: eq, like
        - created_at: eq, ne, gt, lt, ge, le
        - is_deleted: eq

- sort: A JSON string representing the sort order.
    - Allowed sorts:
        - name: asc, desc

- pagination: A JSON string representing the pagination settings.

### Request Body:
- None

### Response Body
- General response schema
"""

get_facility_by_id_docs = """
### This endpoint is used for getting a facility by id.

The following facilities have the authority to get all facilities:

- `Super Administrator`

### Path Parameters:
- facility_id {string}

### Query Parameters:
- None

### Request Body:
- None

### Response Body
- General response schema
"""

update_facility_docs = """
### This endpoint is used for updating a facility by id.

The following facilities have the authority to get all facilities:

- `Super Administrator`

### Path Parameters:
- facility_id {string}

### Query Parameters:
- None

### Request Body:
{\n
    "name": "string"\n
    "sub_district_id": "string"\n
    "facility_type": "string"\n
    "ownership": "string"\n
    "longitude": "float"\n
    "latitude": "float"\n
    "altitude": "float"\n
}

### Response Body
- General response schema
"""

delete_facility_docs = """
### This endpoint is used for deleting a facility by id.

The following facilities have the authority to get all facilities:

- `Super Administrator`

### Path Parameters:
- facility_id {string}

### Query Parameters:
- None

### Request Body:
- None

### Response Body
- General response schema
"""

restore_facility_docs = """
### This endpoint is used for restoring a facility by id.

The following facilities have the authority to get all facilities:

- `Super Administrator`

### Path Parameters:
- facility_id {string}

### Query Parameters:
- None

### Request Body:
- None

### Response Body
- General response schema
"""
