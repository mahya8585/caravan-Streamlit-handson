import streamlit as st

st.title('PyLadies Carevan Streamlit Hands-On')

'''
## まずはじめに
とりあえず有無を言わさずStreamlitをインストールしましょう    
pip install streamlit

色々なファイルが入ってくるので少し待つことにします。その間にStreamlitについて簡単に説明します
'''

'''
## Streamlitとは

[https://streamlit.io/](https://streamlit.io/)

Pythonで作成されたオープンソースのWebフレームワークです
Webアプリに必要なフロントエンドの知識(HTML,CSS, JavaScript)を必要としません
データの可視化やWebアプリケーションの作成に使用されます
素早くアプリを作って公開することができます

#### とにもかくにもまずStreamlitを動かしてみよう
コマンドプロンプト(Windows) or ターミナル(Mac)で以下のコマンドを実行してください
> streamlit hello

ブラウザが立ち上がり、Streamlitのサンプルアプリが表示されますね。簡単でよく使う機能やコンポーネントが紹介されています。今後使い方に困ったときなどはこのサンプルアプリを参考にするとよいでしょう
'''

st.image('streamlit-hello.png', caption='Streamlit hello サンプル画像', use_container_width=True)

'''
#### Streamlit API リファレンス
このリンクからStreamlitのAPIリファレンスを参照することができます。細かい記法や利用についてはこちらを参照してください
[https://docs.streamlit.io/develop/api-reference](https://docs.streamlit.io/develop/api-reference)

'''

'''
## Streamlitの基本的な使い方

#### Streamlit の起動コマンド

> streamlit run ファイル名.py

streamlitは起動完了後、ファイルを更新したらF5を押すことでリアルタイムに更新されます。また、停止する場合はCtrl + Cを押してください

**caravan.py** というファイルを作成して下記のコードを記述しましょう。その後、streamlitを起動し、次の工程にすすみましょう
```python
import streamlit as st
import pandas as pd
```
'''

'''
#### 1. テキスト表示
Streamlitではテキストを表示するために **st.text()** や **st.markdown()** を使用します    
[Markdown記法についてはこちら](https://support-ja.backlog.com/hc/ja/articles/360036145833-%E3%83%86%E3%82%AD%E3%82%B9%E3%83%88%E6%95%B4%E5%BD%A2%E3%81%AE%E3%83%AB%E3%83%BC%E3%83%AB-Markdown-%E8%A8%98%E6%B3%95)

```python
st.title('PyLadies Carevan Streamlitハンズオン！')
st.text('markdown記法についてはこのリンクを参照してください')

st.markdown('### これはMarkdownです')
st.markdown('- チェックリストや **ボールド文字** なども使えます')
```

'''

'''
#### 2. データの表示
データの取り扱いにはpandasと呼ばれるライブラリをよく利用します。pandasはデータ解析を行うためのライブラリで、データを表形式で扱うことができます。
```python
df = pd.DataFrame({
    'A列': [1, 2, 3, 4],
    'B列': [10, 20, 40, 30],
    'C列': [400, 100, 200, 300],
})
```

```python
# st.writeを使ったDataFrameの表示
st.write(df)

# st.dataframeを使ったDataFrameの表示 (列の最大値をハイライトし、表示サイズを指定しています)
st.dataframe(df.style.highlight_max(axis=0), width=500, height=200)
```

データをグラフとして表示することも、streamlitでは簡単にできます。
```python
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
```

```python
st.line_chart(chart_data)
st.area_chart(chart_data)
st.bar_chart(chart_data)
```

'''


'''
#### 3. その他webシステムでよく使うアイテム群
- 画像表示    
画像を表示するために **st.image()** を使用します
```python
st.image('alien.png', caption='キュイーン', use_container_width=True)
```

- テキスト入力    
```python
name = st.text_input('名前を入力してください')
st.write('名前:', name)
```

- チェックボックス    
Streamlitではチェックボックスを作成するために **st.checkbox()** を使用します。 チェックボックスはTrue/Falseの値を返します。
またStreamlitではif文を使って処理の条件分岐を行うことができます。下記の例ではチェックボックスがTrueの場合に画像を表示します。
```python
agree = st.checkbox('画像を表示しますか？')
if agree:
    st.image('alien.png', caption='キュイーン', use_container_width=False)
```

- マルチセレクトボックス    
マルチセレクトボックスは複数の選択肢から複数の選択を行うことができます。 **st.multiselect()** を使用します。
今までの表示のみの設定と異なり、事前に選択肢をリストで指定する必要があります。
```python
options = st.multiselect(
    'あなたの好きな色を選んでください',
    options=['青', '黄色', '赤', 'ピンク', '金色'],
    default=['青'],
)
st.write('好きな色:', options)
```

- スライダー    
```python
history = st.slider("Python歴は?", 0, 33, 3)
st.write("私のPython歴は ", history, "です")
```

- サイドバー    
サイドバーを作成するために **st.sidebar** を使用します。
サイドバーにはテキストや、テキスト入力などを表示することができます。
```python
st.sidebar.markdown('[google](https://google.com)')
```

- カメラ    
カメラを起動させて画像撮影もできます。 **st.camera_input()** を使用します。
この例では、カメラで撮影をしたら(trueが返ってきたら) その画像を表示するようにしています。
```python
picture = st.camera_input("撮影!")
if picture:
    st.image(picture)
```

- ファイルアップロード    
ファイルをアップロードするために **st.file_uploader()** を使用します。
アップロードできるファイルの種類を指定することもできます。
この例では、jpgもしくはpngファイルのみをアップロードできるように制限し、アップロードされた画像を表示するようにしています。
```python
uploaded_file = st.file_uploader('画像を選択してください', type=['jpg','png'])
if uploaded_file is not None:
    st.image(uploaded_file)
```
csvファイルをアップロードして表示させることも簡単にできます。
この例では、csvファイルをアップロードしてCSVファイルが空でなければ、その内容を表示するようにしています。
```python
uploaded_csv_file = st.file_uploader('csvファイルを選択してください', type=['csv'])
if uploaded_csv_file is not None:
    csv_df = pd.read_csv(uploaded_csv_file)
    st.write(csv_df)
```
'''


