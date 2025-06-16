
import pandas as pd
import streamlit as st

st.set_page_config(page_title="SKU to MSKU Mapper", layout="centered")

st.title("🧮 SKU → MSKU Mapping Tool")

# Upload mapping file
mapping_file = st.file_uploader("Upload SKU-MSKU Mapping File (Excel)", type=["xlsx"])
sales_file = st.file_uploader("Upload Sales Data File (CSV)", type=["csv"])

if mapping_file and sales_file:
    try:
        mapping_df = pd.read_excel(mapping_file)
        sales_df = pd.read_csv(sales_file)

        st.success("Files uploaded successfully!")

        if "SKU" not in mapping_df.columns or "MSKU" not in mapping_df.columns:
            st.error("Mapping file must contain 'SKU' and 'MSKU' columns")
        else:
            # Merge sales data with mapping
            merged_df = sales_df.merge(mapping_df, on="SKU", how="left")

            # Handle missing mappings
            missing = merged_df[merged_df["MSKU"].isnull()]
            if not missing.empty:
                st.warning(f"{len(missing)} SKUs have no MSKU mapping.")

            st.dataframe(merged_df)

            csv = merged_df.to_csv(index=False).encode('utf-8')
            st.download_button("⬇️ Download Mapped Sales CSV", csv, "mapped_sales.csv", "text/csv")

    except Exception as e:
        st.error(f"Error: {e}")
