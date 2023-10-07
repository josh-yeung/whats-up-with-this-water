
from geopy.geocoders import Nominatim
from shapely.ops import nearest_points

def country_lookup(query, geocoder, land_geometry):
    
    try:
        loc = geocoder.reverse((query.y, query.x))
        return loc.raw['address']['country']
    except (KeyError, AttributeError):
        _, p2 = nearest_points(query, land_geometry)
        loc = geocoder.reverse((p2.y, p2.x)).raw['address']
        if 'country' in loc.keys():
            return loc['country']
        else:
            return loc['locality']
        
# get world (or any land) geometry, instantiate geolocator service
world = gp.read_file(gp.datasets.get_path('naturalearth_lowres'))
world_geometry = world.geometry.unary_union
geolocator = Nominatim(user_agent="GIW")

# Create a column of country names from points in a GDF's geometry.
gdf['country'] = gdf.geometry.apply(country_lookup, args=(geolocator, world_geometry))