"""add content column to posts table

Revision ID: b1bfe72abc11
Revises: c3463c470d7e
Create Date: 2022-04-21 13:50:42.261522

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "b1bfe72abc11"
down_revision = "c3463c470d7e"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column("posts", "content")
    pass
