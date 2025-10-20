from app.core.schemas.query_params_schemas import AllowedFilterSchema, AllowedSortSchema
from app.core.utils.allowed_filters_sort import created_at_filter, created_at_sort, is_deleted_filter, is_deleted_sort

##################3 filters without joins ##############################################
role_filters_without_joins = ["name", "created_at", "is_deleted"]
permission_filters_without_joins = role_filters_without_joins.copy()

################################### allowed role filters ###############################
role_name_filter = AllowedFilterSchema(field="name", operators=["eq", "like"])
allowed_role_filters = [role_name_filter, created_at_filter, is_deleted_filter]

################################### allowed permission filters ############################
allowed_permission_filters = allowed_role_filters.copy()

################################### allowed role sorts ####################################
role_name_sort = AllowedSortSchema(field="name")
allowed_role_sorts = [role_name_sort, created_at_sort, is_deleted_sort]

################################ allowed permission sorts ################################
allowed_permission_sorts = allowed_role_sorts.copy()
