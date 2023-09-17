from drf_spectacular.utils import OpenApiParameter
from drf_spectacular.types import OpenApiTypes


basic_parameter = OpenApiParameter(
    name='basic',
    type=OpenApiTypes.BOOL,
    description="""
Get response with basic information.
<p><small>Note that 'basic' parameter can not be used with other parameters which are not included in the 'basic' query.</small></p>
""",    
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

province_id_parameter = OpenApiParameter(
    name='province_id',
    type=OpenApiTypes.INT,
    description='Get results from a province with given id',
)

district_id_parameter = OpenApiParameter(
    name='district_id',
    type=OpenApiTypes.INT,
    description='Get results from a district with given id',
)

wards_nested_province_id_parameter = OpenApiParameter(
    name='province_id',
    type=OpenApiTypes.INT,
    location='path',
    description='Get all wards of a province with given id',
    required=True
)


def get_is_border_parameter(province_or_district):
    return OpenApiParameter(
        name='is_border',
        type=OpenApiTypes.BOOL,
        description=f'Is border {province_or_district} or not'
    )


def get_is_coastal_parameter(province_or_district):
    return OpenApiParameter(
        name='is_coastal',
        type=OpenApiTypes.BOOL,
        description=f'Is coastal {province_or_district} or not'
    )

