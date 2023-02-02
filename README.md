# apparel-catalog-processing

This project takes in a sample dataset `myntra_products_catalog.csv`, which consists of clothing, shoes, and home goods. From the raw dataset, we parse the data, identify product categories and subcategories, clean title values, and provide group summaries.

The project is written in Python, uses a SQLite3 database and Pandas to parse and perform data operations.

## Data Operations 

### Categorization
There are no categories defined within the dataset, so we can attempt to categorize items based on keywords from the title or description. This project defines a list of categories and subcategories within `products.db` and uses keyword matching with product titles to identify the product's categorization.

## Open Questions

1. How can we optimize product categorization? Are there ways to improve category lookup speed? Can we improve precision of categories (e.g. mini dress or maxi dress vs. dress)? How can we limit null values? 
2. How could we attach this project to a data orchestration layer such as Dagster or Airflow that would expect product catalogs on a recurring basis? 
3. What would de-duplication look like for data coming in a recurring basis? What if duplicate titles were similar but not exact text matches?
