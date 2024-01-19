from alembic import context
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
import os
import sys

# Add the directory containing your models package to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from models import Base

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(os.path.join(os.path.dirname(__file__), "alembic.ini"))

# add your model's MetaData object here
# for 'autogenerate' support
target_metadata = Base.metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    # Load the models and sort them based on foreign key dependencies
    models = [Base.metadata.tables[name] for name in Base.metadata.tables.keys()]
    models.sort(
        key=lambda table: [
            fk.columns[0].table.name for fk in table.foreign_key_constraints
        ]
    )
    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        # Load the models and sort them based on foreign key dependencies
        models = [Base.metadata.tables[name] for name in Base.metadata.tables.keys()]
        models.sort(
            key=lambda table: [
                fk.columns[0].table.name for fk in table.foreign_key_constraints
            ]
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
