create_district_docs = """
### This endpoint is used to create a new district.

The following districts have the authority to get all districts:

- `Super Administrator`

### Path Parameters:
- None

### Query Parameters:
- None

### Request Body:
{\n
    "name": "string",\n
    "region_id": "string"\n
}

### Response Body
- General response schema
"""

get_all_districts_docs = """
### This endpoint is used for getting all districts.

The following districts have the authority to get all districts:

- `all`

### Path Parameters:
- None

### Query Parameters:
- filters: A JSON string representing the filters to apply.
    - Allowed filters and operators:
        - name: eq, like
        - region_id: eq
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

get_district_by_id_docs = """
### This endpoint is used for getting a district by id.

The following districts have the authority to get all districts:

- `Super Administrator`

### Path Parameters:
- district_id {string}

### Query Parameters:
- None

### Request Body:
- None

### Response Body
- General response schema
"""

update_district_docs = """
### This endpoint is used for updating a district by id.

The following districts have the authority to get all districts:

- `Super Administrator`

### Path Parameters:
- district_id {string}

### Query Parameters:
- None

### Request Body:
{\n
    "name": "string",\n
    "region_id": "string"\n
}
### Response Body
- General response schema
"""

delete_district_docs = """
### This endpoint is used for deleting a district by id.

The following districts have the authority to get all districts:

- `Super Administrator`

### Path Parameters:
- district_id {string}

### Query Parameters:
- None

### Request Body:
- None

### Response Body
- General response schema
"""

restore_district_docs = """
### This endpoint is used for restoring a district by id.

The following districts have the authority to get all districts:

- `Super Administrator`

### Path Parameters:
- district_id {string}

### Query Parameters:
- None

### Request Body:
- None

### Response Body
- General response schema
"""
