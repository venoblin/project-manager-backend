"""created events

Revision ID: ee42c183b630
Revises: d1220a65cd68
Create Date: 2023-11-30 21:10:23.858791

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ee42c183b630'
down_revision = 'd1220a65cd68'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('bugs', schema=None) as batch_op:
        batch_op.alter_column('bug_info',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)

    with op.batch_alter_table('projects', schema=None) as batch_op:
        batch_op.alter_column('git_url',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('projects', schema=None) as batch_op:
        batch_op.alter_column('git_url',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)

    with op.batch_alter_table('bugs', schema=None) as batch_op:
        batch_op.alter_column('bug_info',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)

    # ### end Alembic commands ###