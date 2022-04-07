"""create_movies

Revision ID: 63253ed36cc8
Revises: 
Create Date: 2022-04-07 10:56:40.069707

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '63253ed36cc8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'movies',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('title', sa.String, index=True, unique=True),
        sa.Column('original_title', sa.String, index=True, unique=True),
        sa.Column('romanised_title', sa.String, index=True, unique=True),
        sa.Column('release_year', sa.Integer),
        sa.Column('wiki_link', sa.Text),
        sa.Column('music', sa.String),
        sa.Column('duration', sa.Integer),
        sa.Column('cover', sa.Text)
    )


def downgrade():
    op.drop_table('movies')
