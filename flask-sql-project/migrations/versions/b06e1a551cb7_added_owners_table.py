"""added owners table

Revision ID: b06e1a551cb7
Revises: 12b8b287a01f
Create Date: 2024-07-24 10:14:32.961303

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b06e1a551cb7'
down_revision = '12b8b287a01f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('owners',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=True),
    sa.Column('pup_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['pup_id'], ['puppies.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('owners')
    # ### end Alembic commands ###
