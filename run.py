""" This file runs the app."""

from app.views.app_views import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)