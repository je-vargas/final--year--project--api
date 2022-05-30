"""280322_1457_Linked_category_and_industry

Revision ID: 8a1bd54c60b8
Revises: 63d5987c1a56
Create Date: 2022-03-28 14:57:36.140864

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table, column
from sqlalchemy import String, Integer

from app import models as tb


# revision identifiers, used by Alembic.
revision = '8a1bd54c60b8'
down_revision = '63d5987c1a56'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute("Delete from category")
    op.add_column('category', sa.Column('industry_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'category', 'industry', ['industry_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    category_table = table(
        tb.Category.__tablename__,
        sa.Column("category", String)
    )

    op.bulk_insert(category_table, 
    [
        {"category":"engineering"},
        {"category":"construction"},
        {"category":"health & social"},
        {"category":"education"},
        {"category":"legal occupations"},
        {"category":"management"},
        {"category":"IT occupations"},
        {"category":"catering"},
        {"category":"other"},
    ])

    op.drop_constraint(None, 'category', type_='foreignkey')
    op.drop_column('category', 'industry_id')
    # ### end Alembic commands ###