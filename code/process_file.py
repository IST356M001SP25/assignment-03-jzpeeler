import streamlit as st
import packaging
import json
import os
from io import StringIO

st.title("📦 Process File of Packages")


uploaded_file = st.file_uploader("Upload package file (TXT format only):", type=["txt"])

if uploaded_file:

    original_filename = uploaded_file.name
    json_filename = original_filename.replace(".txt", ".json")

    text_data = StringIO(uploaded_file.getvalue().decode("utf-8")).read()

    packages = []  

    
    for line in text_data.splitlines():
        line = line.strip()
        if line:  # Ensure it's not an empty line
            parsed_pkg = packaging.parse_packaging(line)
            total = packaging.calc_total_units(parsed_pkg)
            unit = packaging.get_unit(parsed_pkg)

            packages.append(parsed_pkg)  # Store parsed data
            
            # Display parsed package info in Streamlit
            st.info(f"📦 {line} ➡️ **Total Size:** {total} {unit}")

    output_path = os.path.join(output_dir, json_filename)
    with open(output_path, "w") as json_file:
        json.dump(packages, json_file, indent=4)

    
    st.success(f"✅ {len(packages)} packages saved to `{json_filename}`", icon="💾")