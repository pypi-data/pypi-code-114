# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['myst',
 'myst.adapters',
 'myst.auth',
 'myst.connectors',
 'myst.connectors.model_connectors',
 'myst.connectors.operation_connectors',
 'myst.connectors.source_connectors',
 'myst.core',
 'myst.core.data',
 'myst.core.time',
 'myst.data',
 'myst.models',
 'myst.openapi',
 'myst.openapi.api',
 'myst.openapi.api.connectors',
 'myst.openapi.api.organizations',
 'myst.openapi.api.projects',
 'myst.openapi.api.projects.backtests',
 'myst.openapi.api.projects.backtests.jobs',
 'myst.openapi.api.projects.backtests.results',
 'myst.openapi.api.projects.deployments',
 'myst.openapi.api.projects.edges',
 'myst.openapi.api.projects.models',
 'myst.openapi.api.projects.models.fit_policies',
 'myst.openapi.api.projects.models.fit_results',
 'myst.openapi.api.projects.models.inputs',
 'myst.openapi.api.projects.models.run_results',
 'myst.openapi.api.projects.nodes',
 'myst.openapi.api.projects.nodes.jobs',
 'myst.openapi.api.projects.nodes.policies',
 'myst.openapi.api.projects.nodes.results',
 'myst.openapi.api.projects.operations',
 'myst.openapi.api.projects.operations.inputs',
 'myst.openapi.api.projects.sources',
 'myst.openapi.api.projects.time_series',
 'myst.openapi.api.projects.time_series.layers',
 'myst.openapi.api.projects.time_series.run_policies',
 'myst.openapi.api.projects.time_series.run_results',
 'myst.openapi.api.users',
 'myst.openapi.models',
 'myst.recipes',
 'myst.recipes.time_series_recipes',
 'myst.resources']

package_data = \
{'': ['*']}

install_requires = \
['google-auth-oauthlib>=0.4.1,<1.0.0',
 'google-auth>=1.11.0,<2.0.0',
 'httpx>=0.15.4,<0.19.0',
 'importlib-metadata',
 'numpy>=1.18.0,<2.0.0',
 'pandas>=0.25.0,<2',
 'pydantic>=1.8.2,<2.0.0',
 'toml>=0.10.2,<0.11.0',
 'typing-extensions>=3.7.2,<4.0.0',
 'urllib3>=1.24.3,<2.0.0']

entry_points = \
{'console_scripts': ['generate-openapi-client = '
                     'tools.generate_openapi_client:app']}

