import statistics_and_charts as sc
import pandas as pd
import altair as alt
import matplotlib.pyplot as plt

from mplsoccer import FontManager, Radar, grid

from yellowbrick.cluster import KElbowVisualizer
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram, linkage

URL1 = 'https://raw.githubusercontent.com/googlefonts/roboto/main/src/hinted/Roboto-Thin.ttf'

URL2 = ('https://raw.githubusercontent.com/google/fonts/main/apache/robotoslab/'
        'RobotoSlab%5Bwght%5D.ttf')

robotto_thin = FontManager(URL1)
robotto_bold = FontManager(URL2)
data_model = sc.data_events.loc[ (sc.data_events.position_name.notnull())
                        & (sc.data_events.position_name != 'Substitute')
                        & (sc.data_events.position_name != 'Goalkeeper')
                        & ((sc.data_events.type_name == 'Carry')
                        | (sc.data_events.type_name == 'Pass')
                        | (sc.data_events.type_name == 'Ball Recovery')
                        | (sc.data_events.type_name == 'Dribble')
                        | (sc.data_events.type_name == 'Duel')
                        | (sc.data_events.type_name == 'Shot')
                        | (sc.data_events.type_name == 'Clearance')
                        | (sc.data_events.type_name == 'Interception')
                        | (sc.data_events.type_name == 'Foul Committed')
                        | (sc.data_events.type_name == 'Foul Won')), ['match_id', 'team_name', 'position_name', 'type_name']]

data_goals =  sc.data_events.loc[ (sc.data_events['shot_outcome_name'] == 'Goal') 
                              &(sc.data_events['period'] != 5)  , ['match_id','team_name', 'shot_outcome_name'] ]

grouped_goals = data_goals.groupby(['match_id', 'team_name']).size().reset_index(name='total_goals')
stats_matches = data_model.groupby(['match_id', 'team_name', 'type_name']).size().unstack('type_name', fill_value=0).reset_index()

data_model = pd.merge(grouped_goals, stats_matches, on=['match_id', 'team_name'], how='right')
data_model['total_goals'] = (data_model['total_goals'].fillna(0)).astype('int')

data_cluster = data_model[['Ball Recovery', 'Carry','Clearance', 'Dribble', 'Duel', 'Interception', 'Pass', 'Shot', 'Foul Won', 'Foul Committed','total_goals']]

model = AgglomerativeClustering(metric = 'euclidean', linkage = 'ward')
visualizer = KElbowVisualizer(model, k=(1,10), timings = False)
visualizer.fit(data_cluster)

model_agglomerative_cluster = AgglomerativeClustering(n_clusters = visualizer.elbow_value_, metric = 'euclidean', linkage = 'ward')
y_model = model_agglomerative_cluster.fit_predict(data_cluster)
data_model['Labels'] = y_model

mapping_game_style = {0:'Agressivo', 1:'Moderado', 2:'Conservador'}

data_model['game_style'] = data_model['Labels'].map(mapping_game_style)


# Gráfico de Barras que mostra o estilo que o time mais jogou
def game_style_barchart(team):
    data = data_model.loc[(data_model['team_name'] == team)]
    
    data['game_style'].value_counts()
    
    style_dict = data['game_style'].value_counts().to_dict()
    game_style_df = pd.DataFrame(list(style_dict.items()), columns=['Game Style', 'Total'])
    
    df_sorted = game_style_df.sort_values(by='Total', ascending=False)
    
    chart = alt.Chart(df_sorted).mark_bar().encode(
        x=alt.X('Game Style:O', sort='-y', axis=alt.Axis(labelAngle=-45, title='Player', titleFontSize=14, labelFontSize=13)),
        y=alt.Y('Total:Q', axis=alt.Axis(title='Total', titleFontSize=14, labelFontSize=13)),
        color=alt.condition(
            alt.datum.is_max_assists == True,
            alt.value('#125d70'),
            alt.value('#3b8197')
        ),
        tooltip=['Game Style', 'Total']  # Adicione as informações para a tooltip
    ).properties(width=700, height=350)
    
    return chart

