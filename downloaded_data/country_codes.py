from pygal.maps.world import COUNTRIES
from pygal_maps_world import i18n

def get_country_code(country_name):
    ''' Returns the two digit country code '''
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
        # if the code wasn't found return none
    else:
        return None
