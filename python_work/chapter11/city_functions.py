def city_function(country,city,population=''):
    if population:
        str = f"{country} , {city} , population {population}"
    else:
        str = f"{country} , {city}"
    return str.title()