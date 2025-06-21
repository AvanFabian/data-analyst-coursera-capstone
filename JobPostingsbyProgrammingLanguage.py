import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

# 📥 Baca file Excel (sudah ada header)
df = pd.read_excel("language-job-postings.xlsx")

# 🧼 Pastikan nama kolom tidak mengandung spasi tersembunyi
df.columns = df.columns.str.strip()

# 🔽 Urutkan berdasarkan jumlah lowongan kerja secara menurun
df_sorted = df.sort_values(by="Number of Job Postings", ascending=False)

# 🚀 Inisialisasi aplikasi Dash
app = dash.Dash(__name__)
app.title = "Programming Language Job Postings"

# 📊 Layout Web
app.layout = html.Div([
    html.H1("📌 Job Postings by Programming Language", style={'textAlign': 'center'}),

    dcc.Graph(
        figure=px.bar(
            df_sorted,
            x="Language",
            y="Number of Job Postings",
            title="Number of Job Postings by Language (Descending)",
            text="Number of Job Postings",
            color="Language"
        ).update_traces(textposition="outside")
         .update_layout(xaxis_tickangle=-45, yaxis_title="Job Count", showlegend=False)
    )
])

# ▶️ Jalankan aplikasi web lokal
if __name__ == '__main__':
    app.run(debug=True)
