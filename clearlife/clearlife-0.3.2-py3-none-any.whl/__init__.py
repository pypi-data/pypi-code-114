from threading import Timer
import logging

from clearlife.cli import get_default_args, main


__version__ = '0.3.2'  # also change in setup.py

log = logging.getLogger(__name__)

TIMER_INTERVAL=30
"""int: number of seconds to wait before retrying a key operation.
"""

class ClearLifeClient(object):
    """API Client for interacting with the `clearlifed` API
    endpoints. Note that this object is just a wrapper around
    the commands in :mod:`clearlifed.cli`.

    Attributes:
        derive_timer (threading.Timer): to retry a key get operation (for example 
            when waiting for the user to approve a notification). Same with
            :attr:`app_timer`.
    """
    def __init__(self, name) -> None:
        super().__init__()
        self.name = name
        self.args = get_default_args(name)

        self._otp = None
        self._app_keys = None

        self.derive_timer = None
        self.app_timer = None


    @property
    def otp(self):
        """Registers this server application with `clearlifed` to
        obtain end-to-end encryption keys.
        """
        if self._otp is None:
            args = self.args.copy()
            args.update({
                "command": "register",
            })

            self._otp = main(args)

        return self._otp


    def _trigger_app_timer(self):
        """Cancels an existing app key timer if it exists, and then 
        creates a new one.
        """
        if self.app_timer is not None:
            self.app_timer.cancel()

        self.app_timer = Timer(TIMER_INTERVAL, self.get_app_keys, kwargs={"retry": True})
        self.app_timer.start()


    def get_app_keys(self, retry=False):
        """Gets the base application keys for this package.

        Args:
            retry (bool): if True, a timer will be set to keep retrying
                this derived key operation until it succeeds.
        """
        args = self.args.copy()
        args.update({
            "command": "appkeys",
            "seed": self.otp["seed"]
        })

        try:
            result = main(args)
        except:
            log.error("Trying to get base app keys", exc_info=True)
            result = None

        self._app_keys = result

        if (result is None or "did" not in result) and retry:
            self._trigger_app_timer()


    @property
    def app_keys(self):
        if self._app_keys is None:
            self.get_app_keys(retry=True)

        return self._app_keys


    def _trigger_derive_timer(self, context, keyid):
        """Cancels an existing derive key timer if it exists, and then 
        creates a new one.
        """
        if self.derive_timer is not None:
            log.debug("Cancelling existing timer that isn't complete.")
            self.derive_timer.cancel()

        self.derive_timer = Timer(TIMER_INTERVAL, self.derive, context, keyid, retry=True)
        log.info(f"Starting new derived key wait timer at {TIMER_INTERVAL} for {context}:{keyid}.")
        self.derive_timer.start()


    def derive(self, context, keyid, retry=False):
        """Derives the keypair and seed for the given context
        and keyid.

        Args:
            retry (bool): if True, a timer will be set to keep retrying
                this derived key operation until it succeeds.
        """
        args = self.args.copy()
        args.update({
            "command": "derive",
            "context": context,
            "keyid": keyid,
            "seed": self.otp["seed"]
        })

        try:
            result = main(args)
        except:
            result = None
            log.error(f"Trying to grab derived keys for {context} and {keyid}.", exc_info=True)

        if (result is None or "did" not in result) and retry:
            self._trigger_derive_timer(context, keyid)

        return result
