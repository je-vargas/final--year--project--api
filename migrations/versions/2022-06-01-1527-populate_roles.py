"""Populate_Roles

Revision ID: a6204762934c
Revises: d08b747459b4
Create Date: 2022-06-01 15:27:07.105705

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table
from sqlalchemy import String, Integer

from app import models as tb


# revision identifiers, used by Alembic.
revision = 'a6204762934c'
down_revision = 'd08b747459b4'
branch_labels = None
depends_on = None


def upgrade():
    table = tb.Roles.__tablename__
    
    roles_table = sa.table(
        table,
        sa.Column("roles", String),
    )

    op.bulk_insert(roles_table, 
        [
            {"roles":"Volunteer"},
            {"roles":"Employer"},
            {"roles":"Recruiter"},
        ])



def downgrade():
    op.execute("Delete from roles")