'''
## 海岸のごみ量の可視化に挑戦
ここでは下記の技術を使って、海岸ごとのごみ量を地図上に可視化してみたいと思います

- 緯度経度情報及びごみ量のdataframe化
- 地図表示
- ヒートマップの作成

### 緯度経度データの取り込み
ひとつ前のセクションで紹介した **st.file_uploader()** を使って、緯度経度情報及びごみ量のデータをアップロードしてみましょう

```python
mg_df = None
marine_garbage_csv_file = st.file_uploader('ごみ量とその海岸のデータが入ったcsvファイルを選択してください', type=['csv'])

if marine_garbage_csv_file is not None:
    # CSVファイルをデータフレームに読み込む
    mg_df = pd.read_csv(marine_garbage_csv_file)

    # (この後出てくるコードはすべてこのif文の中に書いてください)
```

### 海岸と季節が一致するレコードの体積を集計
グラフ表示の項目で記述したように、pandasを使って緯度経度情報及びごみ量のデータをdataframe化します。今回はヒートマップを作成したいので、季節ごとの海岸のごみ体積を集計したデータを利用してみることにします。

```python
# 海岸と季節が一致するレコードの体積を集計
    coast_season_amount = mg_df.groupby(['海岸','緯度','経度','季節'])['体積L'].sum().reset_index()
    st.write('海岸ごとの季節別ごみ量')
    st.write(coast_season_amount)
```

### 地図表示
地図表示およびデータマッピングを行うために、pydeckというライブラリを使用します。pydeckはDeck.glのPythonバインディングであり、大規模な地理空間データの視覚化に適しています。基本的にstreamlitをインストールしていれば一緒にインストールされているライブラリですが、インストール出来てない場合は以下のコマンドでインストールしてください。

```bash
pip install pydeck
```


では、実際にpydeckを使って地図を表示してみましょう。

```python
import pydeck as pdk
```

```python
# 初期の地図の表示設定(広島県の中心付近)
    view_state = pdk.ViewState(
        latitude=34.3963,
        longitude=132.4596, 
        zoom=8,
        pitch=50,
    )
```

```python
# Pydeckを利用したヒートマップレイヤーの作成
    layer = pdk.Layer(
        "HeatmapLayer",
        coast_season_amount[coast_season_amount['季節'] == '春'],
        get_position='[経度, 緯度]',
        get_weight='体積L',
        radiusPixels=40,  # ヒートマップの半径
    )
```

```python
# 地図の表示
    st.pydeck_chart(pdk.Deck(layers=[layer], initial_view_state=view_state))
```

どうですか？地図が表示されましたか？まだ一つの季節しか表示していないので、次のセクションで季節ごとのヒートマップを作成してみましょう

これから春以外の季節のヒートマップも作成しますが、縦に4つ地図が並ぶと見づらいので、タブで切り替えられるようにしてみましょう。

次のコードをヒートマップLayerの設定コード(layer = pdk.Layer)の上部に記載してください。

```python
# タブ切り替えのUI作成
    spring, summer, autumn, winter = st.tabs(['春', '夏', '秋', '冬'])

    with spring:
        # (ここより下のコードはすべてインデントを一つ下げてください)
```

いかがですか？地図の上部に春夏秋冬のタブが表示されましたね。併せて春のタブでヒートマップが表示されていると思います。
では、続いて夏、秋、冬のタブにそれぞれのヒートマップを表示させてみましょう。
・・・もうお分かりですね。**with** 文を使ってタブを切り替え、その中にヒートマップのLayer設定と地図表示のコードを記載します。
**頑張って自力で作成してみましょう！**
'''


'''
## 自分をほめる
great work!!!! 海ゴミデータのヒートマップを表示できましたね！せっかくなので自分をほめてあげましょう :tada::tada::tada: 

```python
# この画像が表示されたタイミングでおめでとうmotionをする
completed = st.checkbox('ハンズオン終わった？')
if completed:
    st.image('greatwork.png', use_container_width=False)
    st.balloons()
```

'''

'''
## アプリの公開
Streamlitを使って作成したアプリは、HerokuやStreamlit Sharingなどを使って公開することができます。
ここではStreamlit SharingとGitHubを利用した簡単公開を紹介します。
1. [Streamlit公式ページ](https://streamlit.io/) 右上の `Sign up` で Streamlit Community Cloud のアカウトを作成
2. GitHubと連携
![GitHubと連携](https://streamlit-yolo-hands-on.readthedocs.io/ja/latest/_images/streamlit_deploy1.png)
3. `create app` から、必要な項目を入力して Deploy! ボタンをクリックするだけ
![Deploy](https://streamlit-yolo-hands-on.readthedocs.io/ja/latest/_images/streamlit_deploy2.png)
'''

'''
## お疲れさまでした！
これでStreamlitの基本的な使い方を学びました。これを参考にして、自分のアプリを作ってみましょう！
Happy Streamlit coding! :sunglasses: :heart: :computer:
'''

'''
### appendix
本セッションで利用したドキュメントは下記にデプロイしています。    
https://caravan-app-handson-hiroshima.streamlit.app/
'''

