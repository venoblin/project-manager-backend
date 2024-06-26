"""added notification and project relationship

Revision ID: 554b85ceccfc
Revises: 6b5edada6d05
Create Date: 2024-05-23 22:52:54.818170

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '554b85ceccfc'
down_revision = '6b5edada6d05'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('notifications', schema=None) as batch_op:
        batch_op.add_column(sa.Column('project_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'projects', ['project_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('notifications', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('project_id')

    # ### end Alembic commands ###
