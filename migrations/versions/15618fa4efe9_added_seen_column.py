"""added seen column

Revision ID: 15618fa4efe9
Revises: 230ee1a73a7e
Create Date: 2024-01-14 23:35:36.019915

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '15618fa4efe9'
down_revision = '230ee1a73a7e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('notifications', schema=None) as batch_op:
        batch_op.add_column(sa.Column('seen', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('notifications', schema=None) as batch_op:
        batch_op.drop_column('seen')

    # ### end Alembic commands ###
