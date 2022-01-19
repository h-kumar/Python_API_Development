"""create post table

Revision ID: bf90fa6e91c0
Revises: 
Create Date: 2022-01-19 23:22:48.954085

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bf90fa6e91c0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts',
                    sa.Column('id', sa.Integer(),
                              nullable=False,
                              primary_key=True),
                    sa.Column('title',sa.String(),nullable=False))
    pass


def downgrade():
    op.drop_table('posts')
    pass
