create_role_docs = """
### This endpoint is used to create a new role.

The following roles have the authority to get all roles:

- `Super Administrator`

### Path Parameters:
- None

### Query Parameters:
- None

### Request Body:
{\n
    "name": "string",\n
    "permission_ids": []\n
}

### Response Body
- General response schema
"""

get_all_roles_docs = """
### This endpoint is used for getting all roles.

The following roles have the authority to get all roles:

- `Super Administrator`

### Path Parameters:
- None

### Query Parameters:
- filters:  A JSON string representing the filters to apply.
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

### Response Body
- General response schema
"""

get_role_by_id_docs = """
### This endpoint is used for getting a role by id.

The following roles have the authority to get all roles:

- `Super Administrator`

### Path Parameters:
- role_id {string}

### Query Parameters:
- Filters
- None

### Request Body:
- None

### Response Body
- General response schema
"""

update_role_docs = """
### This endpoint is used for updating a role by id.

The following roles have the authority to get all roles:

- `Super Administrator`

### Path Parameters:
- role_id {string}

### Query Parameters:
- None

### Request Body:
{\n
    "name": "string",\n
    "permission_ids": []\n
}

### Response Body
- General response schema
"""

delete_role_docs = """
### This endpoint is used for deleting a role by id.

The following roles have the authority to get all roles:

- `Super Administrator`

### Path Parameters:
- role_id {string}

### Query Parameters:
- None

### Request Body:
- None

### Response Body
- General response schema
"""

restore_role_docs = """
### This endpoint is used for restoring a role by id.

The following roles have the authority to get all roles:

- `Super Administrator`

### Path Parameters:
- role_id {string}

### Query Parameters:
- None

### Request Body:
- None

### Response Body
- General response schema
"""