setup_kwargs = {
    'name': 'myst-alpha',
    'version': '0.7.0',
    'description': 'This is the official Python library for the Myst Platform.',
    'long_description': '# Myst Python Library\n\nThis is the official Python client library for the Myst Platform.\n\n## Requirements\n\n- Python 3.7+\n\n## Installation\n\nTo install the package from PyPI:\n\n    $ pip install --upgrade myst-alpha\n\n## Authentication\n\nThe Myst API uses JSON Web Tokens (JWTs) to authenticate requests.\n\nThe Myst Python library handles the sending of JWTs to the API automatically and currently supports two ways to\nauthenticate to obtain a JWT: through your Google user account or a Myst service account.\n\n### Authenticating using your user account\n\nIf you don\'t yet have a Google account, you can create one on the\n[Google Account Signup](https://accounts.google.com/signup) page.\n\nOnce you have access to a Google account, send an email to `support@myst.ai` with your email so we can authorize you to\nuse the Myst Platform.\n\nUse the following code snippet to authenticate using your user account:\n\n```python\nimport myst\n\nmyst.authenticate()\n```\n\nThe first time you run this, you\'ll be presented with a web browser and asked to authorize the Myst Python library to\nmake requests on behalf of your Google user account. If you\'d like to re-authorize (for example with a different\naccount), pass `use_cache=False` to be presented with the web browser authorization once again.\n\n### Authenticating using a service account\n\nYou can also authenticate using a Myst service account. To request a service account, email `support@myst.ai`.\n\nTo authenticate using a service account, set the `MYST_APPLICATION_CREDENTIALS` environment variable to the path to your\nservice account key file:\n\n```sh\n$ export MYST_APPLICATION_CREDENTIALS=</path/to/key/file.json>\n```\n\nThen, go through the service account authentication flow:\n\n```python\nimport myst\n\nmyst.authenticate_with_service_account()\n```\n\nAlternatively, you can explicitly pass the path to your service account key:\n\n```python\nfrom pathlib import Path\n\nimport myst\n\nmyst.authenticate_with_service_account(key_file_path=Path("/path/to/key/file.json"))\n```\n\n## Connecting to a different environment\n\nContributors may want to connect to a non-production environment that they are authorized to develop in. In that case,\nyou can set the client with the API host you\'d like to connect to.\n\n```python\nimport myst\n\nmyst.set_client(myst.Client(api_host="https://petstore.api"))\n\nmyst.authenticate()\n```\n\n## Working with projects and graphs\n\nA project is a workspace for setting up a graph of sources, models, operations, and time series to achieve a particular\nobjective. The sources, model, operations, and time series therein are _nodes_ of the graph, and they are connected by\ndifferent types of _edges_.\n\nFor more of a conceptual overview, see [the platform documentation](https://docs.myst.ai/docs). The following assumes\nsome familiarity with those concepts and focuses instead on demonstrating how to use the Myst client library to\ninteract with the platform.\n\n### Projects\n\n#### Create a project\n\n```python\nimport myst\n\nproject = myst.Project.create(title="SF Electricity Load")\n```\n\n#### List projects\n\n```python\nimport myst\n\nprojects = myst.Project.list()\n```\n\n#### Retrieve a project\n\n```python\nimport myst\n\nproject = myst.Project.get(uuid="f89d7fbe-a051-4d0c-aa60-d6838b7e64a0")\n```\n\n### Nodes (Sources, Models, Operations, Time Series)\n\nA node (source, model, operation, or time series) is always associated with a project, and there are multiple patterns\nin the client library API by which you can list or create them.\n\n#### Create a node\n\nFor example, suppose you want to create a temperature time series to be used as a feature in your model. Assuming that\nyou have the variable `project: Project` in scope, you can write the following to create a new time series:\n\n```python\nksfo_temperature_time_series = project.create_time_series(\n    title="Temperature (KSFO)",\n    sample_period=myst.TimeDelta("PT1H"),  # Sample period of one hour. "PT1H" is an ISO 8601 duration string.\n)\n```\n\nOr, to exactly the same effect:\n\n```python\nimport myst\n\nksfo_temperature_time_series = myst.TimeSeries.create(\n    project=project,  # Notice that project must be specified in this formulation.\n    title="Temperature (KSFO)",\n    sample_period=myst.TimeDelta("PT1H"),\n)\n```\n\nThis is true for the other types of nodes, too. In all, the client library offers the following equivalent ways to\ncreate the different types of nodes:\n\n- `project.create_source(...)` <=> `Source.create(project=project, ...)`\n- `project.create_operation(...)` <=> `Operation.create(project=project, ...)`\n- `project.create_model(...)` <=> `Model.create(project=project, ...)`\n- `project.create_time_series(...)` <=> `TimeSeries.create(project=project, ...)`\n\n#### Create a node with connector\n\nFor nodes that are powered by connectors, you must specify the parameters of that connector during construction. For\nexample, suppose you wanted to create a source node based on The Weather Company\'s Cleaned Observations API, to be used\nas the source of temperature data in the time series we created above. To do so, you would write:\n\n```python\nfrom myst.connectors.source_connectors import cleaned_observations\n\nksfo_cleaned_observations = project.create_source(\n    title="Cleaned Weather (KSFO)",\n    connector=cleaned_observations.CleanedObservations(\n        latitude=37.619,\n        longitude=-122.374,\n        fields=[\n            cleaned_observations.Field.SURFACE_TEMPERATURE_CELSIUS,\n        ],\n    ),\n)\n```\n\n`Model` and `Operation` nodes are constructed similarly. As another example, if we wanted to take the 3-hour rolling\nmean of the temperature, we could create an operation as follows:\n\n```python\nimport myst\n\nfrom myst.connectors.operation_connectors import time_transformations\n\nrolling_mean_ksfo_temperature = project.create_operation(\n    title="Temperature (KSFO) - 3H Rolling Mean",\n    connector=time_transformations.TimeTransformations(\n        rolling_window_parameters=time_transformations.RollingWindowParameters(\n            window_period=myst.TimeDelta("PT3H"),\n            min_periods=1,\n            centered=False,\n            aggregation_function=time_transformations.AggregationFunction.MEAN,\n        )\n    ),\n)\n```\n\nWe will see how to connect an input to this operation [in a following step](#create-an-input).\n\n#### List nodes in a project\n\n```python\nnodes = project.list_nodes()\n```\n\n#### Retrieve a node\n\n```python\nimport myst\n\nmodel = myst.Model.get(\n    project_uuid="05703aea-7319-4623-810d-b92b58692906",\n    uuid="a5ba722c-6750-4796-8b43-230b5e0f4c4a",\n)\n```\n\nSimilar for `myst.Source.get`, `myst.Operation.get`, and `myst.TimeSeries.get`.\n\n### Edges (Inputs, Layers)\n\n#### Create a layer\n\nA layer is an edge that feeds into a time series. You can create a layer into a time series with either:\n\n```python\nimport myst\nfrom myst.connectors.source_connectors import cleaned_observations\n\nlayer = ksfo_temperature_time_series.create_layer(\n    upstream_node=ksfo_cleaned_observations,\n    order=0,\n    end_timing=myst.TimeDelta("-PT23H"),\n    label_indexer=cleaned_observations.Field.SURFACE_TEMPERATURE_CELSIUS.value,\n)\n```\n\nor:\n\n```python\nimport myst\nfrom myst.connectors.source_connectors import cleaned_observations\n\nlayer = myst.Layer.create(\n    downstream_node=ksfo_temperature_time_series,\n    upstream_node=ksfo_cleaned_observations,\n    order=0,\n    end_timing=myst.TimeDelta("-PT23H"),\n    label_indexer=cleaned_observations.Field.SURFACE_TEMPERATURE_CELSIUS.value,\n)\n```\n\n#### Create an input\n\nAn input is an edge that feeds into a model or an operation. To connect the temperature time series into the operation\nwe constructed before, we would write:\n\n```python\nfrom myst.connectors.operation_connectors import time_transformations\n\noperation_input = rolling_mean_ksfo_temperature.create_input(\n    upstream_node=ksfo_temperature_time_series,\n    group_name=time_transformations.GroupName.OPERANDS,\n)\n```\n\nAs always, this creation method is also available as:\n\n```python\nimport myst\n\nfrom myst.connectors.operation_connectors import time_transformations\n\n\noperation_input = myst.Input.create(\n    downstream_node=rolling_mean_ksfo_temperature,\n    upstream_node=ksfo_temperature_time_series,\n    group_name=time_transformations.GroupName.OPERANDS,\n)\n```\n\n#### List time series layers\n\n```python\nlayers = ksfo_temperature_time_series.list_layers()\n```\n\n#### List model/operation inputs\n\n```python\ninputs = rolling_mean_ksfo_temperature.list_inputs()\n```\n\n## Working with time series\n\nTime series are at the core of Myst\'s API. In addition to the functionality offered by a generic node, time series also\nsupport querying and inserting data.\n\nFirst, retrieve a time series:\n\n```python\nimport myst\n\ntime_series = myst.TimeSeries.get(\n    project_uuid="40bcb171-1c51-4497-9524-914630818aeb",\n    uuid="ca2a63d1-3515-47b4-afc7-13c6656dd744",\n)\n```\n\nTo insert a `TimeArray` of random scalar data into the time series:\n\n```python\nimport myst\nimport numpy as np\n\ntime_array = myst.TimeArray(\n    sample_period="PT1H",\n    start_time="2021-07-01T00:00:00Z",\n    end_time="2021-07-08T00:00:00Z",\n    as_of_time="2021-07-01T00:00:00Z",\n    values=np.random.randn(168),\n)\ntime_series.insert_time_array(time_array=time_array)\n```\n\nYou can also query a time series for a given as of time and natural time range. In this example, the query will return\nthe data we just inserted:\n\n```python\nimport myst\n\nreturned_time_array = time_series.query_time_array(\n    start_time=myst.Time("2021-07-01T00:00:00Z"),\n    end_time=myst.Time("2021-07-08T00:00:00Z"),\n    as_of_time=myst.Time("2021-07-01T00:00:00Z"),\n)\nassert returned_time_array == time_array\n```\n\n## Working with policies\n\nA policy is the way to specify the schedule on which a particular target will be fit or run, as well as the parameters\naround the target time range.\n\nAt the time of this writing, the Myst Platform supports two types of policies: _time series run policies_ and _model fit\npolicies_.\n\n### Time series run policies\n\n#### Create a time series run policy\n\n```python\nimport myst\n\nksfo_temp_run_policy = ksfo_temperature_time_series.create_run_policy(\n    schedule_timing=myst.TimeDelta("PT1H"),  # Run every hour.\n    start_timing=myst.TimeDelta("PT1H"),  # Run on data starting from an hour from now (inclusive)...\n    end_timing=myst.TimeDelta("P7D"),  # ...up to 7 days from now (exclusive).\n)\n```\n\n### Model fit policies\n\nSuppose we have a variable `xgboost_model` that contains a value of type `Model`.\n\n#### Create a model fit policy\n\n```python\nimport myst\n\nxgboost_model_fit_policy = xgboost_model.create_fit_policy(\n    schedule_timing=myst.TimeDelta("PT24H"),  # Run every 24 hours.\n    start_timing=myst.Time("2021-01-01T00:00:00Z"),  # Fit on data from the beginning of 2021 (UTC)...\n    end_timing=myst.TimeDelta("-PT1H"),  # ...up to an hour ago (exclusive).\n)\n```\n\n## Deploying\n\nIn order for the graph to be executed, it must first be _deployed_. The Python client library does not currently support\nthis functionality; we recommend using the Myst Platform UI to deploy a project.\n\n## Backtesting\n\nIn order to run a backtest, make sure that you have created and deployed a project and graph with a model you want to backtest.\n\n### Creating and running backtest\n\n```python\nimport myst\n\n# Use an existing project.\nproject = myst.Project.get(uuid="<uuid>")\n\n# Use an existing deployed model within the project.\nmodel = myst.Model.get(project_uuid=project.uuid, uuid="<uuid>")\n\n# Create a backtest.\nbacktest = myst.Backtest.create(\n    project=project,\n    title="My Backtest",\n    model=model,\n    test_start_time=myst.Time("2021-07-01T00:00:00Z"),\n    test_end_time=myst.Time("2022-01-01T00:00:00Z"),\n    fit_start_timing=myst.TimeDelta("-P1M"),\n    fit_end_timing=myst.TimeDelta("-PT24H"),\n    fit_reference_timing=myst.CronTiming(cron_expression="0 0 * * 1"),\n    predict_start_timing=myst.TimeDelta("PT1H"),\n    predict_end_timing=myst.TimeDelta("PT24H"),\n    predict_reference_timing=myst.CronTiming(cron_expression="0 0 * * *"),\n)\n\n# Run the backtest.\nbacktest.run()\n```\n\n### Analyze backtest results\n\nTo extract the result of a backtest in the client library, you can use the following code:\n\n```python\nimport myst\n\n# Use an existing project.\nproject = myst.Project.get(uuid="<uuid>")\n\n# Use an existing backtest within the project.\nbacktest = myst.Backtest.get(project_uuid=project.uuid, uuid="<uuid>")\n\n# Wait until the backtest is complete.\nbacktest.wait_until_completed()\n\n# Get the result of the completed backtest.\nbacktest_result = backtest.get_result()\n```\n\nOnce you have extracted your backtest result, you can use the following code to generate metrics:\n\n```python\n# Get `mape`, `mae`, and `rmse` from the result object.\nmetrics_dictionary = backtest_result.metrics\n\n# To calculate custom metrics, map the backtest result to a pandas data frame.\nresult_data_frame = backtest_result.to_pandas_data_frame()\n\n# Compute some metrics for the backtest result.\nabsolute_error_series = (result_data_frame["targets"] - result_data_frame["predictions"]).abs()\nabsolute_percentage_error_series = absolute_error_series / result_data_frame["targets"].abs()\n\n# Create an index with the prediction horizons.\nhorizon_index = (\n    result_data_frame.index.get_level_values("time") -\n    result_data_frame.index.get_level_values("reference_time")\n)\n\n# Print the MAE and MAPE for each prediction horizon.\nprint(absolute_error_series.groupby(horizon_index).mean())\nprint(absolute_percentage_error_series.groupby(horizon_index).mean())\n```\n\n## Further Examples\n\nFor more full-featured usage examples of the Myst Platform Python client library, see the\n`/examples` folder.\n\n## Support\n\nFor questions or just to say hi, reach out to `support@myst.ai`.\n',
    'author': 'Myst AI, Inc.',
    'author_email': 'support@myst.ai',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7.0,<4.0.0',
}


setup(**setup_kwargs)
