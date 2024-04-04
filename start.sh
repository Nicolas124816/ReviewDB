#! /bin/bash
echo "Start the frontend"
(cd ReviewDB && ng serve) &
echo "Start the backend"
python3 -m flask --app board run --port 8000 --debug && fg
echo "Get database export"
python3 TMDB_Reviews/DataExport.py
echo "Refreshing database"
python3 TMDB_Reviews/DailyRefresh.py

