import pandas as pd
import os


def merge_sales_for_product(input_folder, output_file, product_type):
    # List all CSV files in the data folder
    files = [f for f in os.listdir(input_folder) if f.endswith('.csv') and f.startswith('daily')]

    # Initialize an empty list to store DataFrames
    dfs = []

    # Loop through each file and process it
    for file in files:
        # Read CSV file
        df = pd.read_csv(os.path.join(input_folder, file))

        # Filter for 'pink morsel' products
        df_filtered = df[df['product'] == product_type].copy()

        # Calculate 'sales' and select required columns
        df_filtered['sales'] = df_filtered['price'].str.replace('$', '').astype(float) * df_filtered['quantity']
        df_filtered = df_filtered[['sales', 'date', 'region']]

        # Append the resulting dataframe to the list
        dfs.append(df_filtered)

    # Concatenate all DataFrames in the list into a single DataFrame
    result_df = pd.concat(dfs, ignore_index=True)

    # Save the result DataFrame to a CSV file
    result_df.to_csv(output_file, index=False)

    print(f"Data successfully combined and saved to {output_file}")


# Define the folder where your CSV files are located
data_folder = 'data'

# Define the output file path
output = os.path.join(data_folder, 'pink_morsel_sales.csv')

# Define product type
product = 'pink morsel'

merge_sales_for_product(data_folder, output, product)
