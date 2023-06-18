"""Added githuburl

Revision ID: ce84d1369b70
Revises: d5e1e357b4b3
Create Date: 2023-06-18 15:03:58.866887

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ce84d1369b70'
down_revision = 'd5e1e357b4b3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('projects', schema=None) as batch_op:
        batch_op.drop_column('name')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('projects', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.VARCHAR(length=80), autoincrement=False, nullable=False))

    # ### end Alembic commands ###