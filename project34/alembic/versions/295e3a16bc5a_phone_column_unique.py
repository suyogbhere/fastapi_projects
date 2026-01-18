"""Phone column unique

Revision ID: 295e3a16bc5a
Revises: 7e9049e1824f
Create Date: 2026-01-18 21:35:15.574960

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '295e3a16bc5a'
down_revision: Union[str, Sequence[str], None] = '7e9049e1824f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    with op.batch_alter_table("users") as batch_op:
        batch_op.create_unique_constraint("uq_users_phone", ["phone"])


def downgrade() -> None:
    """Downgrade schema."""
    with op.batch_alter_table("users") as batch_op:
        batch_op.drop_constraint("uq_users_phone","users","phone", type_="unique")
