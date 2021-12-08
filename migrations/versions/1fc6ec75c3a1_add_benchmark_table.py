"""add benchmark table

Revision ID: 1fc6ec75c3a1
Revises: 48f06b6bbb8f
Create Date: 2021-12-08 09:42:48.625007

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1fc6ec75c3a1'
down_revision = '48f06b6bbb8f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('benchmark',
    sa.Column('id', sa.String(length=36), nullable=False),
    sa.Column('benchmark_id', sa.Integer(), nullable=True),
    sa.Column('backend', sa.String(length=1200), nullable=True),
    sa.Column('result', sa.String(length=1200), nullable=True),
    sa.Column('counts', sa.String(length=1200), nullable=True),
    sa.Column('shots', sa.Integer(), nullable=True),
    sa.Column('original_depth', sa.Integer(), nullable=True),
    sa.Column('original_width', sa.Integer(), nullable=True),
    sa.Column('transpiled_depth', sa.Integer(), nullable=True),
    sa.Column('transpiled_width', sa.Integer(), nullable=True),
    sa.Column('complete', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('benchmark')
    # ### end Alembic commands ###
