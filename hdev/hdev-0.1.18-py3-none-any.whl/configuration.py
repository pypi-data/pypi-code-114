"""Configuration for hdev commands."""
import toml


class Configuration(dict):
    """A dict which lets you access it's keys via dot separated strings."""

    def get(self, key, default=None):
        """Get nested dict keys using "key" with dot as separator.

           config.get("key", {}).get("nested", DEFAULT)

        becomes:

            config.get("key.nested", DEFAULT)
        """
        value = self
        for sub_key in key.split("."):
            try:
                value = value[sub_key]
            except KeyError:
                return default

        return value

    @classmethod
    def load(cls, path):
        """Load project TOML configuration based on `path`."""
        try:
            return cls(toml.load(path))

        except FileNotFoundError:
            # No project file, use defaults
            return cls()

        except ValueError:
            print(f"Invalid syntax on toml file '{path}'")
            raise
