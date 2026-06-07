import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="IPL Data Storytelling",
    page_icon="📖",
    layout="wide"
)

# Load Dataset
@st.cache_data
def load_data():
    df = pd.read_csv("IPL_Matches_2008_2022.csv")
    df.columns = df.columns.str.lower()
    return df

df = load_data()

# ----------------------------------
# TITLE
# ----------------------------------

st.title("📖 IPL Data Storytelling (2008 - 2022)")

st.markdown("""
This story explores the evolution of the Indian Premier League (IPL)
from 2008 to 2022 using match-level data.
""")

# ----------------------------------
# DATASET INTRODUCTION
# ----------------------------------

st.header("1️⃣ Dataset Introduction")

st.write("""
The dataset contains IPL matches played from 2008 to 2022.

Key attributes include:

- Teams
- Cities
- Venues
- Toss Results
- Winning Teams
- Player of the Match
""")

st.dataframe(df.head())

# ----------------------------------
# EDA
# ----------------------------------

st.header("2️⃣ Exploratory Data Analysis")

col1, col2, col3 = st.columns(3)

col1.metric("Total Matches", len(df))

col2.metric(
    "Teams",
    pd.concat([df["team1"], df["team2"]]).nunique()
)

col3.metric(
    "Cities",
    df["city"].nunique()
)

# ----------------------------------
# STORY 1
# ----------------------------------

st.header("3️⃣ Story 1: IPL Growth Over Time")

matches = (
    df.groupby("season")
    .size()
    .reset_index(name="matches")
)

fig1 = px.line(
    matches,
    x="season",
    y="matches",
    markers=True,
    title="Matches Played Each Season"
)

st.plotly_chart(fig1, use_container_width=True)

st.success("""
Insight:
IPL has consistently expanded over the years,
with more teams and matches introduced.
""")

# ----------------------------------
# STORY 2
# ----------------------------------

st.header("4️⃣ Story 2: Most Successful Teams")

wins = (
    df["winningteam"]
    .value_counts()
    .reset_index()
)

wins.columns = ["Team", "Wins"]

fig2 = px.bar(
    wins.head(10),
    x="Team",
    y="Wins",
    title="Top Winning Teams"
)

st.plotly_chart(fig2, use_container_width=True)

top_team = wins.iloc[0]["Team"]

st.success(
    f"Insight: {top_team} is the most successful IPL team."
)

# ----------------------------------
# STORY 3
# ----------------------------------

st.header("5️⃣ Story 3: Toss Strategy")

fig3 = px.pie(
    df,
    names="tossdecision",
    title="Bat vs Field Decision"
)

st.plotly_chart(fig3, use_container_width=True)

st.success("""
Insight:
Teams prefer chasing in many IPL matches,
which explains the higher frequency of choosing field first.
""")

# ----------------------------------
# STORY 4
# ----------------------------------

st.header("6️⃣ Story 4: Star Performers")

pom = (
    df["player_of_match"]
    .value_counts()
    .reset_index()
)

pom.columns = ["Player", "Awards"]

fig4 = px.bar(
    pom.head(10),
    x="Player",
    y="Awards",
    title="Most Player of the Match Awards"
)

st.plotly_chart(fig4, use_container_width=True)

best_player = pom.iloc[0]["Player"]

st.success(
    f"Insight: {best_player} dominated Player of the Match awards."
)

# ----------------------------------
# STORY 5
# ----------------------------------

st.header("7️⃣ Story 5: IPL Cities")

cities = (
    df["city"]
    .value_counts()
    .reset_index()
)

cities.columns = ["City", "Matches"]

fig5 = px.bar(
    cities.head(10),
    x="City",
    y="Matches",
    title="Cities Hosting Most Matches"
)

st.plotly_chart(fig5, use_container_width=True)

st.success("""
Insight:
A few major cities host a significant portion
of IPL matches.
""")

# ----------------------------------
# FINDINGS
# ----------------------------------

st.header("8️⃣ Key Findings")

st.write("""
### Major Findings

1. IPL has grown significantly since 2008.

2. Certain franchises dominate the league.

3. Toss decisions influence match strategy.

4. Some players consistently perform under pressure.

5. IPL is concentrated in major cricket cities.
""")

# ----------------------------------
# CONCLUSION
# ----------------------------------

st.header("9️⃣ Conclusion & Recommendations")

st.info("""
Conclusion:

IPL has evolved into one of the world's largest
cricket leagues.

Recommendations:

- Teams should leverage toss decisions wisely.
- Talent scouting should focus on consistent performers.
- Expanding matches to more cities may improve reach.
""")