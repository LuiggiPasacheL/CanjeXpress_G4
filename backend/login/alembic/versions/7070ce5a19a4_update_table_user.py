"""update table user

Revision ID: 7070ce5a19a4
Revises: 76a94f8e0cbf
Create Date: 2023-11-11 14:29:24.706648

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7070ce5a19a4'
down_revision: Union[str, None] = '76a94f8e0cbf'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    with op.batch_alter_table('users') as batch_op:
        batch_op.add_column(sa.Column('points', sa.Integer(), nullable=False, server_default='0'))
        batch_op.add_column(sa.Column('profile_picture', sa.String(length=255), nullable=False, server_default=''))
        batch_op.add_column(sa.Column('is_admin', sa.Boolean(), nullable=False, server_default='0'))

    op.execute("UPDATE users SET points = 10000 WHERE username = 'user'")

def downgrade() -> None:
    with op.batch_alter_table('users') as batch_op:
        batch_op.drop_column('points')
        batch_op.drop_column('profile_picture')
        batch_op.drop_column('is_admin')
