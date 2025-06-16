
                                                   ** Warehouse Management System (WMS) - MVP**
## 📌 Project Overview

This project is a **Minimum Viable Product (MVP)** for a Warehouse Management System (WMS), developed as part of the CSTE WMS assignment. It streamlines SKU to MSKU mapping, data cleaning, and visual dashboard generation for warehouse sales data, using a no-code frontend and AI-enhanced backend.

---

## 🧩 Features Implemented

### ✅ Part 1: SKU to MSKU Mapping Tool
- Built using Python and Tkinter GUI.
- Supports:
  - Mapping individual SKUs to Master SKUs (MSKUs).
  - pip install pandas openpyxl streamlit

  - Combo product support.
  - Error handling for missing mappings.
  - Logs for unmapped SKUs.

### ✅ Part 2: Database & Dashboard
- Used [Baserow](https://baserow.io) as an **Airtable alternative**.
- Created:
  - **Mapped Sales Table** with linked MSKUs.
  - **MSKU Summary Table** (grouped by MSKU, marketplace).
  - Sales metrics dashboard using filters/grouping in Baserow UI.

### ✅ Part 3: Integration
- Uploaded mapped sales data into Baserow.
- Created multiple views (grouped by MSKU, marketplace, etc.).
- Ensured clean user experience with sortable, filterable tables.

### ✅ Part 4: AI over Data Layer (Text-to-SQL)
- Used [Text2SQL.ai](https://text2sql.ai):
  - Uploaded mapped sales data CSV.
  - Executed queries like:
    - “Show total sales per MSKU”
    - “Top 3 products by revenue”
    - “Which MSKU has the most sales?”

---

## 🛠 Tech Stack

| Tool           | Purpose                                 |
|----------------|------------------------------------------|
| **Python**     | SKU → MSKU mapping script (GUI)          |
| **Tkinter**    | GUI for user-friendly input/output       |
| **Pandas**     | Data cleaning and preprocessing          |
| **Baserow**    | Visual relational DB & dashboards        |
| **Text2SQL.ai**| Natural language → SQL query generation  |

