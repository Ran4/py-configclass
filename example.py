import pprint
from typing import Dict

from config_class import Config
import config_fields

class LaykeConfig(Config):
    first_name = config_fields.StringField(max_length=14, regex="34,430", source="name")
    age = config_fields.IntField()
    
    class Meta:
        default_filename = "config.toml"

def main():
    conf = LaykeConfig()
    print(conf)
    #~ print("name:", conf.name)
    
if __name__ == "__main__":
    main()
