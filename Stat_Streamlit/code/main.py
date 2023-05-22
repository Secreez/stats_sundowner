import streamlit as st
import pandas as pd
import random
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, NumeralTickFormatter
from bokeh.palettes import Spectral4
from bokeh.transform import factor_cmap
from math import pi

@st.cache_data() # Caches die Daten, damit sie nicht jedes Mal neu geladen werden müssen.
def load_data():
    data = pd.read_csv('sundowner.csv')
    return data

data = load_data()  # Lade die Daten

# Aktualisieren des Mappings für die neuen Antworten und Fragen
mapping = {
    "erstes Computerprogramm für automatische Webstühle": 1,
    "den ersten Compiler": 2,
    "Den Begriff 'bug'": 3,
    "Vorgängertechnologie von Bluetooth": 4,
    "55.000 $": 1,
    "120.000 $": 2,
    "230.000 $": 3,
    "350.000 $": 4,
    "6,45 %": 1,
    "3,45 %": 2,
    "8,5 %": 3,
    "9,65 %": 4,
    "- 0,65 €": 1,
    "+ 1 €": 2,
    "+ 0,15 €": 3,
    "- 1,15 €": 4,
    "30,5 %": 1,
    "27,3 %": 2,
    "39,1 %": 3,
    "36,4 %": 4,
    "keine signifikanten Zusammenhänge": 1,
    "Pluspunkt für Kandidat:innen wenn Reisen oder Pflege von Angehörigen der Grund waren": 2,
    "Minuspunkt für Kandidat:innen wenn Ursache Kündigung war": 3,
    "empfehlenswert, weil viele Lücken = wenig Berufserfolg und umgekehrt": 4,
    "34.8 %": 1,
    "25.6 %": 2,
    "43,4 %": 3,
    "59,3 %": 4,
    "7,4 %": 1,
    "6,4 %": 2,
    "5,4 %": 3,
    "3.2 %": 4
}

# Aktualisieren der Antworten in den Daten
for col in data.columns[1:]:
    data[col] = data[col].map(mapping).astype(str) # Umschreiben der Antworten in numerische Werte

# Entfernen von NaN-Werten
data = data.dropna()

for question in data.columns[1:]:
    # Zähle die Häufigkeit jeder Bewertung für diese spezifische Frage
    rating_counts = data[question].value_counts().sort_index()

    # Histogramm
    if len(rating_counts) > 1:
        source = ColumnDataSource(data=dict(x=rating_counts.index.astype(str), y=rating_counts.values))

        p = figure(
            x_range=list(rating_counts.index),
            height=350,
            toolbar_location=None,
            title=f"{question}"
        )

        p.vbar(
            x='x',
            top='y',
            width=0.9,
            source=source,
            line_color='white',
            fill_color=factor_cmap('x', palette=Spectral4, factors=rating_counts.index)
        )

        p.xaxis.axis_label = 'Rating'
        p.yaxis.axis_label = 'Count'
        
        # Formatierung der Achsen als ganze Zahlen

        p.yaxis.formatter = NumeralTickFormatter(format='0,0')


        st.bokeh_chart(p, use_container_width=True)

    # Pie Chart
    if len(rating_counts) > 1:
        source = ColumnDataSource(data=dict(x=rating_counts.index.astype(str), y=rating_counts.values))

        p = figure(
            height=350,
            toolbar_location=None,
            title=f"{question}"
        )

        start_angle = 0
        end_angles = []

        for i, count in enumerate(rating_counts.values):
            end_angle = start_angle + 2 * pi * count / rating_counts.sum()
            end_angles.append(end_angle)
            p.wedge(
                x=0, y=0, radius=0.8,
                start_angle=start_angle, end_angle=end_angle,
                fill_color=Spectral4[i % len(Spectral4)],
                legend_label=rating_counts.index[i],
                source=source
            )
            start_angle = end_angle

        p.axis.visible = False
        p.legend.title = 'Fragen: '
        p.legend.label_text_font_size = '8pt'
        p.legend.location = "top_right"

        st.bokeh_chart(p, use_container_width=True)