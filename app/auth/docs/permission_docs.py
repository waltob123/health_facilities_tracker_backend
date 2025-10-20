get_all_permissions_docs = """
### This endpoint is used for getting all permissions.

The following permissions have the authority to get all permissions:

- `Super Administrator`

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

### Response Body
- General response schema
"""
