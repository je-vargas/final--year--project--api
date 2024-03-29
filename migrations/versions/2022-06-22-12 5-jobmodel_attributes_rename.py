"""JobModel_attributes_rename

Revision ID: 605b327f8d17
Revises: fec06faf254d
Create Date: 2022-06-22 12:05:29.565356

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '605b327f8d17'
down_revision = 'fec06faf254d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('jobs', sa.Column('description', sa.String(), nullable=True))
    op.add_column('jobs', sa.Column('title', sa.String(), nullable=True))
    op.drop_column('jobs', 'jobDescription')
    op.drop_column('jobs', 'jobTitle')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('jobs', sa.Column('jobTitle', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('jobs', sa.Column('jobDescription', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_column('jobs', 'title')
    op.drop_column('jobs', 'description')
    # ### end Alembic commands ###
