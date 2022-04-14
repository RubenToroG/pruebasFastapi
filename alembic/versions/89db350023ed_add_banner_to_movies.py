"""Add Banner to movies

Revision ID: 89db350023ed
Revises: cb7bbb5f4da1
Create Date: 2022-04-13 21:15:14.878220

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '89db350023ed'
down_revision = 'cb7bbb5f4da1'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        'movies',
        sa.Column('banner', sa.String)
    )


def downgrade():
    op.drop_column('banner')
