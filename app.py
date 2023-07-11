import streamlit as st
import base64
import Modules.statistics_and_charts as sc
from PIL import Image
from streamlit_extras.metric_cards import style_metric_cards

games_2018_dict = {
    "Russia X Saudi Arabia": 1,
    "Egypt X Uruguay": 2,
    "Morocco X Iran": 3,
    "Portugal X Spain": 4,
    "Croatia X Nigeria": 5,
    "France X Australia": 6,
    "Argentina X Iceland": 7,
    "Peru X Denmark": 8,
    "Costa Rica X Serbia": 9,
    "Brazil X Switzerland": 10,
    "Germany X Mexico": 11,
    "Sweden X South Korea": 12,
    "Tunisia X England": 13,
    "Belgium X Panama": 14,
    "Poland X Senegal": 15,
    "Russia X Egypt": 16,
    "Colombia X Japan": 17,
    "Portugal X Morocco": 18,
    "Uruguay X Saudi Arabia": 19,
    "Iran X Spain": 20,
    "Argentina X Croatia": 21,
    "France X Peru": 22,
    "Denmark X Australia": 23,
    "Brazil X Costa Rica": 24,
    "Nigeria X Iceland": 25,
    "Serbia X Switzerland": 26,
    "Belgium X Tunisia": 27,
    "Germany X Sweden": 28,
    "South Korea X Mexico": 29,
    "Japan X Senegal": 30,
    "Poland X Colombia": 31,
    "England X Panama": 32,
    "Spain X Morocco": 33,
    "Iran X Portugal": 34,
    "Saudi Arabia X Egypt": 35,
    "Uruguay X Russia": 36,
    "Iceland X Croatia": 37,
    "Denmark X France": 38,
    "Nigeria X Argentina": 39,
    "Australia X Peru": 40,
    "Serbia X Brazil": 41,
    "South Korea X Germany": 42,
    "Switzerland X Costa Rica": 43,
    "Mexico X Sweden": 44,
    "Japan X Poland": 45,
    "Panama X Tunisia": 46,
    "Senegal X Colombia": 47,
    "England X Belgium": 48,
    "France X Argentina": 49,
    "Uruguay X Portugal": 50,
    "Spain X Russia": 51,
    "Croatia X Denmark": 52,
    "Belgium X Japan": 53,
    "Brazil X Mexico": 54,
    "Colombia X England": 55,
    "Sweden X Switzerland": 56,
    "Brazil X Belgium": 57,
    "Uruguay X France": 58,
    "Sweden X England": 59,
    "Russia X Croatia": 60,
    "France X Belgium": 61,
    "Croatia X England": 62,
    "Belgium X England": 63,
    "France X Croatia": 64,
}

games_2022_dict = {
    "Qatar X Ecuador": 65,
    "United States X Wales": 66,
    "England X Iran": 67,
    "Senegal X Netherlands": 68,
    "Mexico X Poland": 69,
    "France X Australia": 70,
    "Argentina X Saudi Arabia": 71,
    "Denmark X Tunisia": 72,
    "Belgium X Canada": 73,
    "Morocco X Croatia": 74,
    "Spain X Costa Rica": 75,
    "Germany X Japan": 76,
    "Brazil X Serbia": 77,
    "Switzerland X Cameroon": 78,
    "Portugal X Ghana": 79,
    "Uruguay X South Korea": 80,
    "Qatar X Senegal": 81,
    "England X United States": 82,
    "Wales X Iran": 83,
    "Netherlands X Ecuador": 84,
    "Tunisia X Australia": 85,
    "Poland X Saudi Arabia": 86,
    "France X Denmark": 87,
    "Argentina X Mexico": 88,
    "Spain X Germany": 89,
    "Japan X Costa Rica": 90,
    "Belgium X Morocco": 91,
    "Croatia X Canada": 92,
    "Portugal X Uruguay": 93,
    "Cameroon X Serbia": 94,
    "Brazil X Switzerland": 95,
    "South Korea X Ghana": 96,
    "Ecuador X Senegal": 97,
    "Wales X England": 98,
    "Iran X United States": 99,
    "Netherlands X Qatar": 100,
    "Saudi Arabia X Mexico": 101,
    "Tunisia X France": 102,
    "Poland X Argentina": 103,
    "Australia X Denmark": 104,
    "Croatia X Belgium": 105,
    "Costa Rica X Germany": 106,
    "Canada X Morocco": 107,
    "Japan X Spain": 108,
    "South Korea X Portugal": 109,
    "Ghana X Uruguay": 110,
    "Serbia X Switzerland": 111,
    "Cameroon X Brazil": 112,
    "Argentina X Australia": 113,
    "Netherlands X United States": 114,
    "England X Senegal": 115,
    "France X Poland": 116,
    "Brazil X South Korea": 117,
    "Japan X Croatia": 118,
    "Portugal X Switzerland": 119,
    "Morocco X Spain": 120,
    "Croatia X Brazil": 121,
    "Netherlands X Argentina": 122,
    "Morocco X Portugal": 123,
    "England X France": 124,
    "Argentina X Croatia": 125,
    "France X Morocco": 126,
    "Croatia X Morocco": 127,
    "Argentina X France": 128,
}

teams_list = [
    "Argentina",
    "Australia",
    "Belgium",
    "Brazil",
    "Cameroon",
    "Canada",
    "Colombia",
    "Costa Rica",
    "Croatia",
    "Denmark",
    "Ecuador",
    "Egypt",
    "England",
    "France",
    "Germany",
    "Ghana",
    "Iceland",
    "Iran",
    "Japan",
    "Mexico",
    "Morocco",
    "Netherlands",
    "Nigeria",
    "Panama",
    "Peru",
    "Poland",
    "Portugal",
    "Qatar",
    "Russia",
    "Saudi Arabia",
    "Senegal",
    "Serbia",
    "South Korea",
    "Spain",
    "Sweden",
    "Switzerland",
    "Tunisia",
    "United States",
    "Uruguay",
    "Wales",
]

teams_list_2018 = [
    "Argentina",
    "Australia",
    "Belgium",
    "Brazil",
    "Colombia",
    "Costa Rica",
    "Croatia",
    "Denmark",
    "Egypt",
    "England",
    "France",
    "Germany",
    "Iceland",
    "Iran",
    "Japan",
    "Mexico",
    "Morocco",
    "Nigeria",
    "Panama",
    "Peru",
    "Poland",
    "Portugal",
    "Russia",
    "Saudi Arabia",
    "Senegal",
    "Serbia",
    "South Korea",
    "Spain",
    "Sweden",
    "Switzerland",
    "Tunisia",
    "Uruguay",
]

teams_list_2022 = [
    "Argentina",
    "Australia",
    "Belgium",
    "Brazil",
    "Cameroon",
    "Canada",
    "Costa Rica",
    "Croatia",
    "Denmark",
    "Ecuador",
    "England",
    "France",
    "Germany",
    "Ghana",
    "Iran",
    "Japan",
    "Mexico",
    "Morocco",
    "Netherlands",
    "Poland",
    "Portugal",
    "Qatar",
    "Saudi Arabia",
    "Senegal",
    "Serbia",
    "South Korea",
    "Spain",
    "Switzerland",
    "Tunisia",
    "United States",
    "Uruguay",
    "Wales",
]

world_cup_dict = {"Russia": 2018, "Qatar": 2022}


# Configurações da página
def page_configs():
    st.set_option("deprecation.showPyplotGlobalUse", False)
    st.set_page_config(page_title="World Cup Analysis", page_icon="⚽️", layout="wide")
    style_metric_cards(border_left_color="#1E1E1E")

    hide_default_format = """
        <style>
        footer {visibility: hidden;}
        </style>
        """

    st.markdown(
        """
    <style>
        h1 {
            font-size: 40px;
        }
    </style>
""",
        unsafe_allow_html=True,
    )

    st.markdown(hide_default_format, unsafe_allow_html=True)


