SELECT date,county,sitename,aqi,pm25,status,lat,lon
FROM records
WHERE sitename='富貴角'
ORDER BY date DESC;