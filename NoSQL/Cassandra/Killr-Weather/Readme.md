## Manually Running the COPY Command

If the automated method does not work, you can manually run the `COPY` command using `cqlsh`:

### Step 1: Start `cqlsh` with the CSV file mounted

```bash
sudo docker run --rm -it --network cassandra -v $(pwd):/scripts cassandra:latest cqlsh cassandra 9042
```

Step 2: Execute the COPY command within cqlsh

```bash
COPY isd_weather_data.weather_station (id, name, country_code, state_code, call_sign, lat, long, elevation) FROM '/scripts/weather_stations.csv' WITH HEADER = TRUE;
```

This should import the data from weather_stations.csv into your Cassandra database.

This code block can be directly placed in your README file for clear and concise instructions.
