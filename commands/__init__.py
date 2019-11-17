def register_commands(app):
    from .database import database_cli

    app.cli.add_command(database_cli)
