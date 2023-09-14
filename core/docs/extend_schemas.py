from drf_spectacular.utils import extend_schema, OpenApiExample, OpenApiParameter
from drf_spectacular.types import OpenApiTypes
from drf_spectacular import openapi


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
    description='Get details of one region',
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
                            "name": "Hà Nội",
                            "name_en": "Ha Noi",
                            "id": 1
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

basic_parameter = OpenApiParameter(
    name='basic',
    type=OpenApiTypes.BOOL,
    description='Get response with basic information',
)

area_parameters = [
    OpenApiParameter(
        name='area__gt',
        type=OpenApiTypes.NUMBER,
        description='Filter with area is greater than',
    ),
    OpenApiParameter(
        name='area__lt',
        type=OpenApiTypes.NUMBER,
        description='Filter with area is less than',
    ),
]

districts_count_parameters = [
    OpenApiParameter(
        name='districts_count',
        type=OpenApiTypes.NUMBER,
        description='Filter with exact districts count',
    ),
    OpenApiParameter(
        name='districts_count__gt',
        type=OpenApiTypes.NUMBER,
        description='Filter with districts count is greater than',
    ),
    OpenApiParameter(
        name='districts_count__lt',
        type=OpenApiTypes.NUMBER,
        description='Filter with districts count is less than',
    )
]

neighbours_parameter = OpenApiParameter(
    name='neighbours',
    type=OpenApiTypes.INT,
    description='Get neighboring provinces of the province with given id',
)

number_plates_parameter = OpenApiParameter(
    name='number_plates',
    type=OpenApiTypes.INT,
    description='Get province have the number plate of',
)

population_parameters = [
    OpenApiParameter(
        name='population__gt',
        type=OpenApiTypes.INT,
        description='Filter with population is greater than',
    ),
    OpenApiParameter(
        name='population__lt',
        type=OpenApiTypes.INT,
        description='Filter with population is less than',
    ),
]

region_parameter = OpenApiParameter(
    name='region',
    type=OpenApiTypes.INT,
    description='Get provinces of a region with given id',
)

wards_count_parameters = [
    OpenApiParameter(
        name='wards_count',
        type=OpenApiTypes.NUMBER,
        description='Filter with exact wards count',
    ),
    OpenApiParameter(
        name='wards_count__gt',
        type=OpenApiTypes.NUMBER,
        description='Filter with wards count is greater than',
    ),
    OpenApiParameter(
        name='wards_count__lt',
        type=OpenApiTypes.NUMBER,
        description='Filter with wards count is less than',
    )
]

limit_parameter = OpenApiParameter(
    name='limit',
    type=OpenApiTypes.INT,
    description='Number of results to return per page. Maximum is 100.',
    default=10,
)

province_id = OpenApiParameter(
    name='province_id',
    type=OpenApiTypes.INT,
    description='Get districts of a province with given id',
)

provinces_list_extend_schema = extend_schema(
    description='Get all provinces in country',
    operation_id='Provinces List',
    parameters=[
        basic_parameter,
        *area_parameters,
        *districts_count_parameters,
        neighbours_parameter,
        number_plates_parameter,
        *population_parameters,
        region_parameter,
        *wards_count_parameters,
        limit_parameter,
    ],
    examples=[
        OpenApiExample(
            name='Full information',
            value={
                "name": "Đà Nẵng",
                "name_en": "Da Nang",
                "id": 48,
                "type": "C",
                "region": {
                    "name": "Nam Trung Bộ",
                    "name_en": "South Central Coast",
                    "id": 5
                },
                "area": 1284.73,
                "population": 1195490,
                "number_plates": [
                    43
                ],
                "is_border": 'false',
                "is_coastal": 'true',
                "neighbours": [
                    {
                        "name": "Quảng Nam",
                        "name_en": "Quang Nam",
                        "id": 49
                    },
                    {
                        "name": "Thừa Thiên Huế",
                        "name_en": "Thua Thien Hue",
                        "id": 46
                    }
                ],
                "districts_count": 8,
                "wards_count": 56
            },
        ),
        OpenApiExample(
            name='With "basic" query',
            value={
                "name": "Đà Nẵng",
                "name_en": "Da Nang",
                "id": 48,
                "type": "C"
            },
        ),
    ],
)

