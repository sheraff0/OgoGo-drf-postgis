from django.forms.widgets import NumberInput, MultiWidget

from contrib.utils.gis import coords_to_list, list_to_coords


class PointInputWidget(MultiWidget):
    def __init__(self, **kwargs):
        widgets = (NumberInput, NumberInput)
        super().__init__(widgets, **kwargs)

    def value_from_datadict(self, data, files, name):
        values = [data.get(f"{name}_{i}") for i in (0, 1)]
        return list_to_coords(values)

    def decompress(self, value):
        return coords_to_list(value)
