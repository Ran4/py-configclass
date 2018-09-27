class ConfigField():
    def __init__(self, source=None):
        self.source = source
        
    def validate(self, value):
        pass

class StringField(ConfigField):
    def __init__(self, max_length=None, regex=None, **kwargs):
        super(StringField, self).__init__(**kwargs)
        self.max_length = max_length
        self.regex = regex
        
    def validate(self, value):
        super(StringField, self).validate(value)
        assert isinstance(value, str), f"Must be string, was {value}"
        if self.max_length is not None:
            assert len(value) <= self.max_length
            
        if self.regex is not None:
            print("TODO regex validation")
            
class IntField(ConfigField):
    def __init__(self, min=None, max=None, regex=None, **kwargs):
        super(IntField, self).__init__(**kwargs)
        self.min = min
        self.max = max
        
    def validate(self, value):
        super(IntField, self).validate(value)
        assert isinstance(value, int), f"Must be integer, was {value}"
        if self.max is not None:
            assert value <= self.max
            
        if self.min is not None:
            assert value >= self.min
