from pathlib import Path

TRUE_FOUNDRY_SERVER = (
    "https://sf-server.tfy-ctl-us-east-1-develop.develop.truefoundry.io"
)
# TRUE_FOUNDRY_SERVER = "http://localhost:4040"
AUTH_SERVER = "https://auth-server.tfy-ctl-us-east-1-develop.develop.truefoundry.io"
SERVICE_DEF_FILE_NAME = "servicefoundry.yaml"

SESSION_FILE = f"{str(Path.home())}/.truefoundry"

# Polling during login redirect
MAX_POLLING_RETRY = 100
POLLING_SLEEP_TIME_IN_SEC = 4

# Refresh access token cutoff
REFRESH_ACCESS_TOKEN_IN_MIN = 10 * 60
