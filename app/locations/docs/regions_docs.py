create_region_docs = """
### This endpoint is used to create a new region.

The following regions have the authority to get all regions:

- `Super Administrator`

### Path Parameters:
- None

### Query Parameters:
- None

### Request Body:
{\n
    "name": "string",\n
}

### Response Body
- General response schema
"""

get_all_regions_docs = """
### This endpoint is used for getting all regions.

The following regions have the authority to get all regions:

- `all`

### Path Parameters:
- None

### Query Parameters:
- filters: A JSON string representing the filters to apply.
    - Allowed filters and operators:
        - name: eq, like
        - created_at: eq, ne, gt, lt, ge, le
        - is_deleted: eq
- sort: A JSON string representing the sort order.
    - Allowed sorts:
        - name: asc, desc
- pagination: A JSON string representing the pagination settings.

### Request Body:
- None

### Response Body:
- General response schema
"""

get_region_by_id_docs = """
### This endpoint is used for getting a region by id.

The following regions have the authority to get all regions:

- `Super Administrator`

### Path Parameters:
- region_id {string}

### Query Parameters:
- None

### Request Body:
- None

### Response Body
- General response schema
"""

update_region_docs = """
### This endpoint is used for updating a region by id.

The following regions have the authority to get all regions:

- `Super Administrator`

### Path Parameters:
- region_id {string}

### Query Parameters:
- None

### Request Body:
{\n
    "name": "string",\n
}

### Response Body
- General response schema
"""

delete_region_docs = """
### This endpoint is used for deleting a region by id.

The following regions have the authority to get all regions:

- `Super Administrator`

### Path Parameters:
- region_id {string}

### Query Parameters:
- None

### Request Body:
- None

### Response Body
- General response schema
"""

restore_region_docs = """
### This endpoint is used for restoring a region by id.

The following regions have the authority to get all regions:

- `Super Administrator`

### Path Parameters:
- region_id {string}

### Query Parameters:
- None

### Request Body:
- None

### Response Body
- General response schema
"""
