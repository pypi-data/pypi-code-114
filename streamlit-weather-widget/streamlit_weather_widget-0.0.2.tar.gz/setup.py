import setuptools

setuptools.setup(
    name="streamlit_weather_widget",
    version="0.0.2",
    author="ateeb",
    author_email="",
    description="A component loading forecast data from OpenWeather and uses react-open-weather React component",
    long_description="A component loading forecast data from OpenWeather and uses react-open-weather React component",
    long_description_content_type="text/plain",
    url="",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.7",
    install_requires=[
        # By definition, a Custom Component depends on Streamlit.
        # If your component has other Python dependencies, list
        # them here.
        "streamlit >= 0.63",
    ],
)
