"""removed columns

Revision ID: 72dece329f10
Revises: d6ce031db9d3
Create Date: 2024-01-08 20:48:34.440346

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '72dece329f10'
down_revision = 'd6ce031db9d3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('bugs', schema=None) as batch_op:
        batch_op.drop_column('completed')
        batch_op.drop_column('completed_at')

    with op.batch_alter_table('todos', schema=None) as batch_op:
        batch_op.drop_column('completed')
        batch_op.drop_column('completed_at')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('todos', schema=None) as batch_op:
        batch_op.add_column(sa.Column('completed_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('completed', sa.BOOLEAN(), autoincrement=False, nullable=True))

    with op.batch_alter_table('bugs', schema=None) as batch_op:
        batch_op.add_column(sa.Column('completed_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('completed', sa.BOOLEAN(), autoincrement=False, nullable=True))

    # ### end Alembic commands ###
