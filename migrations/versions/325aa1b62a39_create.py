"""create

Revision ID: 325aa1b62a39
Revises: 
Create Date: 2023-10-23 14:19:52.588539

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '325aa1b62a39'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('priority',
    sa.Column('priority_id', sa.Integer(), nullable=False),
    sa.Column('text', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('priority_id')
    )
    op.create_table('status',
    sa.Column('status_id', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('status_id')
    )
    op.create_table('user',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=64), nullable=False),
    sa.Column('last_name', sa.String(length=64), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password_hash', sa.String(length=128), nullable=False),
    sa.PrimaryKeyConstraint('user_id')
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_user_email'), ['email'], unique=True)
        batch_op.create_index(batch_op.f('ix_user_first_name'), ['first_name'], unique=False)
        batch_op.create_index(batch_op.f('ix_user_last_name'), ['last_name'], unique=False)

    op.create_table('project',
    sa.Column('project_id', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('deadline', sa.DateTime(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('status_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['status_id'], ['status.status_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], ),
    sa.PrimaryKeyConstraint('project_id')
    )
    op.create_table('task',
    sa.Column('task_id', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=False),
    sa.Column('deadline', sa.DateTime(), nullable=False),
    sa.Column('priority_id', sa.Integer(), nullable=True),
    sa.Column('status_id', sa.Integer(), nullable=True),
    sa.Column('project_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['priority_id'], ['priority.priority_id'], ),
    sa.ForeignKeyConstraint(['project_id'], ['project.project_id'], ),
    sa.ForeignKeyConstraint(['status_id'], ['status.status_id'], ),
    sa.PrimaryKeyConstraint('task_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('task')
    op.drop_table('project')
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_user_last_name'))
        batch_op.drop_index(batch_op.f('ix_user_first_name'))
        batch_op.drop_index(batch_op.f('ix_user_email'))

    op.drop_table('user')
    op.drop_table('status')
    op.drop_table('priority')
    # ### end Alembic commands ###
