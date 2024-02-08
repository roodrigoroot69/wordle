"""add date fields to winners

Revision ID: 05eae6c3e53c
Revises: 1f782b1dc135
Create Date: 2024-02-08 03:14:07.888522

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '05eae6c3e53c'
down_revision: Union[str, None] = '1f782b1dc135'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
        op.add_column('winners', sa.Column('created_at', sa.DateTime),)
        op.add_column('winners', sa.Column('updated_at', sa.DateTime),)

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('categories', 'created_at')
    op.drop_column('categories', 'updated_at')

    # ### end Alembic commands ###
