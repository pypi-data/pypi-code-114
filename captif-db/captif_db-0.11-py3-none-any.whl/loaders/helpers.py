from captif_db.db.models import Station


def max_station(db_session, project_id):
    return max(
        (
            vv[0]
            for vv in db_session.query(Station.station_no)
            .filter_by(project_id=project_id)
            .all()
        )
    )