def overview():
    file_1 = open("Images/Team lineup.gif", "rb")
    contents_1 = file_1.read()
    data_url_1 = base64.b64encode(contents_1).decode("utf-8")
    file_1.close()

    left_col_1, right_col_1 = st.columns(2)

    with left_col_1:
        st.markdown("# ")
        st.markdown(
            "### Ciência de Dados e Inteligência Artificial Aplicadas no Futebol Moderno"
        )
        st.markdown("**Criado por Gabriel de Jesus Nunes da Costa**")
        st.markdown("**Data Scientist**")
        st.markdown('<hr style="border:1px solid #125d70">', unsafe_allow_html=True)
        st.markdown(
            f'<p style="background-color:#FBFBFB;color:black;font-size:23px;border-radius:2%;text-align:center;"><strong>Resumo</strong></p>',
            unsafe_allow_html=True,
        )
        st.markdown(
            '<div style="text-align: justify;"> \
                    O projeto tem como objetivo demonstrar o potencial da ciência de dados e inteligência artificial para aprimorar o desempenho de jogadores e equipes de futebol, além de auxiliar a equipe técnica na tomada de decisões. \
                    Por meio de visualizações personalizadas, a equipe técnica pode desenvolver táticas mais eficientes, analisar o desempenho coletivo da equipe e estudar o comportamento individual dos jogadores. O projeto concentra-se \
                    na análise de dados das edições da Copa do Mundo de 2018 e 2022, com foco especial nos aspectos de passes e finalizações das equipes. Dessa forma, busca identificar padrões que possam contribuir para um melhor \
                    entendimento e aprimoramento desses elementos-chave do jogo. Todos os dados utilizados para criação do projeto é proveniente da empresa Statsbomb. </div>',
            unsafe_allow_html=True,
        )

    with right_col_1:
        st.markdown(
            '<div style="text-align: center;">'
            f'<img src="data:image/gif;base64,{data_url_1}" alt="soccer gif">'
            "</div>",
            unsafe_allow_html=True,
        )

    st.markdown('<hr style="border:1px solid #125d70">', unsafe_allow_html=True)

    left_col_2, right_col_2 = st.columns(2)

    # Se der tempo colocar análise da base de dados
    with left_col_2:
        st.markdown(
            f'<p style="background-color:#FBFBFB;color:black;font-size:23px;border-radius:2%;text-align:center;"><strong>Uso da ferramenta</strong></p>',
            unsafe_allow_html=True,
        )

        st.markdown(
            "No canto superior esquerdo, há um aba com o menu principal para navigar em cada página do projeto."
        )
        st.markdown(
            '<div style="text-align: justify;"> • <strong>Overview do Projeto:</strong> Você esta aqui! </div>',
            unsafe_allow_html=True,
        )
        st.markdown(
            '<div style="text-align: justify;"> • <strong>Análise Geral da Seleção:</strong>  O resumo geral das seleções apresenta informações relevantes sobre os jogos disputados, incluindo o número de vitórias, derrotas e empates. Além disso, fornece uma visão geral da movimentação dos jogadores das seleções, oferecendo dados importantes sobre o desempenho individual e coletivo. </div>',
            unsafe_allow_html=True,
        )
        st.markdown(
            '<div style="text-align: justify;"> • <strong>Análise de Finalização:</strong>  A análise de finalização oferece uma abordagem minuciosa e detalhada sobre os chutes executados pelas seleções. Nesse estudo, são investigados diversos aspectos relacionados às finalizações,como localização dos chutes no campo, gols esperados, artilheiros do time e outras métricas. Essa análise busca fornecer insights valiosos sobre a eficiência e eficácia das seleções ao concluir suas jogadas ofensivas, destacando pontos fortes e áreas que podem ser aprimoradas. Ao examinar os dados e padrões das finalizações, é possível obter uma compreensão mais precisa do desempenho das equipes nesse aspecto crucial do jogo.</div>',
            unsafe_allow_html=True,
        )
        st.markdown(
            '<div style="text-align: justify;"> • <strong>Análise da Troca de Passes:</strong>  A análise da troca de passes busca fornecer uma visão abrangente do desempenho da equipe nesse aspecto fundamental do jogo. Essa análise abrange diversos indicadores, incluindo a média de passes por jogo, o total de passes realizados, os passes que resultaram em chutes a gol, o número total de assistências, além da localização dos passes realizados pelos jogadores. Além disso, são avaliados aspectos como a posse de bola, a área de passes mais utilizada e os jogadores que se destacam pela quantidade de passes efetuados. Essa análise visa proporcionar insights valiosos sobre a eficiência da equipe na troca de passes, destacando pontos fortes, padrões de jogo e áreas que podem ser aprimoradas. Dessa forma, é possível compreender mais profundamente a dinâmica da equipe em relação à construção de jogadas e à criação de oportunidades ofensivas.</div>',
            unsafe_allow_html=True,
        )
        st.markdown(
            '<div style="text-align: justify;"> • <strong>Análise do Modelo:</strong>  Para esse painel foi realizado uma aplicação e posteriormente uma análise de cluster para identificar padrões de estilo de jogo das seleções.</div>',
            unsafe_allow_html=True,
        )

    st.markdown('<hr style="border:1px solid #125d70">', unsafe_allow_html=True)

    with right_col_2:
        st.markdown(
            f'<p style="background-color:#FBFBFB;color:#FBFBFB;font-size:34px;border-radius:2%;text-align:center;"><strong>Resumo</strong></p>',
            unsafe_allow_html=True,
        )
        file_2 = open("Images/Soccer.gif", "rb")
        contents_2 = file_2.read()
        data_url_2 = base64.b64encode(contents_2).decode("utf-8")
        file_2.close()
        st.markdown(
            '<div style="text-align: center;">'
            f'<img src="data:image/gif;base64,{data_url_2}" alt="soccer gif">'
            "</div>",
            unsafe_allow_html=True,
        )

    left_col_3, right_col_3 = st.columns(2)

    with left_col_3:
        st.markdown(
            f'<p style="background-color:#FBFBFB;color:black;font-size:23px;border-radius:2%;text-align:center;"><strong>Sobre mim</strong></p>',
            unsafe_allow_html=True,
        )
        st.markdown(
            f'<p style="background-color:#FBFBFB;color:#FBFBFB;font-size:10;border-radius:2%;text-align:center;"><strong>Sobre mim</strong></p>',
            unsafe_allow_html=True,
        )

        st.markdown(
            '<div style="text-align: justify;">👋🏻 Olá, meu nome é Gabriel de Jesus, e \
                    atualmente estou cursando Bacharelado em Ciência de Dados e Inteligência Artificial no Centro Universitário IESB e gosto das áreas de Data Analytics, \
                    Data Visualization, Machine Learning e Business Intelligence. Tenho experiência como Estagiário de Data Engineer na IBM Brasil e como Estagiário de Data Scientist na Vert Technology \
                    and Information, onde desenvolvi habilidades em Data Analytics, Data Visualization, Python, Business Intelligence, Machine Learning, Matemática e Estatística, Power BI/Tableau e SQL</div>',
            unsafe_allow_html=True,
        )

    with right_col_3:
        st.markdown(
            f'<p style="background-color:#FBFBFB;color:black;font-size:23px;border-radius:2%;text-align:center;"><strong>Autor</strong></p>',
            unsafe_allow_html=True,
        )
        image_1 = Image.open("Images/profile.png")
        st.image(image_1)
    st.markdown('<hr style="border:1px solid #125d70">', unsafe_allow_html=True)

    left_col_4, _ = st.columns(2)
    with left_col_4:
        st.markdown(
            f'<p style="background-color:#FBFBFB;color:black;font-size:23px;border-radius:2%;text-align:center;"><strong>Contato</strong></p>',
            unsafe_allow_html=True,
        )
    st.markdown(
        f"""

        Sinta-se à vontade para entrar em contato comigo com quaisquer problemas, comentários ou perguntas.

        - LinkedIn: https://www.linkedin.com/in/gabrieljnc
        - Email:  <gabrieljnc.contato@outlook.com>
        - GitHub: https://github.com/Gabrieljnc
        - Repositório: https://github.com/Gabrieljnc/World_Cup_Analysis
        """,
        unsafe_allow_html=True,
    )


