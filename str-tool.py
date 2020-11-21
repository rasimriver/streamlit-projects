import pandas as pd
import streamlit as st

# Read files
@st.cache
def import_files():
    id_input = pd.read_excel('./id_list.xlsx')
    id_green = pd.read_excel('./id_ok.xlsx')
    id_oos = pd.read_excel('./id_ex.xlsx')

    return id_input, id_green, id_oos;

id_input, id_green, id_oos = import_files()

export = id_input.copy()

done = id_green[id_green['ID'].isin(export.iloc[:,0])]

export['Green'] = export['ID'].isin(id_green.iloc[:,0])

export['OOS'] = export['ID'].isin(id_oos.iloc[:,0])


# done_dup = done[done.duplicated()]

st.write(export, id_input)

# Excel Export

# export = result[result['TO - Organisation'].str.contains('^ITD', na=False)].loc[:,['Application Short Name',  'Application ID', 'TO - Organisation']]
# export_xlsx(export)
