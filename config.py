# Copyright 2017 Jonathan Anderson
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this
# list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
# this list of conditions and the following disclaimer in the documentation
# and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import dotenv
import os
import sys
import warnings


dotenv_path = dotenv.find_dotenv()
if dotenv_path == '':
    warnings.warn(
        'Unable to find a .env file, assuming environment-based configuration')
else:
    dotenv.load_dotenv(dotenv_path)

DATABASE_URL = os.environ.get("DATABASE_URL")
if DATABASE_URL is None:
    sys.stderr.write('No DATABASE_URL specified; need to do one of:\n')
    sys.stderr.write('  - echo "DATABASE_URL=postgres://db_name" > .env or\n')
    sys.stderr.write('  - echo "DATABASE_URL=sqlite://filename" > .env or\n')
    sys.stderr.write('  - export DATABASE_URL="..."\n')
    sys.exit(1)

MAPBOX_TOKEN = os.environ.get("MAPBOX_TOKEN")
if MAPBOX_TOKEN is None:
    warnings.warn("MAPBOX_TOKEN not set; maps will not be able to load tiles")

REGISTRATION_IS_OPEN = os.environ.get("REGISTRATION_IS_OPEN")

SITE_TITLE = os.environ.get('SITE_TITLE')
if SITE_TITLE is None:
    warnings.warn("SITE_TITLE not set, defaulting to 'DevSummit'")
    SITE_TITLE = 'DevSummit'
