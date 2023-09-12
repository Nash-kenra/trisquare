select * from public.sp500 s 

select * from public.nasdaq n 

select * from public.dowjones d 

SELECT * FROM public.sectors_subsectors_mv;

/* Group by sectors */
SELECT
    sector,
    COUNT(*) AS company_count
FROM
    public.sp500
GROUP BY
    sector
ORDER BY
    company_count DESC; -- You can change DESC to ASC for ascending order


    
SELECT distinct sector FROM public.sectors_subsectors_mv;

select distinct exchange_short_name, exchange  from public.globalstocks g 

select * from public.globalstocks g 

select * from public.globalstocks g where symbol = 'MSFT' where exchange_short_name in( 'NYSE', 'NASDAQ' ) and company_type = 'stock'

select count(*) from public.historical_prices hp 

select * from public.daily_prices dp    

/* Group companies by their year */
SELECT
    CONCAT(
        FLOOR(CAST(founded AS INTEGER) / 50) * 50, 
        '-', 
        FLOOR(CAST(founded AS INTEGER) / 50) * 50 + 49
    ) AS year_range,
    COUNT(*) AS company_count
FROM
    public.sp500 s 
GROUP BY
    year_range
ORDER BY
    year_range;
   
/* Group companies by their year, sector */
SELECT
    CONCAT(
        FLOOR(CAST(founded AS INTEGER) / 50) * 50, 
        '-', 
        FLOOR(CAST(founded AS INTEGER) / 50) * 50 + 49
    ) AS year_range,
    COUNT(*) AS company_count
FROM
    public.sp500 s 
GROUP BY
    year_range, sector
ORDER BY
    year_range, sector;


  
