import streamlit as st
import pandas as pd
import pydeck as pdk



st.title('PyLadies Carevan Streamlitハンズオン！')
st.text('markdown記法についてはこのリンクを参照してください')

st.markdown('### これはMarkdownです')
st.markdown('- チェックリストや **ボールド文字** なども使えます')

df = pd.DataFrame({
    'A列': [1, 2, 3, 4],
    'B列': [10, 20, 40, 30],
    'C列': [400, 100, 200, 300],
})

# st.writeを使ったDataFrameの表示
st.write(df)

# st.dataframeを使ったDataFrameの表示 (列の最大値をハイライトし、表示サイズを指定しています)
st.dataframe(df.style.highlight_max(axis=0), width=500, height=200)

st.subheader("PyLadies Tokyo 参加者推移")

data = [
    [15,22,5],
    [5,15,12],
    [41,40,21],
    [19,13,0],
    [23,27,0],
    [17,21,7],
    [28,8,8],
    [6,8,13],
    [7,10,20],
    [35,20,18],
    [13,9,8],
    [21,4,32],
]

months = ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月']
chart_data = pd.DataFrame(
    data,
    columns=['2015', '2020', '2023'],
    index=pd.CategoricalIndex(months, categories=months, ordered=True)
)

st.line_chart(chart_data)
st.area_chart(chart_data)
st.bar_chart(chart_data)

st.image('alien.png', caption='キュイーン', use_container_width=True)

name = st.text_input('名前を入力してください')
st.write('名前:', name)

agree = st.checkbox('画像を表示しますか？')
if agree:
    st.image('alien.png', caption='キュイーン', use_container_width=False)


options = st.multiselect(
    'あなたの好きな色を選んでください',
    options=['青', '黄色', '赤', 'ピンク', '金色'],
    default=['青'],
)
st.write('好きな色:', options)

history = st.slider("Python歴は?", 0, 33, 3)
st.write("私のPython歴は ", history, "です")

st.sidebar.markdown('[google](https://google.com)')

picture = st.camera_input("撮影!")
if picture:
    st.image(picture)

uploaded_file = st.file_uploader('画像を選択してください', type=['jpg','png'])
if uploaded_file is not None:
    st.image(uploaded_file)

uploaded_csv_file = st.file_uploader('csvファイルを選択してください', type=['csv'])
if uploaded_csv_file is not None:
    csv_df = pd.read_csv(uploaded_csv_file)
    st.write(csv_df)



mg_df = None
marine_garbage_csv_file = st.file_uploader('ごみ量とその海岸のデータが入ったcsvファイルを選択してください', type=['csv'])

if marine_garbage_csv_file is not None:
    # CSVファイルをデータフレームに読み込む
    mg_df = pd.read_csv(marine_garbage_csv_file)

    # (この後出てくるコードはすべてこのif文の中に書いてください)

    # 海岸と季節が一致するレコードの体積を集計
    coast_season_amount = mg_df.groupby(['海岸','緯度','経度','季節'])['体積L'].sum().reset_index()
    st.write('海岸ごとの季節別ごみ量')
    st.write(coast_season_amount)

    # 初期の地図の表示設定(広島県の中心付近)
    view_state = pdk.ViewState(
        latitude=34.3963,
        longitude=132.4596, 
        zoom=8,
        pitch=50,
    )

    # タブ切り替えのUI作成
    spring, summer, autumn, winter = st.tabs(['春', '夏', '秋', '冬'])

    with spring:
        # Pydeckを利用したヒートマップレイヤーの作成
        layer = pdk.Layer(
            "HeatmapLayer",
            coast_season_amount[coast_season_amount['季節'] == '春'],
            get_position='[経度, 緯度]',
            get_weight='体積L',
            radiusPixels=40,  # ヒートマップの半径
        )

        # 地図の表示
        st.pydeck_chart(pdk.Deck(layers=[layer], initial_view_state=view_state))
    
    with summer:
        # Pydeckを利用したヒートマップレイヤーの作成
        layer = pdk.Layer(
            "HeatmapLayer",
            coast_season_amount[coast_season_amount['季節'] == '夏'],
            get_position='[経度, 緯度]',
            get_weight='体積L',
            radiusPixels=40,  # ヒートマップの半径
        )

        # 地図の表示
        st.pydeck_chart(pdk.Deck(layers=[layer], initial_view_state=view_state))
    
    with autumn:
        # Pydeckを利用したヒートマップレイヤーの作成
        layer = pdk.Layer(
            "HeatmapLayer",
            coast_season_amount[coast_season_amount['季節'] == '秋'],
            get_position='[経度, 緯度]',
            get_weight='体積L',
            radiusPixels=40,  # ヒートマップの半径
        )

        # 地図の表示
        st.pydeck_chart(pdk.Deck(layers=[layer], initial_view_state=view_state))

    with winter:
        # Pydeckを利用したヒートマップレイヤーの作成
        layer = pdk.Layer(
            "HeatmapLayer",
            coast_season_amount[coast_season_amount['季節'] == '冬'],
            get_position='[経度, 緯度]',
            get_weight='体積L',
            radiusPixels=40,  # ヒートマップの半径
        )

        # 地図の表示
        st.pydeck_chart(pdk.Deck(layers=[layer], initial_view_state=view_state))


# この画像が表示されたタイミングでおめでとうmotionをする
completed = st.checkbox('ハンズオン終わった？')
if completed:
    st.image('greatwork.png', use_container_width=False)
    st.balloons()