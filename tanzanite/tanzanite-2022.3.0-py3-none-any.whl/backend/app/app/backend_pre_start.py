# # pylint: disable=missing-module-docstring
# # pylint: disable=missing-function-docstring


# import logging

# from tenacity import (
#     after_log,
#     before_log,
#     retry,
#     stop_after_attempt,
#     wait_fixed,
# )

# from tanzanite.backend.app.app.db.session import SessionLocal


# logger = logging.getLogger(__name__)


# MAX_TRIES = 60 * 5  # 5 minutes
# WAIT_SECONDS = 1


# @retry(
#     stop=stop_after_attempt(MAX_TRIES),
#     wait=wait_fixed(WAIT_SECONDS),
#     before=before_log(logger, logging.INFO),
#     after=after_log(logger, logging.WARN),
# )
# def init() -> None:
#     logger.debug('[+] binding to %s', SessionLocal.kw.get('bind'))
#     try:
#         db = SessionLocal()
#         # Try to create session to check if DB is awake
#         db.execute("SELECT 1")
#     except Exception as e:
#         logger.error(e)
#         raise e


# def main() -> None:
#     logger.info("[+] initializing database")
#     init()
#     logger.info("[+] database finished initializing")


# if __name__ == "__main__":
#     main()
