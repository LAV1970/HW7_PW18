"""Добавить group_id в students

Revision ID: 20240111_01
Revises: <previous_revision_id>  # Укажите здесь предыдущий ID миграции, если есть
Create Date: 2024-01-11  # Укажите текущую дату

"""

from alembic import op
import sqlalchemy as sa


# Изменения вперед (при обновлении)
def upgrade():
    op.add_column("students", sa.Column("group_id", sa.Integer(), nullable=True))
    op.create_foreign_key(
        "fk_students_group_id", "students", "groups", ["group_id"], ["id"]
    )


# Изменения назад (при откате)
def downgrade():
    op.drop_constraint("fk_students_group_id", "students", type_="foreignkey")
    op.drop_column("students", "group_id")
