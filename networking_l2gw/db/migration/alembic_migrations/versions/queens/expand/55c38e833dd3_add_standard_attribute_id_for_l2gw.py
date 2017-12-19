# Copyright 2017 <Peng Liu/RedHat>
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
#

"""add standard_attribute_id for l2gw

Revision ID: 55c38e833dd3
Revises: 49ce408ac349
Create Date: 2017-12-19 05:18:24.256173

"""

# revision identifiers, used by Alembic.
revision = '55c38e833dd3'
down_revision = '49ce408ac349'

from alembic import op
import sqlalchemy as sa

TABLES = ('l2gateways', 'l2gatewayconnections')


def upgrade():
    for table in TABLES:
        op.add_column(table, sa.Column('standard_attr_id', sa.BigInteger(),
                                        nullable = True))
