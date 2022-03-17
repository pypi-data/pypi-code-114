import enum
from dataclasses import dataclass
from typing import Mapping, MutableMapping, Optional, Tuple
from uuid import UUID

from myst.connectors.source_connectors import cleaned_observations, enhanced_forecast, historical_hourly_conditions
from myst.core.time.time_delta import TimeDelta
from myst.recipes.metar_station import MetarStation
from myst.recipes.time_series_recipe import TimeSeriesRecipe
from myst.resources.layer import Layer
from myst.resources.project import Project
from myst.resources.source import Source
from myst.resources.time_series import TimeSeries

_HISTORICAL_APIS_CUTOVER_BOUNDARY = TimeDelta("-PT23H")
_HISTORICAL_TO_FORECAST_CUTOVER_BOUNDARY = TimeDelta("PT1H")
_THE_WEATHER_COMPANY_DATA_SAMPLE_PERIOD = TimeDelta("PT1H")


@enum.unique
class Field(str, enum.Enum):
    """Data fields available from The Weather Company APIs involved in this recipe."""

    TEMPERATURE = "Temperature"
    RELATIVE_HUMIDITY = "Relative Humidity"
    WIND_DIRECTION = "Wind Direction"
    WIND_SPEED = "Wind Speed"


_CLEANED_OBSERVATIONS_FIELD_MAPPINGS: Mapping[Field, cleaned_observations.Field] = {
    Field.TEMPERATURE: cleaned_observations.Field.SURFACE_TEMPERATURE_CELSIUS,
    Field.RELATIVE_HUMIDITY: cleaned_observations.Field.RELATIVE_HUMIDITY_PERCENT,
    Field.WIND_DIRECTION: cleaned_observations.Field.WIND_DIRECTION_DEGREES,
    Field.WIND_SPEED: cleaned_observations.Field.WIND_SPEED_MPH,
}
_HISTORICAL_HOURLY_CONDITIONS_FIELD_MAPPINGS: Mapping[Field, historical_hourly_conditions.Field] = {
    Field.TEMPERATURE: historical_hourly_conditions.Field.TEMPERATURE,
    Field.RELATIVE_HUMIDITY: historical_hourly_conditions.Field.RELATIVE_HUMIDITY,
    Field.WIND_DIRECTION: historical_hourly_conditions.Field.WIND_DIRECTION,
    Field.WIND_SPEED: historical_hourly_conditions.Field.WIND_SPEED,
}
_ENHANCED_FORECAST_FIELD_MAPPINGS = {
    Field.TEMPERATURE: enhanced_forecast.Field.TEMPERATURE,
    Field.RELATIVE_HUMIDITY: enhanced_forecast.Field.RELATIVE_HUMIDITY,
    Field.WIND_DIRECTION: enhanced_forecast.Field.WIND_DIRECTION,
    Field.WIND_SPEED: enhanced_forecast.Field.WIND_SPEED,
}


@dataclass
class _SourceCache:
    cleaned_observations_source: Source
    historical_hourly_conditions_source: Source
    enhanced_forecast_source: Source


_SOURCE_CACHE: MutableMapping[Tuple[UUID, MetarStation], _SourceCache] = {}


