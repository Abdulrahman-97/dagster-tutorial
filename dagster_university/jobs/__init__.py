from dagster import AssetSelection, define_asset_job

trips_by_week = AssetSelection.assets("trips_by_week")

trips_update_job = define_asset_job(
    name="trip_update_job",
    selection=AssetSelection.all() - trips_by_week
)

trips_by_week_job = define_asset_job(
    name="trips_by_week_job",
    selection=trips_by_week
)