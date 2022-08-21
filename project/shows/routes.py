import os
from typing import Any

import requests
from dotenv import load_dotenv
from flask import current_app, render_template, request, session, flash, redirect, url_for

from . import shows_blueprint

load_dotenv("env")


@shows_blueprint.route("/")
def index():
    return render_template("shows/index.html")


@shows_blueprint.route("/search_shows")
def search_shows() -> requests.Response:
    api_key, version = map(os.getenv, ["API_KEY", "API_VERSION"])
    params = {
        "api_key": api_key,
        "query": request.query
    }
    if request.method == "GET":
        url = f"https://api.themoviedb.org/3/search/{request.media_type}?"
        resp = requests.request(
            "get", url, params=params
        )
        return resp.json()["results"]

