from setuptools import setup

setup(
    name="tljh-new-user",
    version = "0.1.3",
    entry_points={"tljh": ["new-user = tljh_new_user"]},
    py_modules=["tljh_new_user"],
)
