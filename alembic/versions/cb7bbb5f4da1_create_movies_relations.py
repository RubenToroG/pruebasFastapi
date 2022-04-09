"""Create movies relations

Revision ID: cb7bbb5f4da1
Revises: 63253ed36cc8
Create Date: 2022-04-07 21:29:25.654810

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import ForeignKey


# revision identifiers, used by Alembic.
revision = 'cb7bbb5f4da1'
down_revision = '63253ed36cc8'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'screenwriters',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('first_name',sa.String),
        sa.Column('last_name',sa.String)
    )

    op.create_table(
        'producers',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('first_name',sa.String),
        sa.Column('last_name',sa.String)
    )

    op.create_table(
        'movies_screenwriters',
        sa.Column('id_movie', sa.Integer,sa.ForeignKey('movies.id') ,primary_key=True),
        sa.Column('id_screenwriter',sa.Integer, sa.ForeignKey('screenwriters.id'), primary_key=True),
    )

    op.create_table(
        'movies_producers',
        sa.Column('id_movie', sa.Integer, sa.ForeignKey('movies.id'), primary_key=True),
        sa.Column('id_producer',sa.Integer, sa.ForeignKey('producers.id'), primary_key=True)
    )

    op.create_table(
        'view_movie',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('id_user', sa.Integer, sa.ForeignKey('users.id')),
        sa.Column('id_movie', sa.Integer, sa.ForeignKey('movies.id')),
        sa.Column('user_score', sa.Float),
        sa.UniqueConstraint('id_user', 'id_movie')
    )

def downgrade():
    op.drop_table('view_movie')
    op.drop_table('movies_producers')
    op.drop_table('movies_screenwriters')
    op.drop_table('producers')
    op.drop_table('screenwriters')
    
