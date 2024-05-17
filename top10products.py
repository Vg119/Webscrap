#top 10 products revenue for last 30 days
import pandas as pd

transactions_df = pd.read_csv('transaction.csv')
products_df = pd.read_csv('products_tf.csv')

merged_df = pd.merge(transactions_df, products_df, left_on='product_id', right_on='id')

merged_df = merged_df.drop_duplicates()

merged_df['order_date'] = pd.to_datetime(merged_df['order_date'])

max_order_date = merged_df['order_date'].max()

start_date = max_order_date - pd.Timedelta(days=30)

last_30_days_df = merged_df[(merged_df['order_date'] >= start_date) & (merged_df['order_date'] <= max_order_date)].copy()

last_30_days_df.rename(columns={' title': 'title'}, inplace=True)

# Calculate revenue as the product of quantity and price
last_30_days_df['revenue'] = last_30_days_df['quantity'] * last_30_days_df[' price(in Rupees)']

last_30_days_df.to_csv('30_days_transactions.csv', index=False)

revenue_by_product = last_30_days_df.groupby(['product_id', 'title',' price(in Rupees)']).agg({'quantity': 'sum', 'revenue': 'sum'}).reset_index()

top_10_products = revenue_by_product.sort_values(by='revenue', ascending=False).head(10)

top_10_products.to_csv('top_10_products.csv', index=False)
