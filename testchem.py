import streamlit as st
from rdkit import Chem
from rdkit.Chem import Draw
from rxnmapper import RXNMapper
import py3Dmol

# Page config
st.set_page_config(page_title="Chemical App", layout="wide")

# RXN Mapper instance
rxn_mapper = RXNMapper()

# 3D Viewer Function
def show_3d_model(smiles):
    mol = Chem.MolFromSmiles(smiles)
    if not mol:
        st.error("❌ Invalid SMILES for 3D visualization.")
        return
    block = Chem.MolToMolBlock(mol)
    view = py3Dmol.view(width=400, height=400)
    view.addModel(block, "mol")
    view.setStyle({"stick": {}})
    view.zoomTo()
    st.components.v1.html(view._make_html(), height=400)

# Predictor Logic
def predict_reaction_outcome(reaction_smiles):
    if not reaction_smiles.strip():
        return "❌ Empty reaction SMILES string."
    try:
        results = rxn_mapper.get_attention_guided_atom_maps([reaction_smiles])
        return results[0]['mapped_rxn']
    except Exception as e:
        return f"❌ Error: {str(e)}"

# Navigation
page = st.sidebar.selectbox("📘 Go to", ["Home", "Reaction Predictor", "Reaction Analyser", "About"])

# Home
if page == "Home":
    st.title("🧪 Welcome to the Chemical Reaction App")
    st.markdown("Navigate using the sidebar to explore prediction, analysis, and info.")

# Predictor
elif page == "Reaction Predictor":
    st.title("🧬 Chemical Reaction Predictor with 3D Viewer")
    st.subheader("Enter one or more reaction SMILES (one per line):")
    reaction_input = st.text_area("Example: CC(=O)OC.O>>CC(=O)O.CO", height=150)

    if st.button("Predict Reaction Outcomes"):
        reactions = [r.strip() for r in reaction_input.split("\n") if r.strip()]
        if not reactions:
            st.error("Please enter at least one valid SMILES reaction string.")
        else:
            st.subheader("🔎 Prediction Results:")
            for i, reaction in enumerate(reactions, 1):
                st.markdown(f"**Reaction {i}:** `{reaction}`")
                outcome = predict_reaction_outcome(reaction)
                st.write(outcome)
                if ">>" in outcome and "❌" not in outcome:
                    try:
                        product_part = outcome.split(">>")[1]
                        st.markdown("🔬 3D view of main product (first compound):")
                        first_product = product_part.split(".")[0]
                        show_3d_model(first_product)
                    except Exception as e:
                        st.warning(f"⚠ Could not display 3D view: {e}")
                st.markdown("---")

# Analyser
elif page == "Reaction Analyser":
    st.title("🔍 Reaction Analyser")
    st.subheader("Enter SMILES string for analysis:")

    smiles = st.text_input("Example: C1=CC=CC=C1Br")

    if smiles:
        mol = Chem.MolFromSmiles(smiles)
        if mol:
            st.image(Draw.MolToImage(mol, size=(300, 300)), caption="2D Structure")
            st.markdown("🔬 **3D Visualization:**")
            show_3d_model(smiles)
        else:
            st.error("❌ Invalid SMILES input.")

# About
elif page == "About":
    st.title("ℹ️ About This App")
    st.markdown("""
    This is a chemical reaction prediction and visualization tool built with:
    - 🧠 **RDKit** for chemical structure parsing
    - 🧬 **rxnmapper** for reaction mapping
    - 🔬 **3Dmol.js** via `py3Dmol` for interactive visualization
    - 🌐 **Streamlit** for web interface

    Developed by Team ChemiCo 💡 for academic and research use.
    """)

