"""associated bugs-project

Revision ID: 8e3d2e8ce7f7
Revises: 7c794b9478a7
Create Date: 2023-06-19 22:21:29.907211

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8e3d2e8ce7f7'
down_revision = '7c794b9478a7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('bugs', schema=None) as batch_op:
        batch_op.add_column(sa.Column('project_id', sa.Integer(), nullable=False))
        batch_op.create_foreign_key(None, 'projects', ['project_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('bugs', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('project_id')

    # ### end Alembic commands ###
