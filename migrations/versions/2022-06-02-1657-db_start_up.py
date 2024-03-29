"""db_start_up

Revision ID: 0ce3fd999bd6
Revises: 
Create Date: 2022-06-02 16:57:16.665280

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0ce3fd999bd6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('industry',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('industry', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_industry_id'), 'industry', ['id'], unique=False)
    op.create_table('roles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('roles', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('roles')
    )
    op.create_index(op.f('ix_roles_id'), 'roles', ['id'], unique=False)
    op.create_table('test',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('firstname', sa.String(), nullable=False),
    sa.Column('lastname', sa.String(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('createdOn', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_test_id'), 'test', ['id'], unique=False)
    op.create_table('userAccount',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('firstName', sa.String(), nullable=False),
    sa.Column('lastName', sa.String(), nullable=False),
    sa.Column('telephoneNumber', sa.String(), nullable=False),
    sa.Column('dateCreated', sa.DateTime(timezone=True), nullable=False),
    sa.Column('lastLogin', sa.DateTime(timezone=True), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('telephoneNumber')
    )
    op.create_index(op.f('ix_userAccount_id'), 'userAccount', ['id'], unique=False)
    op.create_table('accountRoles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('userAccountId', sa.Integer(), nullable=False),
    sa.Column('roles_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['roles_id'], ['roles.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['userAccountId'], ['userAccount.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_accountRoles_id'), 'accountRoles', ['id'], unique=False)
    op.create_table('category',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('category', sa.String(), nullable=False),
    sa.Column('industry_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['industry_id'], ['industry.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('category')
    )
    op.create_index(op.f('ix_category_id'), 'category', ['id'], unique=False)
    op.create_table('companyDetails',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('companyName', sa.String(), nullable=False),
    sa.Column('companyDescription', sa.String(), nullable=True),
    sa.Column('industry_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['industry_id'], ['industry.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_companyDetails_id'), 'companyDetails', ['id'], unique=False)
    op.create_table('volunteerCV',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('userAccount_id', sa.Integer(), nullable=False),
    sa.Column('cv', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['userAccount_id'], ['userAccount.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('cv')
    )
    op.create_index(op.f('ix_volunteerCV_id'), 'volunteerCV', ['id'], unique=False)
    op.create_table('volunteerSkills',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('userAccount_id', sa.Integer(), nullable=False),
    sa.Column('experience', sa.String(), nullable=True),
    sa.Column('fieldOfStudy', sa.String(), nullable=True),
    sa.Column('degree', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['userAccount_id'], ['userAccount.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_volunteerSkills_id'), 'volunteerSkills', ['id'], unique=False)
    op.create_table('companyRepresentative',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('company_id', sa.Integer(), nullable=False),
    sa.Column('userAccount_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['company_id'], ['companyDetails.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['userAccount_id'], ['userAccount.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_companyRepresentative_id'), 'companyRepresentative', ['id'], unique=False)
    op.create_table('jobs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('employer_id', sa.Integer(), nullable=True),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.Column('jobDescription', sa.String(), nullable=False),
    sa.Column('jobTitle', sa.String(), nullable=False),
    sa.Column('numberOfPositions', sa.Integer(), nullable=False),
    sa.Column('onGoingFill', sa.Boolean(), nullable=False),
    sa.Column('startDate', sa.Date(), nullable=True),
    sa.Column('endDate', sa.Date(), nullable=True),
    sa.Column('applicationDeadline', sa.Date(), nullable=True),
    sa.Column('workHours', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['category.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['employer_id'], ['companyRepresentative.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_jobs_category_id'), 'jobs', ['category_id'], unique=False)
    op.create_index(op.f('ix_jobs_employer_id'), 'jobs', ['employer_id'], unique=False)
    op.create_index(op.f('ix_jobs_id'), 'jobs', ['id'], unique=False)
    op.create_table('userVolunteeringHistory',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('job_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['job_id'], ['jobs.id'], ondelete='RESTRICT'),
    sa.ForeignKeyConstraint(['user_id'], ['userAccount.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_userVolunteeringHistory_id'), 'userVolunteeringHistory', ['id'], unique=False)
    op.create_index(op.f('ix_userVolunteeringHistory_job_id'), 'userVolunteeringHistory', ['job_id'], unique=False)
    op.create_index(op.f('ix_userVolunteeringHistory_user_id'), 'userVolunteeringHistory', ['user_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_userVolunteeringHistory_user_id'), table_name='userVolunteeringHistory')
    op.drop_index(op.f('ix_userVolunteeringHistory_job_id'), table_name='userVolunteeringHistory')
    op.drop_index(op.f('ix_userVolunteeringHistory_id'), table_name='userVolunteeringHistory')
    op.drop_table('userVolunteeringHistory')
    op.drop_index(op.f('ix_jobs_id'), table_name='jobs')
    op.drop_index(op.f('ix_jobs_employer_id'), table_name='jobs')
    op.drop_index(op.f('ix_jobs_category_id'), table_name='jobs')
    op.drop_table('jobs')
    op.drop_index(op.f('ix_companyRepresentative_id'), table_name='companyRepresentative')
    op.drop_table('companyRepresentative')
    op.drop_index(op.f('ix_volunteerSkills_id'), table_name='volunteerSkills')
    op.drop_table('volunteerSkills')
    op.drop_index(op.f('ix_volunteerCV_id'), table_name='volunteerCV')
    op.drop_table('volunteerCV')
    op.drop_index(op.f('ix_companyDetails_id'), table_name='companyDetails')
    op.drop_table('companyDetails')
    op.drop_index(op.f('ix_category_id'), table_name='category')
    op.drop_table('category')
    op.drop_index(op.f('ix_accountRoles_id'), table_name='accountRoles')
    op.drop_table('accountRoles')
    op.drop_index(op.f('ix_userAccount_id'), table_name='userAccount')
    op.drop_table('userAccount')
    op.drop_index(op.f('ix_test_id'), table_name='test')
    op.drop_table('test')
    op.drop_index(op.f('ix_roles_id'), table_name='roles')
    op.drop_table('roles')
    op.drop_index(op.f('ix_industry_id'), table_name='industry')
    op.drop_table('industry')
    # ### end Alembic commands ###
