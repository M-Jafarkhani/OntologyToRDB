class Property:
    label: str
    prop_type: str

    def __init__(self, label, prop_type):
        self.label = label
        self.prop_type = prop_type


class ForeignKey:
    label: str
    reference_iri: str

    def __init__(self, label, reference_iri):
        self.label = label
        self.reference_iri = reference_iri


class ClassMetaData:
    label: str
    properties: list[Property]
    foreignKeys: list[ForeignKey]

    def __init__(self, label):
        self.label = label
        self.properties = list()


class DataTypePropertyMetaData:
    label: str
