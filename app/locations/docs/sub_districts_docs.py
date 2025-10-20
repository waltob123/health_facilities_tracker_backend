create_sub_district_docs = """
### This endpoint is used to create a new sub_district.

The following sub_districts have the authority to get all sub_districts:

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

get_all_sub_districts_docs = """
### This endpoint is used for getting all sub_districts.

The following sub_districts have the authority to get all sub_districts:

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

get_sub_district_by_id_docs = """
### This endpoint is used for getting a sub_district by id.

The following sub_districts have the authority to get all sub_districts:

- `Super Administrator`

### Path Parameters:
- sub_district_id {string}

### Query Parameters:
- None

### Request Body:
- None

### Response Body
- General response schema
"""

update_sub_district_docs = """
### This endpoint is used for updating a sub_district by id.

The following sub_districts have the authority to get all sub_districts:

- `Super Administrator`

### Path Parameters:
- sub_district_id {string}

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

delete_sub_district_docs = """
### This endpoint is used for deleting a sub_district by id.

The following sub_districts have the authority to get all sub_districts:

- `Super Administrator`

### Path Parameters:
- sub_district_id {string}

### Query Parameters:
- None

### Request Body:
- None

### Response Body
- General response schema
"""

restore_sub_district_docs = """
### This endpoint is used for restoring a sub_district by id.

The following sub_districts have the authority to get all sub_districts:

- `Super Administrator`

### Path Parameters:
- sub_district_id {string}

### Query Parameters:
- None

### Request Body:
- None

### Response Body
- General response schema
"""
