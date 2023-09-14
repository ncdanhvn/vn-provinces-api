from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from drf_spectacular.types import OpenApiTypes

regions_list_extend_schema = extend_schema(
    description='Get all regions in country',
    operation_id='Regions List',
    examples=[
        OpenApiExample(
                name='Example 1',
                value={
                    "name": "Tây Bắc Bộ",
                    "name_en": "Northwest",
                    "id": 1,
                    "provinces_count": 6
                },
            response_only=True
        ),
    ],
)

region_details_extend_schema = extend_schema(
    description='Get detail of one region',
    operation_id='Region Details',
    examples=[
        OpenApiExample(
                name='Example 1',
                value={
                    "name": "Đồng bằng sông Hồng",
                    "name_en": "Red River Delta",
                    "id": 3,
                    "provinces_count": 10,
                    "provinces": [
                        {
                            "name": "Bắc Ninh",
                            "name_en": "Bac Ninh",
                            "id": 27
                        },
                        {
                            "name": "..."
                        }
                    ]
                },
            response_only=True
        ),
    ],
)
