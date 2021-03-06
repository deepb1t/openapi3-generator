from apispec import APISpec


def response(status: str, description: str, schema):
    name = schema.__name__

    return dict(key=status, value={'description': description, 'content': {'application/json': {'schema': name}}})


def method(responses, tags=None, security=None):
    if not tags:
        tags = []

    data_responses = {}
    for it in responses:
        data_responses[it['key']] = it['value']

    data = dict(
        responses=data_responses,
        tags=tags,
    )

    if security:
        data['security'] = security

    return data


def add_schema(spec: APISpec, schema):
    if isinstance(schema, list):
        for item in schema:
            if not hasattr(item, 'get_name'):
                raise Exception('No get_name method in this added schema')

            spec.components.schema(item.get_name(), schema=item)
    else:
        if not hasattr(schema, 'get_name'):
            raise Exception('No get_name method in this added schema')

        spec.components.schema(schema.get_name(), schema=schema)


def param(name: str, description: str):
    return {'name': name, 'in': 'path', 'required': True, 'description': description, 'schema': {'type': 'string'}}


def security_api_key():
    return {'type': 'apiKey', 'in': 'header', 'name': 'X-API-Key'}


def security_jwt():
    return {'type': 'http', 'scheme': 'bearer', 'bearerFormat': 'JWT'}


def api_key():
    return {'ApiKey': []}


def bearer():
    return {'Bearer': []}
