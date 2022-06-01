"""Populate_Category&Industry_Tables

Revision ID: 4e9b8217de77
Revises: e9dc1fb108a7
Create Date: 2022-06-01 15:07:39.346172

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table
from sqlalchemy import String

from app import models as tb


# revision identifiers, used by Alembic.
revision = '4e9b8217de77'
down_revision = 'e9dc1fb108a7'
branch_labels = None
depends_on = None


def upgrade():
    industry_table = table(
            tb.Industry.__tablename__,
            sa.Column("industry", String)
        )

    op.bulk_insert(industry_table, 
        [
            {"industry":"Aviation"},
            {"industry":"Arts"},
            {"industry":"Business"},
            {"industry":"Construction"},
            {"industry":"Education"},
            {"industry":"Law Enforcement"},
            {"industry":"Media"},
            {"industry":"Medical"},
            {"industry":"Service Industry"},
            {"industry":"Technology"},
            {"industry":"Hospitality"},
            {"industry":"Engineering"},
        ])

def downgrade():
    op.execute("Delete from industry")

