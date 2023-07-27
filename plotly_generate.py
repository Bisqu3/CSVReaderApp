import plotly.graph_objects as go
import plotly.express as px

#Holds all plotly graph generation functions and returns to app.py

def set_dark_theme(fig):
    fig.update_layout(template="plotly_dark")
    return fig

def generate_line_plot(dataframe, x_col, y_col):
    fig = go.Figure(data=go.Scatter(x=dataframe[x_col], y=dataframe[y_col]))
    fig.update_layout(title=f"Line Chart", xaxis_title=x_col, yaxis_title=y_col)
    return set_dark_theme(fig)

def generate_bar_plot(dataframe, x_col, y_col):
    fig = go.Figure(data=go.Bar(x=dataframe[x_col], y=dataframe[y_col]))
    fig.update_layout(title=f"Bar Chart", xaxis_title=x_col, yaxis_title=y_col)
    return set_dark_theme(fig)

def generate_scatter_plot(dataframe, x_col, y_col):
    fig = go.Figure(data=go.Scatter(x=dataframe[x_col], y=dataframe[y_col], mode='markers'))
    fig.update_layout(title=f"Scatter Plot", xaxis_title=x_col, yaxis_title=y_col)
    return set_dark_theme(fig)

def generate_heatmap(dataframe, x_col, y_col, z_col):
    fig = go.Figure(data=go.Heatmap(x=dataframe[x_col], y=dataframe[y_col], z=dataframe[z_col], colorscale='Viridis'))
    fig.update_layout(title=f"Heatmap", xaxis_title=x_col, yaxis_title=y_col)
    return set_dark_theme(fig)

def generate_trend_line(dataframe, x_col, y_col):
    fig = go.Figure(data=go.Scatter(x=dataframe[x_col], y=dataframe[y_col], mode='markers'))
    fig.update_layout(title=f"Trend Line", xaxis_title=x_col, yaxis_title=y_col)
    fig = px.scatter(dataframe, x=x_col, y=y_col, trendline='ols')
    return set_dark_theme(fig)

def generate_box_plot(dataframe, x_col, y_col):
    fig = go.Figure(data=go.Box(x=dataframe[x_col], y=dataframe[y_col], boxpoints='all', jitter=0.3, pointpos=-1.8, boxmean='sd'))
    fig.update_layout(title=f"Box Plot", xaxis_title=x_col, yaxis_title=y_col, coloraxis=dict(colorscale='Viridis'))
    return set_dark_theme(fig)

def generate_3d_scatter_plot(dataframe, x_col, y_col, z_col, color_col):
    fig = go.Figure(data=go.Scatter3d(x=dataframe[x_col], y=dataframe[y_col], z=dataframe[z_col], mode='markers',
                                     marker=dict(color=dataframe[color_col], size=5)))
    fig.update_layout(title=f"3D Scatter Plot", scene=dict(xaxis_title=x_col, yaxis_title=y_col, zaxis_title=z_col))
    return set_dark_theme(fig)

def generate_us_state_choropleth(dataframe, state_col, z_col, title=None):
    color_range = [min(dataframe[z_col]), max(dataframe[z_col])]
    fig = go.Figure(data=go.Choropleth(
        locations=dataframe[state_col],
        z=dataframe[z_col],
        locationmode='USA-states',
        colorscale='Viridis',
        colorbar=dict(title=z_col, tickvals=[color_range[0], color_range[1]]),
    ))

    # Update the layout
    if title:
        fig.update_layout(title=title)
    fig.update_geos(scope='usa')

    return set_dark_theme(fig)
def generate_MIregression(dataframe, x_col, y_col, z_col, color_col):
    color_range = [min(dataframe[color_col]), max(dataframe[color_col])]
    fig = px.scatter(
        dataframe, x=x_col, y=y_col, color=color_col,
        color_continuous_scale='Viridis', range_color=color_range, opacity=z_col,
        trendline_color_override='darkblue'
    )
    return set_dark_theme(fig)

def generate_customplot1(dataframe, x_col, y_col, z_col, color_col):
    print("")
    return None

def generate_customplot2(dataframe, x_col, y_col, z_col, color_col):
    print("")
    return None

def generate_customplot3(dataframe, x_col, y_col, z_col, color_col):
    print("")
    return None

def generate_customplot4(dataframe, x_col, y_col, z_col, color_col):
    print("")
    return None