def flag_matches(match):
    st.markdown("##### Partida selecionada: ")
    team_home, team_away = sc.flag_matches(match)

    home_team = Image.open(f"Images/Teams/{team_home}.png")
    away_team = Image.open(f"Images/Teams/{team_away}.png")

    new_size_flags = (150, 80)  # Substitua "largura" e "altura" pelos valores desejados

    # Redimensionar a imagem
    image_resized_home_team = home_team.resize(new_size_flags)
    image_resized_away_team = away_team.resize(new_size_flags)

    _, _, _, _, _, home_team_col, x_col, away_team_col, _, _, _, _, _ = st.columns(13)

    with home_team_col:
        st.image(image_resized_home_team, caption=team_home)
    with x_col:
        st.markdown(
            "<h1 style='text-align:center; font-size:45px; margin-top: -15px;'>X</h1>",
            unsafe_allow_html=True,
        )
    with away_team_col:
        st.image(image_resized_away_team, caption=team_away)

    st.markdown('<hr style="border:2px solid #125d70">', unsafe_allow_html=True)


def flag_main_team(team):
    st.markdown("##### Seleção selecionada:")

    main_team = Image.open(f"Images/Teams/{team}.png")

    new_size_flags = (150, 80)  # Substitua "largura" e "altura" pelos valores desejados

    # Redimensionar a imagem
    image_resized_main_team = main_team.resize(new_size_flags)

    _, _, _, mid, _, _, _ = st.columns(7)

    with mid:
        st.image(image_resized_main_team, caption=team)

    st.markdown('<hr style="border:2px solid #125d70">', unsafe_allow_html=True)


def introduction_text():
    table_text = st.checkbox("Informações sobre as colunas")
    if table_text:
        texto = """

    As colunas abaixo fornecem informações importantes sobre cada partida da seleção escolhida, incluindo os times envolvidos, o placar final, a data, o estágio da competição e se a partida faz parte de uma Copa do Mundo. Com base nessas informações, você pode realizar diversas análises e extração de insights relacionados aos jogos e ao desempenho das equipes.


    ###### Colunas da Tabela

    1. **match_id**: Esse campo representa o identificador único de cada partida. Cada partida terá um match_id exclusivo, permitindo a identificação e referência específica de cada jogo.

    2. **home_team_name**: Essa coluna indica o nome da equipe da casa, ou seja, é o time que possui o mando de campo na partida em questão.

    3. **away_team_name**: Essa coluna mostra o nome da equipe visitante, ou seja, é o time que enfrenta a equipe da casa na partida em questão.

    4. **final_score**: Essa coluna exibe o placar final da partida, ou seja, o resultado final do jogo após o tempo regulamentar.

    5. **match_date**: Essa coluna representa a data em que a partida ocorreu. Ela fornece informações sobre o dia em que o jogo foi realizado, permitindo que os dados sejam organizados e consultados cronologicamente.

    6. **stage**: Essa coluna indica a fase ou etapa em que a partida ocorreu. Na Copa do Mundo existem diferentes estágios, como fase de grupos, oitavas de final, quartas de final, semifinais e final. 

    7. **world_cup**: Essa coluna é indicador que mostra qual país foi realizado a Copa do Mundo

    """

        st.markdown(texto)
    else:
        print("")


# -------------Análise Geral da Seleção-----------------


def cards_with_informations(team, world_cup):
    st.markdown('<hr style="border:2px solid #125d70">', unsafe_allow_html=True)
    st.markdown(
        f'<p style="background-color:#FBFBFB;color:black;font-size:23px;border-radius:2%;text-align:center;"><strong>Estatísticas Gerais</strong></p>',
        unsafe_allow_html=True,
    )

    total_of_matches_2018 = sc.total_of_matches(team, "Russia")
    total_of_gols_scored_2018 = sc.total_goals_scored(team, "Russia")
    total_of_gols_conceded_2018 = sc.total_goals_conceded(team, "Russia")
    win_2018, draw_2018, lose_2018 = sc.win_draw_lose(team, "Russia")

    total_of_matches_2022 = sc.total_of_matches(team, "Qatar")
    total_of_gols_scored_2022 = sc.total_goals_scored(team, "Qatar")
    total_of_gols_conceded_2022 = sc.total_goals_conceded(team, "Qatar")
    win_2022, draw_2022, lose_2022 = sc.win_draw_lose(team, "Qatar")
    card_1, card_2, card_3, card_4, card_5, card_6 = st.columns(6)

    if world_cup == "Russia":
        card_1.metric("Total de Jogos", value=total_of_matches_2018)
        card_2.metric("Total de Gols a Favor", value=total_of_gols_scored_2018)
        card_3.metric("Total de Gols Sofrido", value=total_of_gols_conceded_2018)
        card_4.metric("Total de Vitórias", value=win_2018)
        card_5.metric("Total de Empates", value=draw_2018)
        card_6.metric("Total de Derrotas", value=lose_2018)

    if world_cup == "Qatar":
        card_1.metric(
            "Total de Jogos",
            value=total_of_matches_2022,
            delta=int(total_of_matches_2022 - total_of_matches_2018),
        )
        card_2.metric(
            "Total de Gols a Favor",
            value=total_of_gols_scored_2022,
            delta=int(total_of_gols_scored_2022 - total_of_gols_scored_2018),
        )
        card_3.metric(
            "Total de Gols Sofrido",
            value=total_of_gols_conceded_2022,
            delta=int(total_of_gols_conceded_2022 - total_of_gols_conceded_2018),
        )
        card_4.metric(
            "Total de Vitórias", value=win_2022, delta=int(win_2022 - win_2018)
        )
        card_5.metric(
            "Total de Empates", value=draw_2022, delta=int(draw_2022 - draw_2018)
        )
        card_6.metric(
            "Total de Derrotas", value=lose_2022, delta=int(lose_2022 - lose_2018)
        )

    st.markdown('<hr style="border:2px solid #125d70">', unsafe_allow_html=True)


def top_playes_bar_chart(team, wc_country):
    if wc_country == "Russia":
        year = 2018
    else:
        year = 2022

    col_1_bar_plot, col_2_bar_plot = st.columns(2)

    with col_1_bar_plot:
        st.markdown(
            f'<p style="background-color:#FBFBFB;color:black;font-size:23px;border-radius:2%;text-align:center;"><strong>Jogadores que possuem mais Gols</strong></p>',
            unsafe_allow_html=True,
        )
        st.markdown(
            f'<p style="background-color:#FBFBFB;color:#FBFBFB;font-size:23px;border-radius:2%;"><strong>.</strong></p>',
            unsafe_allow_html=True,
        )

        st.altair_chart(sc.top_scores_by_team(team, year))

    with col_2_bar_plot:
        st.markdown(
            f'<p style="background-color:#FBFBFB;color:black;font-size:23px;border-radius:2%;text-align:center;"><strong>Jogadores que possuem mais Assistências</strong></p>',
            unsafe_allow_html=True,
        )
        st.markdown(
            f'<p style="background-color:#FBFBFB;color:#FBFBFB;font-size:23px;border-radius:2%;"><strong>.</strong></p>',
            unsafe_allow_html=True,
        )

        st.altair_chart(sc.top_assists_by_team(team, year))

    st.markdown('<hr style="border:2px solid #125d70">', unsafe_allow_html=True)


def players_and_heatmap(team, wc_country, match):
    if wc_country == "Russia":
        game_ids_passes = games_2018_dict[match]
    if wc_country == "Qatar":
        game_ids_passes = games_2022_dict[match]

    col_1, col_2 = st.columns(2)
    df = sc.players_by_team(game_ids_passes, team)
    list_of_players = set(df["Player"])

    with col_1:
        st.markdown(
            f'<p style="background-color:#FBFBFB;color:black;font-size:23px;border-radius:2%;text-align:center;"><strong>Jogadores</strong></p>',
            unsafe_allow_html=True,
        )

        player = st.selectbox(
            "Escolha um jogador para analisar", options=list_of_players
        )
        st.dataframe(
            sc.players_by_team(game_ids_passes, team),
            use_container_width=True,
            height=550,
        )

    with col_2:
        st.markdown(
            f'<p style="background-color:#FBFBFB;color:black;font-size:23px;border-radius:2%;text-align:center;"><strong>Heatmap da Movimentação dos Jogadores</strong></p>',
            unsafe_allow_html=True,
        )
        choice_move = st.radio(
            "Escolha o Tempo para analise de movimentação ",
            [
                "1˚ Tempo",
                "2˚ Tempo",
                "1˚ Tempo - Prorrogação",
                "2˚ Tempo - Prorrogação",
            ],
            horizontal=True,
        )
        st.markdown(
            f'<p style="background-color:#FBFBFB;color:#FBFBFB;font-size:3px;border-radius:2%;text-align:center;"><strong>Heatmap da Movimentação dos Jogadores</strong></p>',
            unsafe_allow_html=True,
        )

        if choice_move == ("1˚ Tempo"):
            period_pass_team_analysis = 1
        elif choice_move == ("2˚ Tempo"):
            period_pass_team_analysis = 2
        elif choice_move == ("1˚ Tempo - Prorrogação"):
            period_pass_team_analysis = 3
        else:
            period_pass_team_analysis = 4

        st.pyplot(
            sc.heatmap(game_ids_passes, player, period_pass_team_analysis),
            use_container_width=True,
        )

    st.markdown('<hr style="border:2px solid #125d70">', unsafe_allow_html=True)


