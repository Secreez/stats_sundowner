import streamlit as st
import pandas as pd
import random
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource
from bokeh.palettes import Spectral4
from bokeh.transform import factor_cmap

@st.cache_data() # Caches die Daten, damit sie nicht jedes Mal neu geladen werden müssen.
def load_data():
    data = pd.read_csv('sundowner.csv')
    return data

data = load_data()  # Lade die Daten

# Umschreiben der Antworten in numerische Werte
mapping = {"Sehr gut": 4, "Gut": 3, "Meh": 2, "BRUH": 1} # ! Test Werte !
for col in data.columns[1:]:
    data[col] = data[col].map(mapping).astype(str) # Umschreiben der Antworten in numerische Werte

# Für jede Frage, erstelle eine separate Grafik
for question in data.columns[1:]:
    # Zähle die Häufigkeit jeder Bewertung für diese spezifische Frage
    rating_counts = data[question].value_counts().sort_index() 

    source = ColumnDataSource(data=dict(x=rating_counts.index.astype(str), y=rating_counts.values))

    # Wähle zufällig zwischen verschiedenen Diagrammtypen
    chart_type = random.choice(['bar', 'circle', 'line', 'histogram'])


    if chart_type == 'circle':
        p = figure(x_range=list(map(str, range(1, 5))), height=350, toolbar_location=None,
                   title=f"Rating Counts for {question}")
        p.circle(x='x', y='y', size=20, source=source, 
                 color=factor_cmap('x', palette=Spectral4, factors=rating_counts.index)) 
        st.bokeh_chart(p, use_container_width=True)

    elif chart_type == 'line':
        p = figure(x_range=list(map(str, range(1, 5))), height=350, toolbar_location=None,
                   title=f"Rating Counts for {question}") 
        p.line(x='x', y='y', line_width=2, source=source, color='red')  # Einheitliche Farbe für Liniendiagramm
        st.bokeh_chart(p, use_container_width=True) 

    elif chart_type == 'histogram':
    
        bin_edges = range(1, len(rating_counts) + 2) # +2 weil wir die Anzahl der Kategorien haben wollen
        p = figure(height=350, toolbar_location=None, title=f"Histogram for {question}") 
        p.quad(top='y', bottom=0, left='x', right='x_end', source=source, 
               fill_color=factor_cmap('x', palette=Spectral4, factors=rating_counts.index))

        # Calculate x_end values based on x and bin width
        bin_width = 1 # Weil wir nur ganze Zahlen haben
        x_end_values = [int(x) + bin_width for x in rating_counts.index] 
        source.data['x_end'] = x_end_values 

        # Display the visualization in Streamlit
        st.bokeh_chart(p, use_container_width=True) 
