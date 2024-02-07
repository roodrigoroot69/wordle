"""Words model

Revision ID: 4a4b7070fa66
Revises:
Create Date: 2024-02-07 04:25:44.927142

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4a4b7070fa66'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'words',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('word', sa.String),
        sa.Column('is_active', sa.Boolean),
        sa.Column('created_at', sa.DateTime),
        sa.Column('updated_at', sa.DateTime),
    )

def downgrade() -> None:
    op.drop_table('words')