# --------------Análise da Troca de Passes-----------


def cards_with_pass_information(world_cup, team, match):
    st.markdown(
        f'<p style="background-color:#FBFBFB;color:black;font-size:23px;border-radius:2%;text-align:center;"><strong>Estatísticas Gerais</strong></p>',
        unsafe_allow_html=True,
    )

    card_1, card_2, card_3, card_4 = st.columns(4)

    if world_cup == "Russia":
        match_id = games_2018_dict[match]
    if world_cup == "Qatar":
        match_id = games_2022_dict[match]

    with card_1:
        card_1.metric(
            "Média de Passes na Competição",
            value=sc.passing_average_per_game(team, match_id),
        )
    with card_2:
        card_2.metric("Total de Passes", value=sc.total_passes(team, match_id))
    with card_3:
        card_3.metric(
            "Total de Passes para Chute", value=sc.total_passes_per_shot(team, match_id)
        )
    with card_4:
        card_4.metric(
            "Total de Assistências para Gol",
            value=sc.total_assists_per_goal(team, match_id),
        )

    st.markdown('<hr style="border:2px solid #125d70">', unsafe_allow_html=True)


def passes_per_minute(match, world_cup):
    if world_cup == "Russia":
        match_id = games_2018_dict[match]
        year = 2018

    if world_cup == "Qatar":
        match_id = games_2022_dict[match]
        year = 2022

    col_1_passes_minute, col_2_ball_possession = st.columns(2)

    with col_1_passes_minute:
        st.markdown(
            f'<p style="background-color:#FBFBFB;color:black;font-size:23px;border-radius:2%;text-align:center;"><strong>Posse de Bola por Minuto</strong></p>',
            unsafe_allow_html=True,
        )
        minute = st.slider("Qual minuto você deseja analisar", 0, 110)
        st.altair_chart(
            sc.total_passes_per_minute(match_id, minute, year), use_container_width=True
        )
    with col_2_ball_possession:
        st.markdown(
            f'<p style="background-color:#FBFBFB;color:black;font-size:23px;border-radius:2%;text-align:center;"><strong>Posse de Bola Final do Jogo ( % )</strong></p>',
            unsafe_allow_html=True,
        )
        st.altair_chart(sc.pie_chart_possession(match_id), use_container_width=True)

    st.markdown('<hr style="border:2px solid #125d70">', unsafe_allow_html=True)
    return minute


def pass_map_chart(match, team, world_cup):
    st.slider()
    if world_cup == "Russia":
        match_id = games_2018_dict[match]

    if world_cup == "Qatar":
        match_id = games_2022_dict[match]

    st.pyplot(sc.pass_map(match_id, team), use_container_width=True)


def pass_leading_to_shots(match, team, world_cup):
    if world_cup == "Russia":
        match_id = games_2018_dict[match]

    if world_cup == "Qatar":
        match_id = games_2022_dict[match]

    st.pyplot(sc.pass_leading_to_shots(match_id, team), use_container_width=True)


def convex_hull_passes_and_heatmap_of_passes(match, team, world_cup):
    if world_cup == "Russia":
        match_id = games_2018_dict[match]

    if world_cup == "Qatar":
        match_id = games_2022_dict[match]

    data = sc.players_by_team(match_id, team)
    list_of_players = sorted(set(data["Player"]))

    col_1_pass_map_title, col_2_heatmap_pass_title = st.columns(2)
    with col_1_pass_map_title:
        st.markdown(
            f'<p style="color:black;font-size:23px;border-radius:2%;text-align:center;"><strong>Convex Hull - Passes</strong></p>',
            unsafe_allow_html=True,
        )
        period = st.radio(
            " Qual tempo deseja analisar ? ",
            [
                "1˚ Tempo",
                "2˚ Tempo",
                "1˚ Tempo - Prorrogação",
                "2˚ Tempo - Prorrogação",
            ],
            horizontal=True,
        )

    with col_2_heatmap_pass_title:
        st.markdown(
            f'<p style="color:black;font-size:23px;border-radius:2%;text-align:center;"><strong>Heatmap - Passes</strong></p>',
            unsafe_allow_html=True,
        )
        player = st.selectbox(
            "Escolha um jogador para analisar", options=list_of_players
        )

    if period == ("1˚ Tempo"):
        period_pass_analysis = 1
    elif period == ("2˚ Tempo"):
        period_pass_analysis = 2
    elif period == ("1˚ Tempo - Prorrogação"):
        period_pass_analysis = 3
    else:
        period_pass_analysis = 4

    col_left_space, col_right_space = st.columns(2)
    with col_right_space:
        st.markdown(
            f'<p style="color:#FBFBFB;font-size:18px;border-radius:2%;text-align:center;"><strong>Heatmap - Passes</strong></p>',
            unsafe_allow_html=True,
        )

    col_1_pass_map, col_2_heatmap_pass = st.columns(2)
    with col_1_pass_map:
        try:
            st.pyplot(
                sc.convex_hull_passes(player, match_id, period_pass_analysis),
                use_container_width=True,
            )
        except:
            st.write("O jogador não participou do tempo selecionado")

    with col_2_heatmap_pass:
        st.markdown(
            f'<p style="color:#FBFBFB;font-size:3px;border-radius:2%;text-align:center;"><strong>Heatmap - Passes</strong></p>',
            unsafe_allow_html=True,
        )
        st.pyplot(
            sc.heatmap_of_passes(player, match_id, period_pass_analysis),
            use_container_width=True,
        )

    st.markdown('<hr style="border:2px solid #125d70">', unsafe_allow_html=True)


def line_chart_and_player_more_passes(match, team, world_cup):
    if world_cup == "Russia":
        match_id = games_2018_dict[match]
        year = 2018
    if world_cup == "Qatar":
        match_id = games_2022_dict[match]
        year = 2022

    col_1_team_pass, col_2_players_pass = st.columns(2)

    with col_1_team_pass:
        st.markdown(
            f'<p style="background-color:#FBFBFB;color:black;font-size:23px;border-radius:2%;text-align:center;"><strong>Total de Passes por Partida</strong></p>',
            unsafe_allow_html=True,
        )
        st.altair_chart(sc.number_of_passes(match_id, year), use_container_width=True)
    with col_2_players_pass:
        st.markdown(
            f'<p style="background-color:#FBFBFB;color:black;font-size:23px;border-radius:2%;text-align:center;"><strong>Jogadores com Mais Passes na Partida</strong></p>',
            unsafe_allow_html=True,
        )
        st.altair_chart(
            sc.players_with_more_passes(team, match_id, year), use_container_width=True
        )

    st.markdown('<hr style="border:2px solid #125d70">', unsafe_allow_html=True)


