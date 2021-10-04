import click, os

def register(app):
    @app.cli.group()
    def blueprint():
        """Blueprint creation commands"""
        pass
    @blueprint.command()
    @click.argument('name')
    def create(name):
        """Create new flask Blueprint"""
        basedir = os.path.abspath(os.path.dirname(__name__)) + f'/app/blueprints/{name}'

        try:
            if not os.path.exists(basedir):
                os.makedirs(basedir)
                init_file = open(f'{basedir}/__init__.py', 'w')
                init_file.close()
                models_file = open(f'{basedir}/models.py', 'w')
                models_file.close()
                routes_file = open(f'{basedir}/routes.py', 'w')
                routes_file.close()
        except Exception as error:
            print(f"Something went wrong with creating the blueprint called {name}")
            print(error)
        return print("Blueprint created successfully")
        