# This is just Python which means you can inherit and tweak settings

import warnings
import os

_basedir = os.path.abspath(os.path.dirname(__file__))

THREADS_PER_PAGE = 8

# General

# These will need to be set to `True` if you are developing locally
CORS = True
debug = True

# this is the secret key used by flask session management
SECRET_KEY = 'uEhf1dkiurXrsPd0cv3M+dQ9neTM7oFg5iIKBKLtGStoQmaL0B10og=='

# You should consider storing these separately from your config
LEMUR_TOKEN_SECRET = 'soHncj7BFvPpubBXDSRMAzcBOGbPEZYDi8TwH78iguMWVU3GJYztnQ=='
LEMUR_ENCRYPTION_KEYS = 'BmCmU2kOLJ1-_2qsrEpWKvCsd7WycbeEaKHHl-OO2u0='

# List of domain regular expressions that non-admin users can issue
LEMUR_ALLOWED_DOMAINS = []

# Mail Server

LEMUR_EMAIL = ''
LEMUR_SECURITY_TEAM_EMAIL = []

# Certificate Defaults

LEMUR_DEFAULT_COUNTRY = 'US'
LEMUR_DEFAULT_STATE = 'CA'
LEMUR_DEFAULT_LOCATION = 'Los Angeles'
LEMUR_DEFAULT_ORGANIZATION = 'PrimeKey'
LEMUR_DEFAULT_ORGANIZATIONAL_UNIT = 'Operations'

# Authentication Providers
ACTIVE_PROVIDERS = []

# Metrics Providers
METRIC_PROVIDERS = []

# Logging

LOG_LEVEL = "DEBUG"
LOG_FILE = "lemur.log"

# Database

# modify this if you are not using a local database
SQLALCHEMY_DATABASE_URI = 'postgresql://lemur:lemur@postgres:5432/lemur'

# AWS

# LEMUR_INSTANCE_PROFILE = 'Lemur'

# Issuers

# These will be dependent on which 3rd party that Lemur is
# configured to use.

# VERISIGN_URL = ''
# VERISIGN_PEM_PATH = ''
# VERISIGN_FIRST_NAME = ''
# VERISIGN_LAST_NAME = ''
# VERSIGN_EMAIL = ''

#
# EJBCA Plugin Configuration
#

EJBCA_SOURCE_EXPIRE_DAYS = 7300
EJBCA_SOURCE_MAX_RESULTS = 100000

EJBCA_URL = os.getenv('EJBCA_URL')

if not EJBCA_URL:
    warnings.warn("Required variable EJBCA_URL is missing")

CERT_PATH = "/usr/local/share/certs/"

EJBCA_PEM_PATH = os.path.abspath(os.path.join(CERT_PATH, "lemur_ejbca/clientcert.pem"))
EJBCA_PEM_PATH_ISSUINGCAG1 = os.path.abspath(os.path.join(CERT_PATH, "lemur_ejbca/issuingca_admin.pem"))
EJBCA_TRUSTSTORE = os.path.abspath(os.path.join(CERT_PATH, "lemur_ejbca/truststore.pem"))


def get_file_contents(filepath):
    try:
        with open(filepath, "r") as f:
            return f.read()
    except IOError:
        return None


EJBCA_INTERMEDIATE_ISSUINGCAG1 = get_file_contents(
    os.path.abspath(os.path.join(CERT_PATH, "lemur_ejbca/intermediate.pem")))
if not EJBCA_INTERMEDIATE_ISSUINGCAG1:
    warnings.warn("Required certificate for EJBCA_INTERMEDIATE_ISSUINGCAG1 is missing")

EJBCA_ROOT = get_file_contents(os.path.abspath(os.path.join(CERT_PATH, "lemur_ejbca/root.pem")))
if not EJBCA_ROOT:
    warnings.warn("Required certificate for EJBCA_ROOT is missing")
