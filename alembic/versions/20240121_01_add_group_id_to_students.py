"""Добавить group_id в students

Revision ID: 20240121_01
Revises: <previous_revision_id>  # Укажите здесь предыдущий ID миграции, если есть
Create Date: 2024-01-21  # Укажите текущую дату

"""
# явное указание revision
revision = "20240121_01"
down_revision = None  # Укажите здесь предыдущий ID миграции, если есть

from alembic import op
import sqlalchemy as sa

# Уникальный идентификатор для миграции
revision_id = "20240121_01"


# Изменения вперед (при обновлении)
def upgrade():
    # Проверяем, существует ли колонка "group_id" перед её добавлением
    conn = op.get_bind()
    inspector = sa.inspect(conn)
    columns = inspector.get_columns("students")
    group_id_exists = any(column["name"] == "group_id" for column in columns)

    if not group_id_exists:
        op.add_column("students", sa.Column("group_id", sa.Integer(), nullable=True))
        op.create_foreign_key(
            "fk_students_group_id", "students", "groups", ["group_id"], ["id"]
        )
    else:
        print("Column 'group_id' already exists in table 'students'. Skipping...")


# Изменения назад (при откате)
def downgrade():
    op.drop_constraint("fk_students_group_id", "students", type_="foreignkey")
    op.drop_column("students", "group_id")
