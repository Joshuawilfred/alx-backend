#!/usr/bin/env python3
"""Basic Babel setup"""
from flask import Flask, request, render_template, g
from flask_babel import Babel
from typing import Dict, Union


class Config:
    """Config Class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[Dict, None]:
    """Get a user"""
    login_as = request.args.get('login_as')
    return users.get(int(login_as)) if login_as else None


@app.before_request
def before_request() -> None:
    """find a user if any, and set it as a global"""
    g.user = get_user()


@babel.localeselector
def get_locale() -> str:
    """Get locale"""
    url_locale = request.args.get('locale', '')
    if url_locale and url_locale in Config.LANGUAGES:
        return url_locale

    if g.user and g.user.get('locale') in Config.LANGUAGES:
        return g.user.get('locale')

    header_locale = request.headers.get('locale', '')
    if header_locale and header_locale in Config.LANGUAGES:
        return header_locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index() -> str:
    """Default route"""
    username = g.user.get('name') if g.user else None
    return render_template('5-index.html', username=username)


if __name__ == '__main__':
    app.run()
