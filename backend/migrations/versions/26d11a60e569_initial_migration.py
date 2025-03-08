"""Initial migration

Revision ID: 26d11a60e569
Revises: 3b20c8fad346
Create Date: 2025-03-08 09:15:49.167892

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '26d11a60e569'
down_revision = '3b20c8fad346'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('verification', schema=None) as batch_op:
        batch_op.add_column(sa.Column('candidate_id', sa.Integer(), nullable=False))
        batch_op.drop_constraint('verification_Candidate_id_fkey', type_='foreignkey')
        batch_op.create_foreign_key(None, 'candidate', ['candidate_id'], ['id'])
        batch_op.drop_column('Candidate_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('verification', schema=None) as batch_op:
        batch_op.add_column(sa.Column('Candidate_id', sa.INTEGER(), autoincrement=False, nullable=False))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('verification_Candidate_id_fkey', 'candidate', ['Candidate_id'], ['id'])
        batch_op.drop_column('candidate_id')

    # ### end Alembic commands ###
