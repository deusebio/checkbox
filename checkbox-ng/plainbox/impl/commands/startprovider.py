# This file is part of Checkbox.
#
# Copyright 2012-2014 Canonical Ltd.
# Written by:
#   Zygmunt Krynicki <zygmunt.krynicki@canonical.com>
#
# Checkbox is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 3,
# as published by the Free Software Foundation.
#
# Checkbox is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Checkbox.  If not, see <http://www.gnu.org/licenses/>.
"""
:mod:`plainbox.impl.commands.startprovider` -- startprovider sub-command
========================================================================
"""
import warnings


warnings.warn(
    "Use either plainbox.impl.commands.cmd_startprovider"
    " or .inv_startprovider instead", PendingDeprecationWarning, stacklevel=2)

__all__ = ['StartProviderInvocation', 'StartProviderCommand']

from plainbox.impl.commands.inv_startprovider import StartProviderInvocation
from plainbox.impl.commands.cmd_startprovider import StartProviderCommand