province_details_extend_schema = extend_schema(
    description='Get details of one province',
    operation_id='Province Details',
    parameters=[basic_parameter],
    examples=[
        OpenApiExample(
            name='Full Information',
            value={
                "name": "Đà Nẵng",
                "name_en": "Da Nang",
                "id": 48,
                "type": "C",
                "region": {
                    "name": "Nam Trung Bộ",
                    "name_en": "South Central Coast",
                    "id": 5
                },
                "area": 1284.73,
                "population": 1195490,
                "number_plates": [
                    43
                ],
                "is_border": 'false',
                "is_coastal": 'true',
                "neighbours": [
                    {
                        "name": "Quảng Nam",
                        "name_en": "Quang Nam",
                        "id": 49
                    },
                    {
                        "name": "Thừa Thiên Huế",
                        "name_en": "Thua Thien Hue",
                        "id": 46
                    }
                ],
                "districts_count": 8,
                "wards_count": 56,
                "districts": [
                    {
                        "name": "Cẩm Lệ",
                        "name_en": "Cam Le",
                        "id": 495,
                        "type": "UD",
                        "is_border": 'false',
                        "is_coastal": 'false',
                        "wards_count": 6
                    },
                    {
                        "name": "Hải Châu",
                        "name_en": "Hai Chau",
                        "id": 492,
                        "type": "UD",
                        "is_border": 'false',
                        "is_coastal": 'true',
                        "wards_count": 13
                    },
                    {
                        "name": "..."
                    },
                ]
            }
        ),
        OpenApiExample(
            name='With "basic" query',
            value={
                "name": "Đà Nẵng",
                "name_en": "Da Nang",
                "id": 48,
                "type": "C",
                "districts": [
                    {
                        "name": "Cẩm Lệ",
                        "name_en": "Cam Le",
                        "id": 495,
                        "type": "UD"
                    },
                    {
                        "name": "Hải Châu",
                        "name_en": "Hai Chau",
                        "id": 492,
                        "type": "UD"
                    },
                    {
                        "name": "..."
                    }
                ]
            },
        ),
    ],
)

districts_list_extend_schema = extend_schema(
    description='Get all districts in country',
    operation_id='Districts List',
    parameters=[
        province_id,
        basic_parameter,
        *wards_count_parameters,
        limit_parameter,
    ],
    examples=[
        OpenApiExample(
            name='Full information',
            value={
                "name": "Phú Quốc",
                "name_en": "Phu Quoc",
                "id": 911,
                "type": "C",
                "province": {
                    "name": "Kiên Giang",
                    "name_en": "Kien Giang",
                    "id": 91
                },
                "is_border": 'false',
                "is_coastal": 'true',
                "wards_count": 9
            }
        ),
        OpenApiExample(
            name='With "basic" query',
            value={
                "name": "Phú Quốc",
                "name_en": "Phu Quoc",
                "id": 911,
                "type": "C",
                "province_id": 91
            }
        )
    ]
)

district_details_extend_schema = extend_schema(
    description='Get details of one district',
    operation_id='Districts List',
    parameters=[
        basic_parameter,
    ],
    examples=[
        OpenApiExample(
            name='Full information',
            value={
                "name": "Phú Quốc",
                "name_en": "Phu Quoc",
                "id": 911,
                "type": "C",
                "province": {
                    "name": "Kiên Giang",
                    "name_en": "Kien Giang",
                    "id": 91
                },
                "is_border": 'false',
                "is_coastal": 'true',
                "wards_count": 9,
                "wards": [
                    {
                        "name": "Dương Đông",
                        "name_en": "Duong Dong",
                        "id": 31078,
                        "type": "W"
                    },
                    {
                        "name": "Gành Dầu",
                        "name_en": "Ganh Dau",
                        "id": 31087,
                        "type": "C"
                    },
                    {
                        "name": "...",
                    },
                ]
            }
        ),
        OpenApiExample(
            name='With "basic" query',
            value={
                "name": "Phú Quốc",
                "name_en": "Phu Quoc",
                "id": 911,
                "type": "C",
                "province_id": 91,
                "wards": [
                    {
                        "name": "Dương Đông",
                        "name_en": "Duong Dong",
                        "id": 31078,
                        "type": "W"
                    },
                    {
                        "name": "Gành Dầu",
                        "name_en": "Ganh Dau",
                        "id": 31087,
                        "type": "C"
                    },
                    {
                        "name": "..."
                    }
                ]
            }
        )
    ]
)
