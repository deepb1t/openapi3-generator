from apispec import APISpec

from internal.statuses import OK
from internal.helpers import param, method, response
from api.schemas.categories import CategorySchema


def add_paths(spec: APISpec):
    spec.path(
        path='/category/{id}',
        parameters=[
            param('id', 'ID of a Category')
        ],
        operations=dict(
            get=method(
                responses=[
                    response(OK, 'Information about a category', CategorySchema),
                ]
            )
        ),
    )
