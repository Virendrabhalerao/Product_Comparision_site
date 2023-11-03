import streamlit as st
from pythonyugeapitest import get_product_info  # Replace 'your_script_name' with the actual name of your script file

def main():
    st.title("Product Information App")

    api_key = "NkXQQnZZjAdFtrnINzCFJlMEr8AmUKyFLDh"
    product_name = st.text_input("Enter the product name:")

    if st.button("Get Product Info"):
        product_info = get_product_info(api_key, product_name)

        if product_info:
            st.subheader("Product Info:")
            st.write("Product Title:", product_info[0]['product_title'])
            st.write("Lowest Price:", product_info[0]['product_lowest_price'])
            st.write("Product Link:", product_info[0]['product_link'])
            st.image(product_info[0]['product_image'], caption="Product Image", use_column_width=True)
        else:
            st.warning("No product found with the given name.")

if __name__ == "__main__":
    main()
