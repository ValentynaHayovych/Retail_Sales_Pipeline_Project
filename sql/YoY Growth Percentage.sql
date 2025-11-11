SELECT
 COUNTRY,
 year,
 total_revenue,
 ROUND(
  ((total_revenue - LAG(total_revenue) OVER (PARTITION BY COUNTRY ORDER BY year)) / LAG(total_revenue) OVER (PARTITION BY COUNTRY ORDER BY year)) * 100, 2
 ) AS yoy_growth,
FROM(
  SELECT
   COUNTRY,
   EXTRACT(YEAR FROM ORDERDATE) AS year,
   ROUND(SUM(SALES), 2) AS total_revenue,
  FROM
   `retail-sales-pipeline-476503.retail_sales_cleaned.retail_sales_cleaned`
  GROUP BY
   COUNTRY, year
)

ORDER BY
 year, total_revenue DESC