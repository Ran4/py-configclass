import anyconfig
from config_fields import ConfigField

class ConfigurationError(Exception):
    pass

class ConfigurationValidationError(ConfigurationError):
    pass


class Config:
    def __init__(self, filename: str=None, validate: bool=True):
        if filename is None:
            filename = self.Meta.default_filename
        
        self.filename = filename
        try:
            self.dict = anyconfig.load(filename, ac_parser="toml")
        except FileNotFoundError as e:
            print("TODO create default file")
            raise e
        
        self._inject_config_into_self(validate)
        
    def __str__(self):
        fields = list(self._fields.keys())
        return f"<Config fields={fields}]>"
        
    def _inject_config_into_self(self, validate: bool):
        # Replace each config field
        self._fields = {}
        field_names = [f for f in dir(self) if not f.startswith("_")]
        for field_name in field_names:
            field = self.__getattribute__(field_name)
            if isinstance(field, ConfigField):
                value = self._inject_field_into_self(field, field_name)
                if validate:
                    field.validate(value)
                    
    def _inject_field_into_self(self, field, field_name):
        #if field.source...
        source = field.source if field.source is not None else field_name
        try:
            value = self.dict[source]
        except KeyError as e:
            missing_var = e.args[0]
            msg = f"Configuration is missing mandatory variable `{missing_var}`"
            raise ConfigurationError(msg) from None
        self.__setattr__(field_name, value)
        self._fields[field_name] = field
        return value
            
    def save(self, filename=None):
        with open(filename or self.filename, "w") as f:
            anyconfig.dump(self.dict, f)