class TheWeatherCompany(TimeSeriesRecipe):
    """A recipe for creating time series that stitch together multiple The Weather Company data sources.

    This recipe is defined for a given METAR station and field. Because the three The Weather Company APIs involved in
    this recipe interpolate differently between METAR stations, we do not allow specification of arbitrary lat/long,
    which could result in a time series of poor quality. Instead, we require a particular METAR station.
    """

    def __init__(self, metar_station: MetarStation, field: Field) -> None:
        self._metar_station = metar_station
        self._field = field

    def create(self, project: Project, title: Optional[str] = None, description: Optional[str] = None) -> TimeSeries:
        """Creates a new time series in the given project containing weather data for this recipe.

        This method will create the following resources in the given project:

        - A source specifying the `CleanedObservations` connector.
        - A source specifying the `HistoricalHourlyConditions` connector.
        - A source specifying the `EnhancedForecast` connector.
        - A time series with three layers:
          - One from the `CleanedObservations` source with no start offset and an end offset of -23 hours (exclusive)
          - One from the `HistoricalHourlyConditions` source with a start offset of -23 hours (inclusive) and an end
            offset of 1 hour (exclusive)
          - One from the `EnhancedForecast` source with a start offset of 1 hour (inclusive) and no end offset

        When invoking this method multiple times for the same project, with recipes created for the same METAR station,
        the same sources will be reused.

        Args:
            project: the project in which to create the time series and attendant sources
            title: the title of the time series; if none is given, will default to a combination of the field name and
                METAR station specified in the recipe
            description: the description of the time series

        Returns:
            the created time series
        """
        latitude = self._metar_station.latitude
        longitude = self._metar_station.longitude

        # Cache/look up sources by project + METAR station. This allows low-effort reuse of TWC sources within a single
        # client process.
        source_cache_key = (project.uuid, self._metar_station)

        # Create the three sources.
        if source_cache_key not in _SOURCE_CACHE:
            cleaned_observations_source = Source.create(
                project=project,
                title=f"CO ({self._metar_station.name})",
                connector=cleaned_observations.CleanedObservations(
                    latitude=latitude, longitude=longitude, fields=list(_CLEANED_OBSERVATIONS_FIELD_MAPPINGS.values())
                ),
            )
            historical_hourly_conditions_source = Source.create(
                project=project,
                title=f"HHC ({self._metar_station.name})",
                connector=historical_hourly_conditions.HistoricalHourlyConditions(
                    latitude=latitude,
                    longitude=longitude,
                    fields=list(_HISTORICAL_HOURLY_CONDITIONS_FIELD_MAPPINGS.values()),
                ),
            )
            enhanced_forecast_source = Source.create(
                project=project,
                title=f"EF ({self._metar_station.name})",
                connector=enhanced_forecast.EnhancedForecast(
                    latitude=latitude, longitude=longitude, fields=list(_ENHANCED_FORECAST_FIELD_MAPPINGS.values())
                ),
            )

            _SOURCE_CACHE[source_cache_key] = _SourceCache(
                cleaned_observations_source=cleaned_observations_source,
                historical_hourly_conditions_source=historical_hourly_conditions_source,
                enhanced_forecast_source=enhanced_forecast_source,
            )

        # Create the time series.
        default_title = f"{self._field.value} ({self._metar_station.name})"
        time_series = TimeSeries.create(
            project=project,
            title=title or default_title,
            sample_period=_THE_WEATHER_COMPANY_DATA_SAMPLE_PERIOD,
            cell_shape=(),
            coordinate_labels=(),
            axis_labels=(),
            description=description,
        )
        Layer.create(
            downstream_node=time_series,
            upstream_node=_SOURCE_CACHE[source_cache_key].cleaned_observations_source,
            order=0,
            output_index=0,
            label_indexer=_CLEANED_OBSERVATIONS_FIELD_MAPPINGS[self._field],
            end_timing=_HISTORICAL_APIS_CUTOVER_BOUNDARY,
        )
        Layer.create(
            downstream_node=time_series,
            upstream_node=_SOURCE_CACHE[source_cache_key].historical_hourly_conditions_source,
            order=1,
            output_index=0,
            label_indexer=_HISTORICAL_HOURLY_CONDITIONS_FIELD_MAPPINGS[self._field],
            start_timing=_HISTORICAL_APIS_CUTOVER_BOUNDARY,
            end_timing=_HISTORICAL_TO_FORECAST_CUTOVER_BOUNDARY,
        )
        Layer.create(
            downstream_node=time_series,
            upstream_node=_SOURCE_CACHE[source_cache_key].enhanced_forecast_source,
            order=2,
            output_index=0,
            label_indexer=_ENHANCED_FORECAST_FIELD_MAPPINGS[self._field],
            start_timing=_HISTORICAL_TO_FORECAST_CUTOVER_BOUNDARY,
        )

        return time_series
