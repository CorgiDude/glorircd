# -*- coding: utf-8 -*-
# Copyright © 2015 by the GlorIRCd team.  All rights reserved.
# See COPYING file included with this source for more information.

"""The AsyncIO backend for GlorIRCd."""

from taillight.signal import Signal

from GlorIRCd.modules.core.module import can_unload_signal


class AsyncioBackend:

    """The AsyncIO backend module for GlorIRCd."""

    def __init__(self, server):
        self.server = server

        # Prevent the backend from being unloaded.
        can_unload_signal.add(lambda fqmn: False, listener='io/asyncio')


M_NAME = 'asyncio'
M_CATEGORY = 'io'
M_DESCRIPTION = 'Provides the AsyncIO I/O backend.'
M_VERSION = '1.0.0'
M_REQUIRES = []
M_CLASS = AsyncioBackend