def ball_passer_receiver_and_pass_network(team, match, world_cup):
    if world_cup == "Russia":
        match_id = games_2018_dict[match]
    if world_cup == "Qatar":
        match_id = games_2022_dict[match]

    col_left, col_right = st.columns(2)

    with col_left:
        st.markdown(
            f'<p style="background-color:#FBFBFB;color:black;font-size:23px;border-radius:2%;text-align:center;"><strong>Troca de passes</strong></p>',
            unsafe_allow_html=True,
        )
        period = st.radio(
            "Escolha o tempo para analise ",
            [
                "1˚ Tempo",
                "2˚ Tempo",
                "1˚ Tempo - Prorrogação",
                "2˚ Tempo - Prorrogação",
            ],
            horizontal=True,
        )

    if period == ("1˚ Tempo"):
        period_pass_analysis = 1
    elif period == ("2˚ Tempo"):
        period_pass_analysis = 2
    elif period == ("1˚ Tempo - Prorrogação"):
        period_pass_analysis = 3
    else:
        period_pass_analysis = 4

    with col_right:
        st.markdown(
            f'<p style="background-color:#FBFBFB;color:black;font-size:23px;border-radius:2%;text-align:center;"><strong>Conexões das Troca de passes</strong></p>',
            unsafe_allow_html=True,
        )

    col_1_players_pass, col_2_pass_network = st.columns(2)

    with col_1_players_pass:
        st.dataframe(
            sc.ball_passer_receiver(team, match_id, period_pass_analysis),
            width=860,
            height=700,
            use_container_width=True,
        )
    with col_2_pass_network:
        st.pyplot(
            sc.pass_network(match_id, team, period_pass_analysis),
            use_container_width=True,
        )

    st.markdown('<hr style="border:2px solid #125d70">', unsafe_allow_html=True)


def pass_analysis(match, team, world_cup):
    if world_cup == "Russia":
        match_id = games_2018_dict[match]
    if world_cup == "Qatar":
        match_id = games_2022_dict[match]

    st.markdown(
        f'<p style="background-color:#FBFBFB;color:black;font-size:23px;border-radius:2%;text-align:center;"><strong>Área de Passes</strong></p>',
        unsafe_allow_html=True,
    )

    col_left, _ = st.columns(2)

    with col_left:
        choice = st.radio(
            "Escolha o Tempo para analise ",
            [
                "1˚ Tempo",
                "2˚ Tempo",
                "1˚ Tempo - Prorrogação",
                "2˚ Tempo - Prorrogação",
            ],
            horizontal=True,
        )

    if choice == ("1˚ Tempo"):
        period_pass_team_analysis = 1
    elif choice == ("2˚ Tempo"):
        period_pass_team_analysis = 2
    elif choice == ("1˚ Tempo - Prorrogação"):
        period_pass_team_analysis = 3
    else:
        period_pass_team_analysis = 4

    st.pyplot(
        sc.pass_analisys(match_id, team, period_pass_team_analysis),
        use_container_width=True,
    )
    st.markdown('<hr style="border:2px solid #125d70">', unsafe_allow_html=True)


def arrow_passes_and_pass_lead_shot(match, team, world_cup):
    if world_cup == "Russia":
        match_id = games_2018_dict[match]
        year = 2018

    if world_cup == "Qatar":
        match_id = games_2022_dict[match]
        year = 2022

    col_1_arrow_passes, col_2_passes_ls = st.columns(2)

    with col_1_arrow_passes:
        st.markdown(
            f'<p style="background-color:#FBFBFB;color:black;font-size:23px;border-radius:2%;text-align:center;"><strong>Direção média dos Passes </strong></p>',
            unsafe_allow_html=True,
        )
        st.markdown(
            f'<p style="background-color:#FBFBFB;color:#FBFBFB;font-size:6px;border-radius:2%;text-align:center;"><strong>Direção média dos Passes </strong></p>',
            unsafe_allow_html=True,
        )
        st.pyplot(sc.arrow_passes(match_id, team, year), use_container_width=True)
    with col_2_passes_ls:
        st.markdown(
            f'<p style="background-color:#FBFBFB;color:black;font-size:23px;border-radius:2%;text-align:center;"><strong>Passes para Chute</strong></p>',
            unsafe_allow_html=True,
        )
        st.pyplot(
            sc.pass_leading_to_shots(match_id, team, year), use_container_width=True
        )

    st.markdown('<hr style="border:2px solid #125d70">', unsafe_allow_html=True)


# --------------Análise da Finalização-----------


def cards_with_shots_information(world_cup, team, match):
    st.markdown(
        f'<p style="background-color:#FBFBFB;color:black;font-size:23px;border-radius:2%;text-align:center;"><strong>Estatísticas de Finalização</strong></p>',
        unsafe_allow_html=True,
    )

    card_1, card_2, card_3, card_4, card_5 = st.columns(5)

    if world_cup == "Russia":
        match_id = games_2018_dict[match]
        year = 2018
    if world_cup == "Qatar":
        match_id = games_2022_dict[match]
        year = 2022

    with card_1:
        card_1.metric(
            "Média de Finalizações por Jogo",
            value=sc.avg_shots_per_game(team, world_cup),
        )
    with card_2:
        card_2.metric(
            "Média de Finalizações no Gol por Jogo",
            value=sc.avg_shots_on_target_per_game(team, world_cup),
        )
    with card_3:
        card_3.metric(
            "Total de Finalizações", value=sc.total_shots_match(match_id, team, year)
        )
    with card_4:
        card_4.metric(
            "Total de Chutes no Gol",
            value=sc.total_shots_on_target(match_id, team, year),
        )
    with card_5:
        card_5.metric(
            "Precisão das Finalizações",
            value=f"{sc.shots_precision(match_id, team, year)}%",
        )

    st.markdown('<hr style="border:2px solid #125d70">', unsafe_allow_html=True)


def line_chart_and_player_more_shots(match, team, world_cup):
    if world_cup == "Russia":
        match_id = games_2018_dict[match]
        year = 2018
    if world_cup == "Qatar":
        match_id = games_2022_dict[match]
        year = 2022

    col_1_team_shots, col_2_players_shots = st.columns(2)

    with col_1_team_shots:
        st.markdown(
            f'<p style="background-color:#FBFBFB;color:black;font-size:23px;border-radius:2%;text-align:center;"><strong>Total de Finalizações por Partida</strong></p>',
            unsafe_allow_html=True,
        )
        st.altair_chart(sc.number_of_shots(match_id, year), use_container_width=True)
    with col_2_players_shots:
        st.markdown(
            f'<p style="background-color:#FBFBFB;color:black;font-size:23px;border-radius:2%;text-align:center;"><strong>Jogadores com Mais Finalizações na Partida</strong></p>',
            unsafe_allow_html=True,
        )
        st.altair_chart(
            sc.players_with_more_shots(team, match_id, year), use_container_width=True
        )

    st.markdown('<hr style="border:2px solid #125d70">', unsafe_allow_html=True)


def kde_shots_and_jointgrid(match, world_cup):
    if world_cup == "Russia":
        match_id = games_2018_dict[match]
        year = 2018
    if world_cup == "Qatar":
        match_id = games_2022_dict[match]
        year = 2022

    col_1_team_shots, col_2_players_shots = st.columns(2)

    with col_1_team_shots:
        st.markdown(
            f'<p style="background-color:#FBFBFB;color:black;font-size:23px;border-radius:2%;text-align:center;"><strong>Heatmap das Distribuições de Finalizações</strong></p>',
            unsafe_allow_html=True,
        )
        st.pyplot(sc.kde_shot_map(match_id, year), use_container_width=True)
    with col_2_players_shots:
        st.markdown(
            f'<p style="background-color:#FBFBFB;color:black;font-size:23px;border-radius:2%;text-align:center;"><strong>Distribuição e Scatter Plot dos XG(Expected Goals)</strong></p>',
            unsafe_allow_html=True,
        )
        st.pyplot(sc.shots_jointgrid(match_id, year), use_container_width=True)

    st.markdown('<hr style="border:2px solid #125d70">', unsafe_allow_html=True)


def scatterplot_line_xg_and_shots(match, team, world_cup):
    if world_cup == "Russia":
        match_id = games_2018_dict[match]
    if world_cup == "Qatar":
        match_id = games_2022_dict[match]

    col_left_title, col_right_title = st.columns(2)

    with col_left_title:
        st.markdown(
            f'<p style="background-color:#FBFBFB;color:black;font-size:23px;border-radius:2%;text-align:center;"><strong>Scatterplot de XG por Resultado de Finalização</strong></p>',
            unsafe_allow_html=True,
        )

    with col_right_title:
        st.markdown(
            f'<p style="background-color:#FBFBFB;color:black;font-size:23px;border-radius:2%;text-align:center;"><strong>Mapa de Chutes</strong></p>',
            unsafe_allow_html=True,
        )

    col_left, col_right = st.columns(2)

    with col_left:
        st.markdown(
            f'<p style="background-color:#FBFBFB;color:#FBFBFB;font-size:13px;border-radius:2%;text-align:center;"><strong>Mapa de Chutes</strong></p>',
            unsafe_allow_html=True,
        )
        st.altair_chart(
            sc.scatterplot_xg_outcome(match_id, team), use_container_width=True
        )

    with col_right:
        st.pyplot(sc.shots(match_id), use_container_width=True)

    st.dataframe(sc.goals(match_id), use_container_width=True)
    st.markdown('<hr style="border:2px solid #125d70">', unsafe_allow_html=True)


