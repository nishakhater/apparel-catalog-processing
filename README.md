# apparel-catalog-processing :shopping:

This project takes in a sample dataset `myntra_products_catalog.csv`, which consists of clothing, shoes, and home goods. From the raw dataset, we parse the data, identify product categories and subcategories, clean title values, remove unnecessary columns, and then push the cleaned data to a SQLite3 database.

The project is written in Python, uses a SQLite3 database and Pandas to parse and perform data operations.

## Data Operations 

### Categorization
There are no categories defined within the dataset, so we can attempt to categorize items based on keywords from the title or description. This project defines a list of categories and subcategories within `products.db` and uses keyword matching with product titles to identify the product's categorization.

### Simplifying Product Titles
In the raw dataset, the brand is included in the product title. This may not be ideal for listing the products on a website, as often the brand and product title are separate components for a product listing. It would be repetitive to have the brand in the product title. Thus, we remove the brand from the product title by doing a search and replace on product title.

### Unnecessary Columns
For this project, we don't care about certain columns in the dataset, so we remove them using Pandas before pushing data to our table.

### Pushing Data to SQL Table
After the data has been cleaned, categorized, and processed, we can push it to our SQLite3 database for storage.

## Open Questions

1. How can we optimize product categorization? Are there ways to improve category lookup speed? Can we improve precision of categories (e.g. mini dress or maxi dress vs. dress)? How can we limit null values? 
2. How could we attach this project to a data orchestration layer such as Dagster or Airflow that would expect product catalogs on a recurring basis? 
3. What would de-duplication look like for data coming in a recurring basis? What if duplicate titles were similar but not exact text matches?
4. What other information could we pull from the product description column? 
