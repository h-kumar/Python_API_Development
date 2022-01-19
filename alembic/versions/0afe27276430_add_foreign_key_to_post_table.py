"""add foreign key to post table

Revision ID: 0afe27276430
Revises: 6d18240506a3
Create Date: 2022-01-19 23:57:35.512356

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0afe27276430'
down_revision = '6d18240506a3'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer, nullable=False))
    op.create_foreign_key('posts_users_fkey',
                          source_table='posts',
                          referent_table='users',
                          local_cols=['owner_id'],
                          remote_cols=['id'],
                          ondelete='CASCADE')
    pass


def downgrade():
    op.drop_constraint('posts_users_fkey',table_name='posts')
    op.drop_column('posts','owner_id')
    pass
