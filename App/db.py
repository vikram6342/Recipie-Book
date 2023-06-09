from flask import g, current_app

import sqlite3
import click


def get_db():
    if g.db is None:
        db = sqlite3.connect(
            current_app.config["DATABASE"],
            detect_types= sqlite3.PARSE_DECLTYPES
            )
        g.db.row_factory = sqlite3.Row

    return g.db

