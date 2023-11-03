"""create user table

Revision ID: 2921cc2f5baf
Revises: 
Create Date: 2023-11-03 08:50:56.441684

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2921cc2f5baf'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('username', sa.String(50), nullable=False, unique=True),
        sa.Column('password', sa.String(100), nullable=False)
    )

def downgrade() -> None:
    op.drop_table('users')
