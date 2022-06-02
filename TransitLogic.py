
def get_route_id(routes, route_name):
    for route in routes:
        current_route = route["route_label"]
        if current_route == route_name:
            return routes[0]["route_id"]


def search_data(value_to_search, parameter_to_search, parameter_to_get, items):
    for item in items:
        if item[parameter_to_search] == value_to_search:
            return item[parameter_to_get]
