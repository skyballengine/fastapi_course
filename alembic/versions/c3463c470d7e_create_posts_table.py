"""create posts table

Revision ID: c3463c470d7e
Revises: 
Create Date: 2022-04-21 13:29:59.375658

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "c3463c470d7e"
down_revision = None
branch_labels = None
depends_on = None

# define how to upgrade or update table
def upgrade():
    op.create_table(
        "posts",
        sa.Column("id", sa.Integer(), nullable=False, primary_key=True),
        sa.Column("title", sa.String(), nullable=False),
    )
    pass


# define how to roll back changes
def downgrade():
    op.drop_table("posts")
    pass
