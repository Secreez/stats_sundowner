import streamlit as st
sources = {
    "Fun Fact Einstiegsfrage zum Warmlaufen / Hedy LAMARR": "https://www.austria.info/de/inspiration/meister-und-meisterwerke/hedy-lamarr-filmdiva-und-lady-bluetooth",
    "Oberflächlichkeit / Schönheit": "https://www.degruyter.com/document/doi/10.1515/9781400839445/html",
    "Diskriminierung über die Vornamen": "https://ubsearch.sbg.ac.at/primo-explore/fulldisplay?docid=USB_almanz71311202060003331&context=L&vid=USB&lang=de_DE&search_scope=USB_local_data&adaptor=Local%20Search%20Engine&isFrbr=true&tab=default_tab&query=any,contains,emily%20and%20greg&sortby=date&facet=frbrgroupid,include,668147536&offset=0",
    "Diskriminierung von Frauen (1)": "https://ubsearch.sbg.ac.at/primo-explore/fulldisplay?docid=TN_cdi_crossref_primary_10_1007_BF03372854&context=PC&vid=USB&lang=de_DE&search_scope=USB_local_data&adaptor=primo_central_multiple_fe&tab=default_tab&query=any,contains,diskriminierung%20frauen%20personalauswahl&offset=0",
    "Diskriminierung von Frauen (2)": "https://ubsearch.sbg.ac.at/primo-explore/fulldisplay?docid=TN_cdi_crossref_primary_10_1093_esr_jcx051&context=PC&vid=USB&lang=de_DE&search_scope=USB_local_data&adaptor=primo_central_multiple_fe&tab=default_tab&query=any,contains,personalauswahl%20diskriminierung&offset=0",
    "Lücken im Lebenslauf": "https://ubsearch.sbg.ac.at/primo-explore/fulldisplay?docid=TN_cdi_crossref_primary_10_1026_0932_4089_a000237&context=PC&vid=USB&lang=de_DE&search_scope=USB_local_data&adaptor=primo_central_multiple_fe&tab=default_tab&query=any,contains,l%C3%BCcken%20im%20lebenslauf&offset=0",
    "Bedeutung von Bewerbungsfotos / Entscheidungskriterien der Personalverantwortlichen": "https://econtent.hogrefe.com/doi/10.1026/0932-4089/a000193",
    "Behinderung und Arbeitsmarkt": "https://ubsearch.sbg.ac.at/primo-explore/fulldisplay?docid=TN_cdi_gale_infotracmisc_A506556134&context=PC&vid=USB&lang=de_DE&search_scope=USB_local_data&adaptor=primo_central_multiple_fe&tab=default_tab&query=any,contains,arbeitsmarkt%20alter%20diskriminierung&offset=0"
}

def display_sources():
    st.markdown("#### Quellen:")
    st.markdown("Alle Quellen sind PDFs. In der Präsentation werden nur kurze Informationen zu den Quellen gegeben. Eine vollständige Auflistung der Quellen findet ihr sonst auf unserer LinkedIn-Seite. Bei Interesse kontaktiert uns bitte.")

    for question, source in sources.items():
        st.markdown(f"- {question}: [{source}]({source})")

display_sources()