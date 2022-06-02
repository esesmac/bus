import sys

import Services
import TransitLogic
from NextTrip import NextTrip


def main(argv):
    route_name = argv[1]
    direction_name = argv[3]
    stop_name = argv[2]
    routes = Services.request_routes()
    next_trip = NextTrip()
    next_trip.routeId = TransitLogic.get_route_id(routes, route_name)
    print(next_trip.routeId)
    directions = Services.request_directions(next_trip.routeId)
    next_trip.directionId = TransitLogic.search_data(direction_name, "direction_name", "direction_id", directions)
    print(next_trip.directionId)
    stops = Services.request_stops(next_trip.routeId, next_trip.directionId)
    next_trip.stopId = TransitLogic.search_data(stop_name, "description", "place_code", stops)
    print(next_trip.stopId)
    route_stops = Services.request_trip(next_trip.routeId, next_trip.directionId, next_trip.stopId)
    next_departure_text = TransitLogic.search_data(True, "actual", "departure_text", route_stops["departures"])
    print(next_departure_text)


if __name__ == "__main__":
    main(sys.argv)


