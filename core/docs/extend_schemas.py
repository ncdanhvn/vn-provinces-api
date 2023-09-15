from drf_spectacular.utils import extend_schema, OpenApiExample
from .operation_parameters import *


regions_list_extend_schema = extend_schema(
    description='Get all regions in country',
    operation_id='regions_list',
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
    operation_id='region_details',
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

provinces_list_extend_schema = extend_schema(
    description='Get all provinces in country',
    operation_id='provinces_list',
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
        get_is_border_parameter('province'),
        get_is_coastal_parameter('province'),
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
    operation_id='province_details',
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
    operation_id='districts_list',
    parameters=[
        province_id_parameter,
        basic_parameter,
        *wards_count_parameters,
        limit_parameter,
        get_is_border_parameter('district'),
        get_is_coastal_parameter('district'),
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
    operation_id='district_details',
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

wards_list_extend_schema = extend_schema(
    operation_id='wards_list',
    description='Get all wards in country',
    parameters=[
        province_id_parameter,
        district_id_parameter,
        limit_parameter,
        basic_parameter,
    ],
    examples=[
        OpenApiExample(
            name='Full information',
            value={
                "name": "Bách Khoa",
                "name_en": "Bach Khoa",
                "id": 277,
                "type": "W",
                "district": {
                    "name": "Hai Bà Trưng",
                    "name_en": "Hai Ba Trung",
                    "id": 7
                },
                "province": {
                    "name": "Hà Nội",
                    "name_en": "Ha Noi",
                    "id": 1
                }
            }
        ),
        OpenApiExample(
            name='With "basic" query',
            value={
                "name": "Bách Khoa",
                "name_en": "Bach Khoa",
                "id": 277,
                "type": "W",
                "district_id": 7,
                "province_id": 1
            }
        ),
    ]
)

ward_details_extend_schema = extend_schema(
    operation_id='ward_details',
    description='Get details of one ward',
    parameters=[
        basic_parameter,
    ],
    examples=[
        OpenApiExample(
            name='Full information',
            value={
                "name": "Bách Khoa",
                "name_en": "Bach Khoa",
                "id": 277,
                "type": "W",
                "district": {
                    "name": "Hai Bà Trưng",
                    "name_en": "Hai Ba Trung",
                    "id": 7
                },
                "province": {
                    "name": "Hà Nội",
                    "name_en": "Ha Noi",
                    "id": 1
                }
            }
        ),
        OpenApiExample(
            name='With "basic" query',
            value={
                "name": "Bách Khoa",
                "name_en": "Bach Khoa",
                "id": 277,
                "type": "W",
                "district_id": 7,
                "province_id": 1
            }
        ),
    ]
)

wards_nested_list_extend_schema = extend_schema(
    operation_id='wards_nested_province_list',
    description='Get all wards of a province',
    parameters=[
        wards_nested_province_id_parameter,
        basic_parameter,
        limit_parameter,
    ],
    examples=[
        OpenApiExample(
            name="Full information",
            value={
                "name": "Bách Khoa",
                "name_en": "Bach Khoa",
                "id": 277,
                "type": "W",
                "district": {
                    "name": "Hai Bà Trưng",
                    "name_en": "Hai Ba Trung",
                    "id": 7
                }
            }
        ),
        OpenApiExample(
            name='With "basic" query',
            value={
                "name": "Bách Khoa",
                "name_en": "Bach Khoa",
                "id": 277,
                "type": "W",
                "district_id": 7
            }
        ),
    ]
)
