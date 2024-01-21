"""Добавить group_id в students

Revision ID: 20240121_01
Revises: <previous_revision_id>  # Укажите здесь предыдущий ID миграции, если есть
Create Date: 2024-01-21  # Укажите текущую дату

"""
# явное указание revision
revision = "20240121_01"
down_revision = "<20240111_01>"  # Укажите здесь предыдущий ID миграции, если есть

from alembic import op
import sqlalchemy as sa

# Уникальный идентификатор для миграции
revision_id = "20240121_01"


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