def players_on_off_target(match, team, world_cup):
    if world_cup == "Russia":
        match_id = games_2018_dict[match]
        year = 2018
    if world_cup == "Qatar":
        match_id = games_2022_dict[match]
        year = 2022

    col_left, col_right = st.columns(2)
    with col_left:
        st.markdown(
            f'<p style="background-color:#FBFBFB;color:black;font-size:23px;border-radius:2%;text-align:center;"><strong>Jogadores com mais Finalizações no Gol</strong></p>',
            unsafe_allow_html=True,
        )
        st.altair_chart(
            sc.players_with_more_shots_on_target(team, match_id, year),
            use_container_width=True,
        )

    with col_right:
        st.markdown(
            f'<p style="background-color:#FBFBFB;color:black;font-size:23px;border-radius:2%;text-align:center;"><strong>Jogadores com mais Finalizações Erradas</strong></p>',
            unsafe_allow_html=True,
        )
        st.altair_chart(
            sc.players_with_more_shots_off_target(team, match_id, year),
            use_container_width=True,
        )

    st.markdown('<hr style="border:2px solid #125d70">', unsafe_allow_html=True)


def shot_analysis(match, team, world_cup):
    if world_cup == "Russia":
        match_id = games_2018_dict[match]
    if world_cup == "Qatar":
        match_id = games_2022_dict[match]

    st.markdown(
        f'<p style="background-color:#FBFBFB;color:black;font-size:23px;border-radius:2%;text-align:center;"><strong>Área de Finalizações</strong></p>',
        unsafe_allow_html=True,
    )

    col_left, _ = st.columns(2)

    with col_left:
        choice = st.radio(
            "Escolha o Tempo para analise ",
            [
                "1˚ Tempo",
                "2˚ Tempo",
                "1˚ Tempo - Prorrogação",
                "2˚ Tempo - Prorrogação",
            ],
            horizontal=True,
        )

    if choice == ("1˚ Tempo"):
        period_pass_team_analysis = 1
    elif choice == ("2˚ Tempo"):
        period_pass_team_analysis = 2
    elif choice == ("1˚ Tempo - Prorrogação"):
        period_pass_team_analysis = 3
    # if choice == ('1˚ Tempo - Prorrogação'):
    else:
        period_pass_team_analysis = 4

    st.pyplot(
        sc.shot_analisys(match_id, team, period_pass_team_analysis),
        use_container_width=True,
    )
    st.markdown('<hr style="border:2px solid #125d70">', unsafe_allow_html=True)


# --------------Modelo-----------


def introduction_table_datamodel():
    texto = """

    As colunas abaixo fornecem informações importantes sobre as estatísticas de cada partida da seleção escolhida, incluindo os times envolvidos. Essas variáveis fornecem informações úteis para análise e estatísticas sobre as partidas de futebol, permitindo entender melhor o desempenho das equipes e dos jogadores em diferentes aspectos do jogo.

    ###### Colunas da Tabela

    1. **match_id**: É o identificador único para cada partida de futebol na base de dados.

    2. **world_cup**: Indica se o jogo faz parte da Copa do Mundo. Pode ter valores binários, como 0 para não fazer parte da Copa do Mundo e 1 para fazer parte.

    3. **team_name**: O nome da equipe que participou do jogo.

    4. **Total_goals**: O número total de gols marcados pela equipe na partida.

    5. **Ball Recovery**: A quantidade de vezes em que a equipe recuperou a posse de bola.

    6. **Carry**: Refere-se ao número de vezes em que um jogador carregou a bola, ou seja, manteve a posse dela enquanto avançava.

    7. **Clearance**: Representa o número de vezes em que a equipe afastou a bola de sua área de perigo, geralmente através de um chutão ou cabeceio.

    8. **Dribble**: O número de dribles realizados pela equipe durante a partida, que envolve um jogador superando um adversário enquanto mantém a posse de bola.

    9. **Duel**: Indica a quantidade de duelos disputados pela equipe. Um duelo é um confronto direto entre dois jogadores pela posse de bola.

    10. **Foul Committed**: O número de faltas cometidas pela equipe durante o jogo.

    11. **Foul Won**: O número de faltas sofridas pela equipe durante o jogo.

    12. **Interception**: A quantidade de interceptações feitas pela equipe, ou seja, quando um jogador intercepta um passe do time adversário.

    13. **Pass**: O número de passes realizados pela equipe durante a partida.

    14. **Shot**: O número de chutes a gol realizados pela equipe.

    15. **match**: Alguns detalhes específicos sobre a partida em si, como local, data, horário, etc.

    16. **Game_style**: Pode indicar o estilo de jogo da equipe, como ofensivo, moderado ou conservador.

    """

    st.markdown(texto)


