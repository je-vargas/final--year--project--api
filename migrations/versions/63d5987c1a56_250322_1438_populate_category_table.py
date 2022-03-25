"""250322.1438_populate_category_table

Revision ID: 63d5987c1a56
Revises: d3cb7b1f1aab
Create Date: 2022-03-25 14:42:25.838019

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.sql import table, column
from sqlalchemy import String, Integer

from app import models as tb


# revision identifiers, used by Alembic.
revision = '63d5987c1a56'
down_revision = 'd3cb7b1f1aab'
branch_labels = None
depends_on = None


def upgrade():

    print("\n")
    print(type(tb.Category.__tablename__))
    print("\n")

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

def downgrade():
    op.execute("Delete from category")
