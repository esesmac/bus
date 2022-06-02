import json
import requests as requests


def request_routes():
    resp = requests.get("https://svc.metrotransit.org/nextripv2/routes")
    data = json.loads(resp.text)
    return data


def request_directions(route_id):
    resp = requests.get("https://svc.metrotransit.org/nextripv2/directions/" + route_id)
    data = json.loads(resp.text)
    return data


def request_stops(route_id, direction_id):
    resp = requests.get("https://svc.metrotransit.org/nextripv2/stops/" + str(route_id) + "/" + str(direction_id))
    data = json.loads(resp.text)
    return data


def request_trip(route_id, direction_id, place_code):
    resp = requests.get("https://svc.metrotransit.org/nextripv2/" + str(route_id) + "/" + str(direction_id) + "/" + place_code)
    data = json.loads(resp.text)
    return data