# Times que possuem o estilo de jogo selecionado
def game_style_teams(game_style, year):
    data = data_model.loc[(data_model['game_style'] == game_style)]
    data = pd.merge(sc.data_matches, data, on=['match_id'], how='right')
    map_year = {'Russia':2018, 'Qatar':2022}
    data['year'] = data['world_cup'].map(map_year)
    data = data[['match_id', 'year','team_name', 'total_goals', 'Ball Recovery', 'Carry',
       'Clearance', 'Dribble', 'Duel', 'Foul Committed', 'Foul Won',
       'Interception', 'Pass', 'Shot', 'match', 'game_style']]
    data = data.loc[data['year'] == year]
    return data['team_name'].value_counts().to_frame()

# DF que retorna as partidas e os estilos do time selecionado
def team_compare(team):
    data = data_model.loc[(data_model['team_name'] == team)]
    data = pd.merge(sc.data_matches, data, on=['match_id'], how='right')
    map_year = {'Russia':2018, 'Qatar':2022}
    data['year'] = data['world_cup'].map(map_year)
    data = data[['match_id', 'year','team_name', 'total_goals', 'Ball Recovery', 'Carry',
       'Clearance', 'Dribble', 'Duel', 'Foul Committed', 'Foul Won',
       'Interception', 'Pass', 'Shot', 'match', 'game_style']]
    return data

parameters = ['total_goals', 'Ball Recovery', 'Carry','Clearance', 'Dribble', 
          'Duel', 'Foul Committed', 'Foul Won','Interception', 'Pass', 'Shot']

def get_parameters_team_1(team,match_id):
    data = data_model.loc[(data_model['team_name'] == team) & (data_model['match_id'] == match_id)]
    return team,data[parameters].values

def get_parameters_team_2(team, match_id):
    data = data_model.loc[(data_model['team_name'] == team) & (data_model['match_id'] == match_id)]
    return team, data[parameters].values

def radar_chart():
    low =  [0, 20, 139, 2, 2, 3, 10, 4, 4, 196, 0]
    high = [7, 72, 926, 56, 33, 53, 37, 37, 28, 1133, 31]

    radar = Radar(parameters, low, high,
              # whether to round any of the labels to integers instead of decimal places
              round_int=[False]*len(parameters),
              num_rings=4,  # the number of concentric circles (excluding center circle)
              # if the ring_width is more than the center_circle_radius then
              # the center circle radius will be wider than the width of the concentric circles
              ring_width=1, center_circle_radius=1)
    
    team_1, parameters_1 = get_parameters_team_1('Brazil', 10)
    team_2, parameters_2 = get_parameters_team_2('Saudi Arabia', 1)
        
    #creating the figure using the grid function from mplsoccer:
    fig, axs = grid(figheight=7, grid_height=0.915, title_height=0.06, endnote_height=0.025,
                    title_space=0, endnote_space=0, grid_key='radar', axis=False)
    # plot radar
    radar.setup_axis(ax=axs['radar'])  # format axis as a radar
    rings_inner = radar.draw_circles(ax=axs['radar'], facecolor='#e6eae1', edgecolor='#e6eae1')
    radar_output = radar.draw_radar_compare(parameters_1[0], parameters_2[0], ax=axs['radar'],
                                            kwargs_radar={'facecolor': '#0094ea', 'alpha': 0.3},
                                            kwargs_compare={'facecolor': '#dc0000', 'alpha': 0.1})
    
    radar_poly, radar_poly2, vertices1, vertices2 = radar_output
    
    range_labels = radar.draw_range_labels(ax=axs['radar'], fontsize=12, fontproperties=robotto_thin.prop, color='#000000')
    param_labels = radar.draw_param_labels(ax=axs['radar'], fontsize=12,fontproperties=robotto_thin.prop, color='#000000')
    
    axs['radar'].scatter(vertices1[:, 0], vertices1[:, 1],
                         c='#0094ea', edgecolors='#0094ea', marker='o', s=50, zorder=1)
    axs['radar'].scatter(vertices2[:, 0], vertices2[:, 1],
                         c='#dc0000', edgecolors='#dc0000', marker='o', s=50, zorder=1)

    title1_text = axs['title'].text(0.01, 0.65, f'{team_1}', fontsize=15, color='#0094ea',
                                    fontproperties=robotto_bold.prop, ha='left', va='center')
    title3_text = axs['title'].text(0.99, 0.65, f'{team_2}', fontsize=15, fontproperties=robotto_bold.prop, ha='right', va='center', color='#dc0000')

    return plt.show()





















