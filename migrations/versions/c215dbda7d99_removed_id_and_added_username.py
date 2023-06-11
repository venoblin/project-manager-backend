"""removed id and added username

Revision ID: c215dbda7d99
Revises: e7f21332208b
Create Date: 2023-06-04 20:43:52.264642

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c215dbda7d99'
down_revision = 'e7f21332208b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('username', sa.String(length=80), nullable=False))
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(length=80),
               nullable=False)
        batch_op.alter_column('email',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)
        batch_op.alter_column('password',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)
        batch_op.drop_column('id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False))
        batch_op.alter_column('password',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)
        batch_op.alter_column('email',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(length=80),
               nullable=True)
        batch_op.drop_column('username')

    # ### end Alembic commands ###