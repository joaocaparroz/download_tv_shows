import os
import re


def check_already_downloaded_episodes(show_folder: str) -> list:
    file_list = []

    for r, d, f in os.walk(show_folder):
        for file in f:
            if file.endswith(".mkv"):
                file_list.append(file)

    p = re.compile(r'S(\d{1,2})E(\d{1,2})')

    episodes_list = []

    for fi in file_list:
        m = p.search(fi)
        episodes_list.append({
            'season': int(m.group(1)),
            'episode': int(m.group(2))
        })

    return episodes_list
