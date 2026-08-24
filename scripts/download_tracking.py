"""Descarga el dataset de tracking de SoccerNet."""

import os
from pathlib import Path

from SoccerNet.Downloader import SoccerNetDownloader

DEST = Path("data/raw/soccernet")
DEST.mkdir(parents=True, exist_ok=True)

dl = SoccerNetDownloader(LocalDirectory=str(DEST))

password = os.environ.get("SOCCERNET_PASSWORD")
if password:
    dl.password = password

# Empieza solo por 'test'. Añade 'train' cuando sepas que lo necesitas.
dl.downloadDataTask(task="tracking", split=["test"])
