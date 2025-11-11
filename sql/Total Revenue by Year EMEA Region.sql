-- Total Revenue by Year EMEA Region

SELECT
 COUNTRY,
 EXTRACT(YEAR FROM ORDERDATE) AS year,
 ROUND(SUM(SALES), 2) AS total_revenue
from
 `retail-sales-pipeline-476503.retail_sales_cleaned.retail_sales_cleaned`
WHERE
 TERRITORY = 'EMEA'
GROUP BY
 COUNTRY, year
ORDER BY
 year, total_revenue DESC
