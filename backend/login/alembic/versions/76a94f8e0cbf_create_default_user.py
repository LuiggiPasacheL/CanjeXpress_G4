"""create default user

Revision ID: 76a94f8e0cbf
Revises: 2921cc2f5baf
Create Date: 2023-11-03 09:12:34.858120

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '76a94f8e0cbf'
down_revision: Union[str, None] = '2921cc2f5baf'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    conn = op.get_bind()
    conn.execute(
            statement=sa.text(text='INSERT INTO users (username, password) VALUES (:username, :password)'),
            parameters={'username': 'user', 'password': '$2a$12$BS9kZpZhsUR/hmzUAb4C1uXOwDO0hw1otPNguM3Zls1zN8jf5ElO.'}
        )


def downgrade() -> None:
    conn = op.get_bind()
    conn.execute(
            statement=sa.text(text='DELETE FROM users WHERE username = :username'),
            parameters={'username': 'user'}
        )
