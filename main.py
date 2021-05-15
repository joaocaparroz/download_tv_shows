import logging

import joblib

from eztv_api import download_needed_episodes
from os_functions import check_already_downloaded_episodes

logging.basicConfig(level=logging.INFO)


def main(tv_shows_list: list):
    logging.info('Starting script...')
    for tv_show in tv_shows_list:
        logging.info(f"Processing {tv_show['name']}")
        process_tv_show(tv_show)

    logging.info('Script successfully finished...')


def process_tv_show(tv_show: dict):
    already_downloaded_episodes_list = check_already_downloaded_episodes(tv_show['folder'])
    download_needed_episodes(already_downloaded_episodes_list, tv_show['imdb_id'], tv_show.get('filters'))


if __name__ == '__main__':
    tv_shows = joblib.load('data/tv_shows.joblib')
    main(tv_shows)
