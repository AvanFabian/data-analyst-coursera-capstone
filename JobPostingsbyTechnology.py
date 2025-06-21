import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

# Baca data dari file Excel (update path sesuai kebutuhan)
df = pd.read_excel("job-postings.xlsx", header=None, names=["Technology", "Number of Job Postings"])

# Urutkan secara descending berdasarkan jumlah lowongan
df_sorted = df.sort_values(by="Number of Job Postings", ascending=False)

# Buat aplikasi Dash
app = dash.Dash(__name__)
app.title = "Job Postings by Technology"

# Layout aplikasi
app.layout = html.Div([
    html.H1("📊 Job Postings by Technology (Ordered Desc)", style={'textAlign': 'center'}),

    dcc.Graph(
        figure=px.bar(
            df_sorted,
            x='Technology',
            y='Number of Job Postings',
            title='Job Postings per Technology (Descending Order)',
            text='Number of Job Postings',
            labels={'Number of Job Postings': 'Job Count'},
            color='Technology',
        ).update_traces(textposition='outside')
         .update_layout(xaxis_tickangle=-45, yaxis_title='Job Count', showlegend=False)
    ),

    html.P("Data diurutkan berdasarkan jumlah lowongan kerja terbanyak untuk setiap teknologi.")
])

# Jalankan server lokal
if __name__ == '__main__':
    app.run(debug=True)
