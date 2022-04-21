"""add users table

Revision ID: cee326d09c65
Revises: b1bfe72abc11
Create Date: 2022-04-21 14:21:15.005705

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "cee326d09c65"
down_revision = "b1bfe72abc11"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("email", sa.String(), nullable=False),
        sa.Column("password", sa.String(), nullable=False),
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
    )
    pass


def downgrade():
    op.drop_table("users")
    pass
