"""populate roles

Revision ID: 5f96e827c179
Revises: 5bc0cee5ef94
Create Date: 2022-06-02 17:13:24.282893

"""
from alembic import op
import sqlalchemy as sa

from sqlalchemy.sql import table
from sqlalchemy import String

from app import models as tb


# revision identifiers, used by Alembic.
revision = '5f96e827c179'
down_revision = '5bc0cee5ef94'
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
            {"roles":"volunteer"},
            {"roles":"employeer"},
            {"roles":"recruiter"},
        ])



def downgrade():
    op.execute("Delete from roles")
