'''
Write a streamlit to input one string of package data. 
It should use the `packaging.py` module to parse the string 
and output the package info as it appears. 
Calculate the total package size and display that.

see one_package.png for a screenshot
'''
import streamlit as st
import packaging

st.title("Process One Package")

pkg = st.text_input("Enter package data: ")

if st.button("Process Package"):
    if pkg:
        parsed_pkg = packaging.parse_packaging(pkg)
        total = packaging.calc_total_units(parsed_pkg) # these three lines process the package data
        unit = packaging.get_unit(parsed_pkg)

        st.subheader("Parsed Package Info") #these two lines display the parsed package info
        st.json(parsed_pkg) 

        st.subheader("Package Contents")
        table_data = [{"Item": list(item.keys())[0], "Quantity": list(item.values())[0]} for item in parsed_pkg]
        st.table(table_data)

        st.metric(label="Total Package Size", value=f"{total} {unit}")

else:
    st.warning("You must input package info in order to process")