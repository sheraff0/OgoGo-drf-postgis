def validate_and_serialize(Serializer, data, many=False):
    serializer = Serializer(data=data, many=many)
    serializer.is_valid(raise_exception=True)
    return serializer.data
