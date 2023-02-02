# apparel-catalog-processing

This project takes in a sample dataset myntra_products_catalog.csv, which consists of clothing, shoes, and home goods. From the raw dataset, we parse the data, identify product categories and subcategories, clean title values, and provide group summaries.

## Open Questions

1. How can we optimize product categorization? Are there ways to improve categorization speed and lookup? Can we improve precision 
2. How could we attach this to a data orchestration layer such as Dagster or Airflow that would expect product catalogs on a recurring basis? 
