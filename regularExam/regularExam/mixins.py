class ReadOnlyMixin:
    readonly_fields = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if '__all__' in self.readonly_fields:
            for field in self.fields.values():
                field.disabled = True
        else:
            for field_name in self.readonly_fields:
                if field_name in self.fields:
                    self.fields[field_name].disabled = True