"""update_users_user_profile_facilities

Revision ID: 179b8025fb43
Revises: 5e5c265e9ef2
Create Date: 2025-10-22 12:55:21.684152
"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = "179b8025fb43"
down_revision: Union[str, Sequence[str], None] = "5e5c265e9ef2"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema safely."""
    conn = op.get_bind()

    # Drop foreign key and columns if they exist
    with op.batch_alter_table("user_profiles", schema=None) as batch_op:
        inspector = sa.inspect(conn)
        columns = [col["name"] for col in inspector.get_columns("user_profiles")]
        fks = [fk["name"] for fk in inspector.get_foreign_keys("user_profiles")]

        if "user_profiles_ibfk_1" in fks:
            batch_op.drop_constraint("user_profiles_ibfk_1", type_="foreignkey")

        if "cadre_id" in columns:
            batch_op.drop_column("cadre_id")

        if "other_names" in columns:
            batch_op.drop_column("other_names")

        if "country" not in columns:
            batch_op.add_column(sa.Column("country", sa.String(length=50), nullable=False))

    # Drop indexes and table only if they exist
    inspector = sa.inspect(conn)
    if "cadres" in inspector.get_table_names():
        indexes = [idx["name"] for idx in inspector.get_indexes("cadres")]
        if "ix_cadres_id" in indexes:
            op.drop_index("ix_cadres_id", table_name="cadres")
        if "name" in indexes:
            op.drop_index("name", table_name="cadres")
        op.drop_table("cadres")


def downgrade() -> None:
    """Downgrade schema."""
    # Recreate cadres table
    op.create_table(
        "cadres",
        sa.Column("name", mysql.VARCHAR(length=100), nullable=False),
        sa.Column("id", mysql.VARCHAR(length=36), nullable=False),
        sa.Column("created_at", mysql.DATETIME(), nullable=False),
        sa.Column("updated_at", mysql.DATETIME(), nullable=False),
        sa.Column("is_deleted", mysql.TINYINT(display_width=1), autoincrement=False, nullable=True),
        sa.Column("deleted_at", mysql.DATETIME(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        mysql_collate="utf8mb4_general_ci",
        mysql_default_charset="utf8mb4",
        mysql_engine="InnoDB",
    )
    op.create_index(op.f("name"), "cadres", ["name"], unique=True)
    op.create_index(op.f("ix_cadres_id"), "cadres", ["id"], unique=True)

    # Recreate columns and constraints in user_profiles
    with op.batch_alter_table("user_profiles") as batch_op:
        batch_op.drop_column("country")
        batch_op.add_column(sa.Column("other_names", mysql.VARCHAR(length=50), nullable=True))
        batch_op.add_column(sa.Column("cadre_id", mysql.VARCHAR(length=36), nullable=True))
        batch_op.create_foreign_key(
            op.f("user_profiles_ibfk_1"),
            "cadres",
            ["cadre_id"],
            ["id"],
            onupdate="CASCADE",
            ondelete="SET NULL",
        )