def charts_model(team, world_cup):
    st.markdown(
        "<h1 style='text-align:center; font-size:35px'>Explorando a Identidade do Futebol: Classificação de Estilos de Jogo de Times</h1>",
        unsafe_allow_html=True,
    )
    st.markdown('<hr style="border:1px solid #125d70">', unsafe_allow_html=True)
    st.write(
        "Caso tenha interesse em saber sobre o desenvolvimento dos clusters aplicados selecione a box abaixo"
    )

    build_model = st.checkbox("Detalhes")
    if build_model:
        st.write(
            "Abaixo foi realizado um tratatamento para juntar todos os dados que seriam necessários para aplicação dos estudos"
        )
        code_01 = """data_model = data_events.loc[ (data_events.position_name.notnull())
                        & (data_events.position_name != 'Substitute')
                        & (data_events.position_name != 'Goalkeeper')
                        & ((data_events.type_name == 'Carry')
                        | (data_events.type_name == 'Pass')
                        | (data_events.type_name == 'Ball Recovery')
                        | (data_events.type_name == 'Dribble')
                        | (data_events.type_name == 'Duel')
                        | (data_events.type_name == 'Shot')
                        | (data_events.type_name == 'Clearance')
                        | (data_events.type_name == 'Interception')
                        | (data_events.type_name == 'Foul Committed')
                        | (data_events.type_name == 'Foul Won')), ['match_id', 'team_name', 'position_name', 'type_name']]

        data_goals =  data_events.loc[ (data_events['shot_outcome_name'] == 'Goal') 
                                &(data_events['period'] != 5)  , ['match_id','team_name', 'shot_outcome_name'] ]

        grouped_goals = data_goals.groupby(['match_id', 'team_name']).size().reset_index(name='total_goals')
        stats_matches = data_model.groupby(['match_id', 'team_name', 'type_name']).size().unstack('type_name', fill_value=0).reset_index()

        data_model = pd.merge(grouped_goals, stats_matches, on=['match_id', 'team_name'], how='right')
        data_model['total_goals'] = (data_model['total_goals'].fillna(0)).astype('int')"""
        st.code(code_01, language="python")
        st.write(
            "Em seguida foi realizado um plot para entender o comportamento das variáveis entre elas"
        )
        pairplot = st.checkbox("Pairplot com todas variáveis")
        if pairplot:
            st.image("Images/pairplot.png", width=2500)
        else:
            print("")

        code_02 = """ 
                data_cluster = data_model[['Ball Recovery', 'Carry','Clearance', 'Dribble', 'Duel', 'Interception', 'Pass', 'Shot', 'Foul Won', 'Foul Committed','total_goals']]

                model = AgglomerativeClustering(metric = 'euclidean', linkage = 'ward')
                visualizer = KElbowVisualizer(model, k=(1,10), timings = False)
                visualizer.fit(data_cluster)
                visualizer.show()

                """
        st.write(
            "Abaixo foi realizado um teste para identificar o número de clusters ideias de acordo com nossos dados, para isso foi utilizado a biblioteca KElbowVisualizer e a ténica utilizada para realizar os cluters foi o AgglomerativeClustering"
        )
        st.code(code_02, language="python")
        _, col_model_01, _ = st.columns(3)
        with col_model_01:
            st.image("Images/kelbow.png", use_column_width=True)

        st.write(
            "Em seguida foi utilizada a visuzalição por meio do dendrograma, que é uma representação gráfica de uma estrutura hierárquica de agrupamento (clustering). Ele é amplamente utilizado em análise de dados para visualizar a semelhança ou dissimilaridade entre objetos ou grupos de objetos."
        )
        _, col_model_02, _, _ = st.columns(4)
        with col_model_02:
            st.image("Images/dendograma.png", width=1000)

        st.write(
            "No código demonstrado a seguir mostra a implementação dos cluster com a quantidade indicada pelo método K-elbow e pelo dendrograma, que no caso foram 3 classes"
        )
        code_03 = """
                model_agglomerative_cluster = AgglomerativeClustering(n_clusters = visualizer.elbow_value_, metric = 'euclidean', linkage = 'ward')
                y_model = model_agglomerative_cluster.fit_predict(data_cluster)
                data_model['Labels'] = y_model
            """
        st.code(code_03, language="python")
        _, col_model_03, _, _ = st.columns(4)
        with col_model_03:
            st.image(
                "Images/comparacao.png",
                width=1000,
                caption='Exemplo abaixo do cluster nas correlação das variáveis "Dribble" e "Carry" ',
            )

        text_game_style = """
        
                            Através de uma análise dos cluters geradoas foi identificado padrões de estilos de jogo através das estatísticas das partidas, sendo:

                            0. **Ofensivo**: Seleções caracterizadas por uma média de 685 passes por jogo, média de 16 finalizações por jogo, seleções que possuem menos Cleareances na partida, seleções que recuperam mais a bola e que possuem média de 1.5 gols por jogo. 
                            1. **Moderado**: Seleções caracterizadas por uma média de 482 passes por jogo, média de 12 finalizações por jogo, seleções que possuem mais Duelos em média na partida, ou seja, são equipes que mais tiveram picos entre ataque e defesa.
                            2. **Conservador**: Seleções caracterizadas por uma média de 314 passes por jogo, média de 9 finalizações por partida, seleções que recuperam menos bolas, seleções que fazem menos progressões, ou seja, equipes que deixam o adversário jogar mais na posse de bola e que jogam de forma mais defensiva.

                            Cada característica atribuída a uma seleção é referente as partidas individuais, levando em consideração todos as estatísticas de jogos das Copas do Mundo FIFA 2018 e 2022.
                 
                        """
        st.markdown(text_game_style)
        col_model_04, col_model_05, col_model_06 = st.columns(3)
        with col_model_04:
            st.image(
                "Images/conservador.png",
                use_column_width=True,
                caption="Estilo de jogo Conservador",
            )
        with col_model_05:
            st.image(
                "Images/moderado.png",
                use_column_width=True,
                caption="Estilo de jogo Moderado",
            )
        with col_model_06:
            st.image(
                "Images/ofensivo.png",
                use_column_width=True,
                caption="Estilo de jogo Ofensivo",
            )
    else:
        print("")

    st.markdown('<hr style="border:1px solid #125d70">', unsafe_allow_html=True)

    parameters = [
        "total_goals",
        "Ball Recovery",
        "Carry",
        "Clearance",
        "Dribble",
        "Duel",
        "Foul Committed",
        "Foul Won",
        "Interception",
        "Pass",
        "Shot",
    ]

    st.markdown(
        f'<p style="background-color:#FBFBFB;color:black;font-size:23px;border-radius:2%;text-align:center;"><strong>Estatísticas da Partidas</strong></p>',
        unsafe_allow_html=True,
    )
    columns = st.checkbox("Descrição das Colunas")

    if columns:
        introduction_table_datamodel()
    else:
        print("")

    st.dataframe(sc.team_compare(team, world_cup), use_container_width=True)
    st.markdown('<hr style="border:1px solid #125d70">', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(
            f'<p style="background-color:#FBFBFB;color:black;font-size:23px;border-radius:2%;text-align:center;"><strong>Estilos de Jogo Utilizados</strong></p>',
            unsafe_allow_html=True,
        )
        st.markdown(
            f'<p style="background-color:#FBFBFB;color:#FBFBFB;font-size:10px;border-radius:2%;text-align:center;"><strong>Estilos de Jogo Utilizados</strong></p>',
            unsafe_allow_html=True,
        )
        st.altair_chart(
            sc.game_style_barchart(team, world_cup), use_container_width=True
        )
    with col2:
        st.markdown(
            f'<p style="background-color:#FBFBFB;color:black;font-size:23px;border-radius:2%;text-align:center;"><strong>Estilos de Jogo Utilizados por Outras Seleções</strong></p>',
            unsafe_allow_html=True,
        )
        game_style_list = st.selectbox(
            "Selecione um estilo de jogo", ["Conservador", "Moderado", "Ofensivo"]
        )
        st.dataframe(
            sc.game_style_teams(game_style_list, world_cup), use_container_width=True
        )

    st.markdown('<hr style="border:1px solid #125d70">', unsafe_allow_html=True)

    st.markdown(
        f'<p style="background-color:#FBFBFB;color:black;font-size:23px;border-radius:2%;text-align:center;"><strong>Análise de Jogos e Estatísticas</strong></p>',
        unsafe_allow_html=True,
    )
    


    col_model_07, col_model_08 = st.columns(2)
    with col_model_07:
        country_selectbox = st.selectbox(
            "Selecione a edição que deseja analisar",
            ["FIFA World Cup 2018 - Russia", "FIFA World Cup 2022 - Qatar"],
        )
    if country_selectbox == "FIFA World Cup 2018 - Russia":
        teams_list = teams_list_2018
        country_chosen = "Russia"
    else:
        teams_list = teams_list_2022
        country_chosen = "Qatar"

    with col_model_08:
        other_team = st.selectbox("Selecione um time para comparar", teams_list)

    st.dataframe(sc.team_compare(other_team, country_chosen), use_container_width=True)

    st.markdown('<hr style="border:1px solid #125d70">', unsafe_allow_html=True)

    col3, col4 = st.columns(2)
    list_matches_main_team = list(sc.team_compare(team, world_cup)["match"])
    list_matches_other = list(sc.team_compare(other_team, country_chosen)["match"])

    with col3:
        st.markdown(
            f'<p style="background-color:#FBFBFB;color:black;font-size:23px;border-radius:2%;text-align:center;"><strong>1˚ Seleção para Análise</strong></p>',
            unsafe_allow_html=True,
        )
        st.write(
            "Selecione abaixo a partida da seleção para análise das estatísticas e estilo de jogo"
        )
        match_team_1 = st.selectbox(
            "Selecione a partida da 1˚ Seleção", list_matches_main_team
        )

        team_1, parameters_team_1, id_team_1 = sc.get_parameters_team_1(
            team, match_team_1, world_cup
        )
    with col4:
        st.markdown(
            f'<p style="background-color:#FBFBFB;color:black;font-size:23px;border-radius:2%;text-align:center;"><strong>2˚ Seleção para Análise</strong></p>',
            unsafe_allow_html=True,
        )
        st.write(
            "Selecione abaixo a partida da seleção para análise das estatísticas e estilo de jogo"
        )
        match_team_2 = st.selectbox(
            "Selecione a partida da 2˚ Seleção", list_matches_other
        )
        team_2, parameters_team_2, id_team_2 = sc.get_parameters_team_1(
            other_team, match_team_2, country_chosen
        )

    columns = st.checkbox('Detalhes sobre as estatísticas')   
    if columns:
        text_columns = """
    
                        Através de uma análise dos cluters geradoas foi identificado padrões de estilos de jogo através das estatísticas das partidas, sendo:

                        0. **Total_goals**: Número total de gols marcados pela equipe.
                        1. **Ball Recovery**: Quantidade de recuperações de bola realizadas pela equipe.
                        2. **Carry**: Número de vezes que a equipe conduziu a bola em sua posse.
                        3. **Clearance**: Quantidade de vezes que a equipe realizou um afastamento da bola para longe da sua área.
                        3. **Dribble**: Número de dribles realizados pela equipe.
                        3. **Duel**: Número de dribles realizados pela equipe.
                        3. **Foul Committed**: Número de faltas cometidas pela equipe.
                        3. **Foul Won**:  Número de faltas sofridas pela equipe.
                        3. **Interception**:  Quantidade de interceptações realizadas pela equipe.
                        3. **Pass**: Número de passes completados pela equipe.
                        3. **Shot**: Quantidade de chutes realizados pela equipe.
                        Cada característica atribuída a uma seleção é referente as partidas individuais, levando em consideração todos as estatísticas de jogos das Copas do Mundo FIFA 2018 e 2022.
                
                    """
        
        st.markdown(text_columns)

    _, col5, _ = st.columns(3)
    with col5:
        st.pyplot(
            sc.radar_chart(
                team_1, id_team_1, world_cup, team_2, id_team_2, country_chosen
            ),
            use_container_width=True,
        )


def main():
    page_configs()
    topic = [
        "Overview do Projeto",
        "Análise Geral da Seleção",
        "Análise de Finalização",
        "Análise da Troca de Passes",
        "Análise de Estilo de Jogo",
    ]
    st.sidebar.title("Menu Principal")
    chosen_content = st.sidebar.selectbox("Selecione um tema", topic)
    st.sidebar.markdown('<hr style="border:1px solid #125d70">', unsafe_allow_html=True)

    st.sidebar.title("Filtros")

    world_cup = st.sidebar.selectbox(
        "Escolha qual Copa do Mundo você deseja analisar",
        options=["FIFA World Cup 2018 - Russia", "FIFA World Cup 2022 - Qatar"],
    )

    if world_cup == "FIFA World Cup 2018 - Russia":
        world_cup = "Russia"
        teams_list = teams_list_2018
    else:
        world_cup = "Qatar"
        teams_list = teams_list_2022

    team = st.sidebar.selectbox("Escolha uma seleção para analisar", options=teams_list)

    match = st.sidebar.selectbox(
        "Escolha o jogo que queira analisar", options=sc.return_matches(team, world_cup)
    )

    st.sidebar.markdown('<hr style="border:1px solid #125d70">', unsafe_allow_html=True)

    st.sidebar.markdown("#### Contact")
    st.sidebar.markdown("https://www.linkedin.com/in/gabrieljnc/")

    if chosen_content == "Overview do Projeto":
        overview()

    elif chosen_content == "Análise Geral da Seleção":
        st.markdown(
            "<h1 style='text-align:center; font-size:35px'>Análise Estatística do Futebol: Uma Visão Geral das Seleções na Copa do Mundo</h1>",
            unsafe_allow_html=True,
        )
        st.markdown('<hr style="border:2px solid #125d70">', unsafe_allow_html=True)
        panel_geral = st.checkbox("Informações sobre o painel")
        if panel_geral:
            st.markdown("##### Objetivo:")
            st.write(
                "Nesse painel tem como objetivo principal oferecer uma análise estatística abrangente sobre uma seleção de futebol específica. O painel fornece informações relevantes sobre a seleção, incluindo estatísticas gerais como o número total de jogos disputados, vitórias, derrotas e empates. Além disso, é possível visualizar a movimentação dos jogadores durante as partidas da seleção selecionada. Essa funcionalidade permite acompanhar de forma dinâmica e interativa o desempenho dos jogadores em campo, fornecendo uma visão mais detalhada da atuação da equipe. O dashboard oferece uma visão completa e informativa sobre a performance da seleção, fornecendo aos usuários insights valiosos para análise e tomada de decisões relacionadas ao desempenho da equipe"
            )
        else:
            print("")

        flag_main_team(team)
        introduction_text()
        st.dataframe(sc.get_team_games(team, world_cup), use_container_width=True)
        cards_with_informations(team, world_cup)
        top_playes_bar_chart(team, world_cup)
        players_and_heatmap(team, world_cup, match)

    elif chosen_content == "Análise de Finalização":
        st.markdown(
            "<h1 style='text-align:center; font-size:35px'>Alvo Certo: Explorando as Estatísticas de Finalização</h1>",
            unsafe_allow_html=True,
        )
        st.markdown('<hr style="border:2px solid #125d70">', unsafe_allow_html=True)
        panel_shots = st.checkbox("Informações sobre o painel")
        if panel_shots:
            st.markdown("##### Objetivo:")
            text_shots = """
                        O painel possui como objetivo oferecer uma análise detalhada e visualização completa das finalizações em jogadas de uma equipe. Essa análise é de extrema importância para a equipe técnica, pois fornece insights valiosos sobre o desempenho da equipe em relação à finalização das jogadas, podendo influenciar diretamente nas decisões tomadas pela comissão técnica.
            
                        O painel do dashboard apresenta informações relevantes, como a direção dos chutes, os locais onde as finalizações ocorreram e o total de finalizações por partida, entre outros dados relevantes. Essas informações permitem uma análise aprofundada do desempenho da equipe na hora de finalizar as jogadas, fornecendo uma visão clara e precisa sobre a eficiência e a precisão dos chutes realizados.

                        Essa análise detalhada das finalizações auxilia a equipe técnica na identificação de padrões, pontos fortes e áreas a serem aprimoradas. Com base nessas informações, a comissão técnica pode tomar decisões mais embasadas sobre estratégias táticas, treinamentos específicos e ajustes necessários para melhorar o desempenho da equipe nas finalizações. O dashboard proporciona uma visão completa e de fácil interpretação sobre as estatísticas das finalizações, contribuindo para a melhoria contínua da equipe e o alcance de melhores resultados.
                        """
            st.markdown(text_shots)
        else:
            print("")
        flag_matches(match)
        cards_with_shots_information(world_cup, team, match)
        line_chart_and_player_more_shots(match, team, world_cup)
        scatterplot_line_xg_and_shots(match, team, world_cup)
        players_on_off_target(match, team, world_cup)
        kde_shots_and_jointgrid(match, world_cup)
        shot_analysis(match, team, world_cup)

    elif chosen_content == "Análise da Troca de Passes":
        st.markdown(
            "<h1 style='text-align:center; font-size:35px'>Desvendando a Estatística por trás da Troca de Passes</h1>",
            unsafe_allow_html=True,
        )
        st.markdown('<hr style="border:2px solid #125d70">', unsafe_allow_html=True)
        panel_pass = st.checkbox("Informações sobre o painel")
        if panel_pass:
            st.markdown("##### Objetivo:")
            text_shots = """
                        O painel tem como principal objetivo mostrar os recursos de análise de troca de passes de uma equipe. Nessa seção específica, são disponibilizadas visualizações que destacam os padrões de passes entre os jogadores. Utilizam-se gráficos de rede ou diagramas de fluxo para ilustrar a quantidade, direção e precisão dos passes realizados.

                        Essas visualizações permitem que técnicos e analistas identifiquem padrões de jogo, áreas de oportunidade e pontos fortes da equipe. Com base nessas informações, eles podem ajustar estratégias, treinamentos e táticas para aprimorar o desempenho geral.

                        A análise exploratória e modelagem dos dados fornecem insights valiosos para a compreensão do fluxo de passes durante as partidas. Os gráficos de rede destacam as conexões entre os jogadores, permitindo uma visualização clara das dinâmicas e dos relacionamentos no campo. Além disso, a precisão dos passes pode ser analisada, ajudando a identificar pontos a serem aprimorados ou consolidar áreas de força.

                        Essas informações são fundamentais para os treinadores e analistas tomarem decisões informadas e embasadas. Ao ajustar suas estratégias e táticas com base nas análises dos padrões de passes, eles podem melhorar a fluidez do jogo, identificar jogadores-chave e maximizar as oportunidades de criação de jogadas.
                        """
            st.markdown(text_shots)
        else:
            print("")
        flag_matches(match)
        cards_with_pass_information(world_cup, team, match)
        line_chart_and_player_more_passes(match, team, world_cup)
        pass_analysis(match, team, world_cup)
        arrow_passes_and_pass_lead_shot(match, team, world_cup)
        passes_per_minute(match, world_cup)
        ball_passer_receiver_and_pass_network(team, match, world_cup)
        convex_hull_passes_and_heatmap_of_passes(match, team, world_cup)

    elif chosen_content == "Análise de Estilo de Jogo":
        charts_model(team, world_cup)


if __name__ == "__main__":
    main()
