"""Table

Revision ID: 83506a738bf1
Revises: 
Create Date: 2023-04-21 15:12:14.351833

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '83506a738bf1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('full_name', sa.String(length=20), nullable=False),
    sa.Column('program', sa.String(length=20), nullable=False),
    sa.Column('year', sa.String(length=20), nullable=False),
    sa.Column('sr_code', sa.String(length=60), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('image_upload', sa.String(length=20), nullable=False),
    sa.Column('contact_person', sa.String(length=20), nullable=False),
    sa.Column('address', sa.String(length=20), nullable=False),
    sa.Column('contact_number', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('address'),
    sa.UniqueConstraint('contact_number'),
    sa.UniqueConstraint('contact_person'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('full_name'),
    sa.UniqueConstraint('program'),
    sa.UniqueConstraint('sr_code'),
    sa.UniqueConstraint('year')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
