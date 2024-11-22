dcc.Dropdown(id='site-dropdown',
             options=[
                 {'label': 'All Sites', 'value': 'ALL'},
                 {'label': 'Site 1', 'value': 'site1'},
                 {'label': 'Site 2', 'value': 'site2'},
                 {'label': 'Site 3', 'value': 'site3'},
                 {'label': 'Site 4', 'value': 'site4'}
             ],
             value='ALL',
             placeholder="Select a Launch Site here",
             searchable=True),
dcc.Graph(id='success-pie-chart')
@app.callback(
    Output('success-pie-chart', 'figure'),
    Input('site-dropdown', 'value')
)
def update_pie_chart(selected_site):
    if selected_site == 'ALL':
        df = spacex_df  # Usamos todos los datos
    else:
        df = spacex_df[spacex_df['Launch Site'] == selected_site]  # Filtramos por el sitio seleccionado

    # Crear el gráfico de pastel con los datos filtrados
    fig = px.pie(df, names='class', title=f'Successful Launches at {selected_site}')
    return fig
    dcc.RangeSlider(
    id='payload-slider',
    min=0, max=10000, step=1000,
    marks={0: '0', 1000: '1000', 5000: '5000', 10000: '10000'},
    value=[0, 10000]  # Valor inicial para el rango de carga útil
)
dcc.Graph(id='success-payload-scatter-chart')
@app.callback(
    Output('success-payload-scatter-chart', 'figure'),
    [Input('site-dropdown', 'value'),
     Input('payload-slider', 'value')]
)
def update_scatter_chart(selected_site, payload_range):
    # Filtrar los datos basados en el sitio seleccionado y el rango de carga útil
    filtered_df = spacex_df[
        (spacex_df['Payload Mass (kg)'] >= payload_range[0]) &
        (spacex_df['Payload Mass (kg)'] <= payload_range[1])
    ]
    
    if selected_site != 'ALL':
        filtered_df = filtered_df[filtered_df['Launch Site'] == selected_site]
    
    # Crear el gráfico de dispersión
    fig = px.scatter(filtered_df, x='Payload Mass (kg)', y='class',
                     color='Booster Version Category', title='Scatter plot of Payload vs Launch Success')
    return fig
    if __name__ == '__main__':
    app.run_server(port=8051)
    

