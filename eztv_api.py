import logging
import re
import os

import requests
from clutch import Client
from clutch.method.torrent import TorrentAddArguments

TRANSMISSION_ADDRESS = os.getenv('TRANSMISSION_ADDRESS')
TRANSMISSION_USERNAME = os.getenv('TRANSMISSION_USERNAME')
TRANSMISSION_PASSWORD = os.getenv('TRANSMISSION_PASSWORD')
DOWNLOAD_DIR = os.getenv('DOWNLOAD_DIR')


def download_needed_episodes(already_downloaded_episodes_list: list, imdb_id: int, filters: list):
    torrents = get_tv_show_torrents(imdb_id)
    torrents = filter_torrents(filters, torrents)
    torrents = remove_already_downloaded_torrents(already_downloaded_episodes_list, torrents)

    client = Client(address=TRANSMISSION_ADDRESS, username=TRANSMISSION_USERNAME, password=TRANSMISSION_PASSWORD)

    torrents = remove_downloading_torrents(client, torrents)

    for torrent in torrents:
        arguments: TorrentAddArguments = {
            "download_dir": f"{DOWNLOAD_DIR}/{re.sub('.mkv', '', torrent['filename'])}",
            "paused": False,
            "filename": torrent['magnet_url']
        }
        client.torrent.add(arguments)
        logging.info(f"Added torrent {torrent['filename']}")


def get_tv_show_torrents(imdb_id: int) -> list:
    url = 'https://eztv.re/api/get-torrents'

    params = {
        'imdb_id': imdb_id,
        'limit': 100
    }

    response = requests.get(url, params)
    response_json = response.json()

    torrents = response_json.get('torrents')

    while response_json['limit'] == len(response_json['torrents']):
        page = response_json['page'] + 1
        params.update({
            'page': page
        })

        response = requests.get(url, params)
        response_json = response.json()

        torrents += response_json.get('torrents')

    return torrents


def filter_torrents(filters: list, torrents: list) -> list:
    for fil in filters:
        torrents = [x for x in torrents if fil in x['filename']]

    return torrents


def remove_already_downloaded_torrents(already_downloaded_torrents: list, torrents: list) -> list:
    for ep in already_downloaded_torrents:
        torrents = [x for x in torrents if (ep['season'] != int(x['season']) or ep['episode'] != int(x['episode']))]

    return torrents


def remove_downloading_torrents(transmission_client: Client, torrents: list) -> list:
    response = transmission_client.torrent.accessor(all_fields=True)
    transmission_torrents = response.arguments.torrents
    for torrent in transmission_torrents:
        torrents = [x for x in torrents if x['filename'] != torrent.name]

    return torrents
