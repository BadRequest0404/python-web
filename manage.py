from app import create_app
from app import db, User, Task

from flask.cli import FlaskGroup
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from config import config

config_class = config['development']
app = create_app(config_class)
migrate = Migrate(app, db)

@app.shell_context_processor
def make_shell_context():
    return dict(app=app, db=db, User=User, Task=Task)

@app.cli.command("test")
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)

if __name__ == '__main__':
    app.run(debug=True)
