import pandas as pd
import streamlit as st
import os
import re

# Read files

id_green = pd.read_excel('./id_ok.xlsx')
id_oos = pd.read_excel('./id_ex.xlsx')

def file_selector(folder_path='.'):
    filenames = os.listdir(folder_path)
    regex = re.compile(r'(.xlsx|.xls)$')
    filenames = [i for i in filenames if regex.search(i)]
    selected_filename = st.selectbox('Select an Excel file', filenames)
    return os.path.join(folder_path, selected_filename)

filename = file_selector()
st.write('You selected `%s`' % filename)

id_input = pd.read_excel(filename)

export = id_input.copy()

def column_selector(df):
    columns = list(df.columns)
    selected_column = st.selectbox('Select a column', columns)
    return selected_column

column = column_selector(export)
st.write('You selected `%s`' % column)

done = id_green[id_green.iloc[:,0].isin(export.loc[:,column])]

export['Green'] = export.loc[:,column].isin(id_green.iloc[:,0])

export['OOS'] = export.loc[:,column].isin(id_oos.iloc[:,0])

# done_dup = done[done.duplicated()]

st.write(export)

# Excel Export

if st.button('Export'):
    filename = "export3.xlsx"
    export.to_excel(filename)
    st.write('File has been exported with the filename %s' % filename)

# export.to_excel('export.xlsx')
