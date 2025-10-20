from app.core.schemas.query_params_schemas import AllowedFilterSchema, AllowedSortSchema

# general filters
created_at_filter = AllowedFilterSchema(field="created_at", operators=["eq", "lt", "le", "gt", "ge", "ne"])
is_deleted_filter = AllowedFilterSchema(field="is_deleted", operators=["eq"])

# general sorts
created_at_sort = AllowedSortSchema(field="created_at")
is_deleted_sort = AllowedSortSchema(field="is_deleted")

###################################################################################
#                             ROOT ROUTE FILTERS AND SORT                         #
###################################################################################
# Define allowed filters
email_filter = AllowedFilterSchema(field="email", operators=["EQ"])  # type: ignore
age_filter = AllowedFilterSchema(field="age", operators=["lt", "le", "gt", "ge", "eq", "ne"])
allowed_filters = [email_filter, age_filter]

# Define allowed sorts
email_sort = AllowedSortSchema(field="email")  # type: ignore
age_sort = AllowedSortSchema(field="age")
allowed_sorts = [email_sort, age_sort]
