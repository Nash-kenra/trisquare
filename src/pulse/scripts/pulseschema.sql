-- Table creation commands. New setup can run this.
-- Drop tables
DROP MATERIALIZED view if EXISTS public.sectors_subsectors_mv;
DROP TABLE if EXISTS public.dowjones;
DROP TABLE if EXISTS public.nasdaq;
DROP TABLE if EXISTS public.daily_prices;
DROP TABLE if EXISTS public.historical_prices;
DROP TABLE if EXISTS public.sp500;
DROP TABLE if EXISTS public.globalstocks;
DROP TABLE if EXISTS public.comp_estimates;
DROP TABLE if EXISTS public.globaletfs;
DROP TABLE if EXISTS public.stockprices; -- this table is removed, this needs to be removed eventually, kept it for backward compatability
DROP TABLE if EXISTS public.historic_prices; -- this table is removed, this needs to be removed eventually, kept it for backward compatability
DROP TABLE if EXISTS public.COMP_RECOM;

CREATE TABLE public.dowjones (
	symbol varchar NOT NULL,
	company_name varchar NULL,
	sector varchar NULL,
	subsector varchar NULL,
	headquarter varchar NULL,
	datefirstadded timestamp NULL,
	cik varchar NULL,
	founded timestamp NULL,
	CONSTRAINT dowjones_pkey PRIMARY KEY (symbol)
);

-- public.nasdaq definition

CREATE TABLE public.nasdaq (
	symbol varchar NOT NULL,
	company_name varchar NULL,
	sector varchar NULL,
	subsector varchar NULL,
	headquarter varchar NULL,
	cik varchar NULL,
	founded timestamp NULL,
	CONSTRAINT nasdaq_pkey PRIMARY KEY (symbol)
);

-- public.sp500 definition

CREATE TABLE public.sp500 (
	symbol varchar NOT NULL,
	company_name varchar NULL,
	sector varchar NULL,
	subsector varchar NULL,
	headquarter varchar NULL,
	datefirstadded varchar NULL,
	cik varchar NULL,
	founded varchar NULL,
	CONSTRAINT sp500_pkey PRIMARY KEY (symbol)
);

-- public.daily_prices definition

CREATE TABLE public.daily_prices (
	symbol varchar NOT NULL,
	date_time timestamp NOT NULL,
	company_name varchar NULL,
	price float8 NULL,
	changes_percentage float8 NULL,
	day_change float8 NULL,
	day_low float8 NULL,
	day_high float8 NULL,
	year_high float8 NULL,
	year_low float8 NULL,
	market_cap int8 NULL,
	price_avg_50 float8 NULL,
	price_avg_200 float8 NULL,
	exchange varchar NULL,
	volume int4 NULL,
	avg_volume int4 NULL,
	open_price float8 NULL,
	previous_close float8 NULL,
	eps float8 NULL,
	pe float8 NULL,
	earnings_announcement timestamp NULL,
	shares_outstanding int8 NULL,
	CONSTRAINT daily_prices_pkey PRIMARY KEY (symbol, date_time)
);

-- public.globalstocks definition

CREATE TABLE public.globalstocks (
	symbol varchar NOT NULL,
	company_name varchar NULL,
	price float8 NULL,
	exchange varchar NULL,
	exchange_short_name varchar NULL,
	company_type varchar NULL,
	CONSTRAINT globalstocks_pkey PRIMARY KEY (symbol)
);

-- public.comp_estimates definition
CREATE TABLE  public.comp_estimates (
	symbol varchar NOT NULL,
	date_time timestamp NOT NULL,
	estimatedrevenuelow float8 NULL,
	estimatedrevenuehigh float8 NULL,
	estimatedrevenueavg float8 NULL,
	estimatedebitdalow float8 NULL,
	estimatedebitdahigh float8 NULL,
	estimatedebitdaavg float8 NULL,
    estimatedebitlow float8 NULL,
    estimatedebithigh float8 NULL,
    estimatedebitavg float8 NULL,
    estimatednetincomelow float8 NULL,
    estimatednetincomehigh float8 NULL,
    estimatednetincomeavg float8 NULL,
    estimatedsgaexpenselow float8 NULL,
    estimatedsgaexpensehigh float8 NULL,
    estimatedsgaexpenseavg float8 NULL,
    estimatedepsavg float8 NULL,
    estimatedepshigh float8 NULL,
    estimatedepslow float8 NULL,
    numberanalystestimatedrevenue int4 NULL,
    numberanalystsestimatedeps int4 NULL,
	CONSTRAINT comp_estimates_pkey PRIMARY KEY (symbol)
);


 
-- public.historical_prices definition

CREATE TABLE public.historical_prices (
	symbol varchar NOT NULL,
	date_time timestamp NOT NULL,
	open_price float8 NULL,
	day_high float8 NULL,
	day_low float8 NULL,
	close_price float8 NULL,
	adj_close float8 NULL,
	volume int4 NULL,
	unadjusted_volume int4 NULL,
	day_change float8 NULL,
	change_percent float8 NULL,
	vwap float8 NULL,
	label_name varchar NULL,
	change_over_time float8 NULL,
	market_cap float8 NULL,
	CONSTRAINT historical_prices_pkey PRIMARY KEY (symbol, date_time)
);

CREATE TABLE public.comp_ratings (
	symbol varchar NOT NULL,
	date_time timestamp NOT NULL,
	rating varchar NULL,
	rating_score int4 NULL,
	rating_recommendation varchar NULL,
	rating_details_dcf_score int4 NULL,
	rating_details_dcf_recommendation varchar NULL,
	rating_details_roe_score int4 NULL,
	rating_details_roe_recommendation varchar NULL,
	rating_details_roa_score int4 NULL,
	rating_details_roa_recommendation varchar NULL,
	rating_details_de_score int4 NULL,
	rating_details_de_recommendation varchar NULL,
	rating_details_pe_score int4 NULL,
	rating_details_pe_recommendation varchar NULL,
	rating_details_pb_score int4 NULL,
	rating_details_pb_recommendation varchar NULL,
	CONSTRAINT comp_ratings_pkey PRIMARY KEY (symbol, date_time)

CREATE TABLE public.COMP_RECOM (
	symbol varchar NOT NULL,
	date_time timestamp NOT NULL,
	analyst_ratings_buy int4 NULL,
	analyst_ratings_hold int4 NULL,
	analyst_ratings_sell int4 NULL,
	analyst_ratings_strong_sell int4 NULL,
	analyst_ratings_strong_buy int4 NULL,
	CONSTRAINT COMP_RECOM_pkey PRIMARY KEY (symbol,date_time)
);

-- public.sectors_subsectors_mv source

CREATE MATERIALIZED VIEW public.sectors_subsectors_mv
TABLESPACE pg_default
AS SELECT distinct sector, subsector FROM public.sp500 order by sector;