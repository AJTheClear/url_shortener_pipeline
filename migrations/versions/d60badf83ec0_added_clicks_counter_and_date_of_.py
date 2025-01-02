"""Added clicks counter and date of creation

Revision ID: d60badf83ec0
Revises: 
Create Date: 2025-01-02 20:23:37.811718

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd60badf83ec0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('url',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('original_url', sa.String(), nullable=False),
    sa.Column('short_url', sa.String(), nullable=False),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.Column('clicks', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('short_url')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('url')
    # ### end Alembic commands ###
