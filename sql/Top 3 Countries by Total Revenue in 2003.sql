-- Top 3 Countries by Total Revenue in 2003

SELECT
 COUNTRY,
 EXTRACT(YEAR FROM ORDERDATE) AS year,
 ROUND(SUM(SALES), 2) AS total_revenue
from
 `retail-sales-pipeline-476503.retail_sales_cleaned.retail_sales_cleaned`
WHERE 
 EXTRACT(YEAR FROM ORDERDATE) = 2003
GROUP BY
 COUNTRY, year
ORDER BY
 total_revenue DESC
LIMIT 3;
