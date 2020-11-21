import pandas as pd
import streamlit as st

# Read files
@st.cache
def import_files():
    id_list = pd.read_excel('./id_list.xlsx')
    id_ok = pd.read_excel('./id_ok.xlsx')
    id_ex = pd.read_excel('./id_ex.xlsx')

    return id_list, id_ok, id_ex;

id_list, id_ok, id_ex = import_files()

st.write(id_ok)

# Excel Export

# export = result[result['TO - Organisation'].str.contains('^ITD', na=False)].loc[:,['Application Short Name',  'Application ID', 'TO - Organisation']]
# export_xlsx(export)
