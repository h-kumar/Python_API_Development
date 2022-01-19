"""add content column to posts

Revision ID: 33550cbb7f42
Revises: bf90fa6e91c0
Create Date: 2022-01-19 23:38:23.203238

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '33550cbb7f42'
down_revision = 'bf90fa6e91c0'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content',sa.String(),nullable=False))
    pass


def downgrade():
    op.drop_column('posts','content')
    pass
