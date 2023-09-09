import os


def get_volumes():
    volumes = []
    for volume in os.walk('static/volumes'):
        volumes.append(volume)
    return volumes
