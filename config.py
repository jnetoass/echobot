#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "a896b57b-d97c-414f-8b1d-0dd0780e3492")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "9yRpUW=vZ$RU(Si1fmJho_>=pE>")
