-- import in hbtn_0c_0 database a new table
SELECT city, AVG(value) AS avg_temp 
FROM temperatures
GROUP BY city
ORDER BY  avg_temp DESC;
