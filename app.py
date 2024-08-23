from true_api import create_app
from true_api.extensions import db
from flask.cli import FlaskGroup

app = create_app()
cli = FlaskGroup(app)

@app.cli.command("create-db")
def create_db():
    """Creates the db tables."""
    db.create_all()

@app.cli.command("drop-db")
def drop_db():
    """Drops the db tables."""
    db.drop_all()

if __name__ == '__main__':
    cli()