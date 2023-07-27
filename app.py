import os
from flask import Flask, render_template, request, redirect, url_for, jsonify
import pandas as pd
import plotly.express as px
import plotly.offline as pyo
from plotly_generate import *

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def get_available_csvs():
    csvs = []
    for file in os.listdir(app.config['UPLOAD_FOLDER']):
        if file.endswith('.csv'):
            csvs.append(file)
    print("Available CSVs:", csvs)  # Add this line for debugging
    return csvs


def read_csv(file_name):
    return pd.read_csv(file_name)

def get_csv_data(csv_file):
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], csv_file)
    print("File path:", file_path)  # Add this line for debugging
    df = read_csv(file_path)
    return df


def get_column_names(df):
    return list(df.columns)

@app.route('/', methods=['GET', 'POST'])
def upload_csv():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file and file.filename.endswith('.csv'):
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
            return redirect(url_for('show_data', csv=file.filename, csvs=get_available_csvs()))
    return render_template('index.html', csvs=get_available_csvs())

@app.route('/show_data', methods=['GET'])
def show_data():
    csv_file = request.args.get('csv')
    df = get_csv_data(csv_file)
    if df is None:
        error_message = f"CSV file '{csv_file}' not found in the uploads folder."
        return render_template('index.html', csvs=get_available_csvs(), error=error_message)

    return render_template('index.html', csvs=get_available_csvs(), filename=csv_file, table=df.to_html(classes="table table-striped"), x_cols=get_column_names(df), y_cols=get_column_names(df))

@app.route('/plot_graph', methods=['POST'])
def plot_graph():
    csv_file = request.form.get('csv')
    graph_type = request.form.get('graph_type')
    x_col = request.form.get('x_axis')
    y_col = request.form.get('y_axis')
    z_col = request.form.get('z_axis')
    color_col = request.form.get('color_axis')

    df = get_csv_data(csv_file)
    graph = None

    #TODO not use a shit ton of ifs
    if graph_type == "line":
        graph = generate_line_plot(df, x_col, y_col)
    elif graph_type == "bar":
        graph = generate_bar_plot(df, x_col, y_col)
    elif graph_type == "scatter":
        graph = generate_scatter_plot(df, x_col, y_col)
    elif graph_type == "heatmap":
        graph = generate_heatmap(df, x_col, y_col, z_col)
    elif graph_type == "trend_line":
        graph = generate_trend_line(df, x_col, y_col)
    elif graph_type == "box_plot":
        graph = generate_box_plot(df, x_col, y_col)
    elif graph_type == "3dscatter":
        graph = generate_3d_scatter_plot(df, x_col, y_col, z_col, color_col)
    elif graph_type == "statechloro":
        graph = generate_us_state_choropleth(df, x_col, y_col, z_col)
    elif graph_type == "MLR":
        graph = generate_MIregression(df, x_col, y_col, z_col, color_col)     
    elif graph_type == "c1":
        graph = generate_customplot1(df, x_col, y_col, z_col, color_col)
    elif graph_type == "c2":
        graph = generate_customplot2(df, x_col, y_col, z_col, color_col)
    elif graph_type == "c3":
        graph = generate_customplot3(df, x_col, y_col, z_col, color_col)
    elif graph_type == "c4":
        graph = generate_customplot4(df, x_col, y_col, z_col, color_col)

    # Generate the plotly graph
    plot_div = pyo.plot(graph, output_type='div')

    return render_template('index.html', csvs=get_available_csvs(), filename=csv_file, x_cols=get_column_names(df), y_cols=get_column_names(df), graph=plot_div, graph_type=graph_type)

if __name__ == '__main__':
    app.run(debug=True)