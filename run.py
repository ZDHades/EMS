from flask import current_app as app
from app import create_app, cli, db

app = create_app()
cli.register(app)

@app.shell_context_processor
def shell_context():
    return {}
    