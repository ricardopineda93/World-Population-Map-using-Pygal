from pygal.maps.world import COUNTRIES

def get_country_code(country_name):
    '''Returns the pygal 2 digit country code for given country'''
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
        # If country is not found:
    return None


