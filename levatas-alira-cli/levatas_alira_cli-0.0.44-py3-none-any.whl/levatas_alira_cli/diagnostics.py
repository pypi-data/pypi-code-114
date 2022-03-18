import os
import yaml
import uuid

from importlib import import_module


class Diagnostics:
    def __init__(self, configuration) -> None:
        self.modules = None
        self._load_configuration(configuration)

    def run(self):
        result = []
        if self.modules is None:
            return result

        for module in self.modules:
            module_result = module["function"](**module["arguments"])

            item = {
                "label": module["label"],
            }

            if isinstance(module_result, tuple):
                item["status"] = module_result[0]
                item["messages"] = module_result[1]
            else:
                item["status"] = module_result

            result.append(item)

        return result

    def _load_configuration(self, configuration) -> None:
        if configuration is None:
            configuration = os.path.join(
                self.configuration_directory, "diagnostics.yml"
            )

        if hasattr(configuration, "read"):
            configuration = self._load_configuration_from_stream(configuration)
        else:
            configuration = self._load_configuration_from_file(configuration)

        if configuration is not None:
            result = self._load_modules(configuration)
            self.modules = list(result.values()) if result else None

    def _load_modules(self, configuration):
        result = {}
        modules = configuration.get("diagnostics", [])
        if modules is None:
            return None

        for item in modules:
            try:
                module_path, _, fn_name = item["function"].rpartition(".")
                function = getattr(import_module(module_path), fn_name)

                reference = f"{fn_name}.{uuid.uuid4().hex}"
                result[reference] = {"function": function}

                if "label" in item:
                    result[reference]["label"] = item["label"]
                else:
                    result[reference]["label"] = fn_name

                fn_arguments = {}
                for argument_id, argument in item.items():
                    if argument_id in ("function", "label"):
                        continue

                    if argument.startswith("$"):
                        argument = os.environ.get(argument[1:], argument)

                    fn_arguments[argument_id] = argument

                result[reference]["arguments"] = fn_arguments
            except ModuleNotFoundError as e:
                raise RuntimeError(
                    f"Unable to load function {module_path}.{fn_name}"
                ) from e

        return result

    def _load_configuration_from_stream(self, configuration):
        try:
            return yaml.safe_load(configuration.read())
        except Exception as e:
            raise RuntimeError("Unable to load configuration") from e

    def _load_configuration_from_file(self, configuration):
        try:
            with open(configuration) as file:
                return yaml.load(file.read(), Loader=yaml.FullLoader)
        except Exception as e:
            raise RuntimeError(
                "Unable to load configuration from " f"file {configuration}"
            ) from e


def connectivity(endpoint, **kwargs):
    import http.client as httplib

    if endpoint.startswith("http://"):
        endpoint = endpoint[7:]
        connection = httplib.HTTPConnection(endpoint, timeout=5)
    elif endpoint.startswith("https://"):
        endpoint = endpoint[8:]
        connection = httplib.HTTPSConnection(endpoint, timeout=5)
    else:
        connection = httplib.HTTPSConnection(endpoint, timeout=5)

    try:
        connection.request("HEAD", "/")
        return True
    except Exception:
        return False
    finally:
        connection.close()
