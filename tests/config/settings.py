"""Settings module for test app."""

ENV: str = "development"
TESTING: bool = True
SQLALCHEMY_DATABASE_URI: str = "sqlite://"
SECRET_KEY: str = "not_so_secrete"  # nosec

BCRYPT_LOG_ROUNDS = (
    4
)  # For faster tests; needs at least 4 to avoid "ValueError: Invalid rounds"
DEBUG_TB_ENABLED: bool = False
CACHE_TYPE: str = "simple"  # Can be "memcached", "redis", etc.
SQLALCHEMY_TRACK_MODIFICATIONS: bool = False
# WEBPACK_MANIFEST_PATH: str = "webpack/manifest.json"
# WTF_CSRF_ENABLED: bool = False  # Allows form testing
