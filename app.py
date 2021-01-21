import streamlit as st
import pandas as pd
import numpy as np
from judge import Judge
from utils import download_button

st.sidebar.markdown("# JLI v2")

st.sidebar.markdown("## Upload judge data")
uploaded_csv_judge = st.sidebar.file_uploader("Upload CSV", type="csv", key="judge")
if uploaded_csv_judge:
    df_judge = pd.read_csv(uploaded_csv_judge)
    df_judge = df_judge.drop_duplicates(subset=["Judge Code Names"])  # There is a duplicate
    df_judge.loc[:, "Judge Code Names"] = [x.strip().lower() for x in df_judge.loc[:, "Judge Code Names"]]
    st.sidebar.write(f"{df_judge.shape[0]} rows and {df_judge.shape[1]} columns")


def process_judgments(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    concurrence_collist = [
        "Concurrence1",
        "Concurrence2",
        "Concurrence3",
        "Concurrence4",
        "Concurrence5",
        "Concurrence6",
        "Concurrence7",
        "Concurrence8",
        "Concurrence9",
        "Concurrence10",
        "Concurrence11",
        "Concurrence12",
    ]
    dissent_collist = [
        "Dissent1",
        "Dissent2",
        "Dissent3",
        "Dissent4",
        "Dissent5",
        "Dissent6",
    ]
    bench_collist = [
        "Bench1",
        "Bench2",
        "Bench3",
        "Bench4",
        "Bench5",
        "Bench6",
        "Bench7",
        "Bench8",
        "Bench9",
        "Bench10",
        "Bench11",
        "Bench12",
        "Bench13",
    ]
    df["concurrence"] = df[concurrence_collist].apply(
        lambda x: list(x.values),
        axis=1,
    )
    df["dissent"] = df[dissent_collist].apply(
        lambda x: list(x.values),
        axis=1,
    )
    df["bench"] = df[bench_collist].apply(
        lambda x: list(x.values),
        axis=1,
    )

    df = df.loc[
        :,
        [
            "Name of Case",
            "Date of Decision",
            "Split",
            "Type Appellant",
            "Type Respondent",
            "Jurisdiction",
            "Who Won",
            "concurrence",
            "dissent",
            "bench",
        ],
    ]

    return df


st.sidebar.markdown("## Upload judgment data")
uploaded_csv_judgment = st.sidebar.file_uploader("Upload CSV", type="csv", key="judgment")
if uploaded_csv_judgment:
    df_judgment = process_judgments(uploaded_csv_judgment)
    st.sidebar.write(f"{df_judgment.shape[0]} rows and {df_judgment.shape[1]} columns")

st.sidebar.markdown("## Upload judgment text data")
uploaded_csv_text = st.sidebar.file_uploader("Upload CSV", type="csv", key="text")
if uploaded_csv_text:
    df_text = pd.read_csv(uploaded_csv_text)
    st.sidebar.write(f"{df_text.shape[0]} rows and {df_text.shape[1]} columns")


mode = st.radio(
    label="",
    options=["Judges", "Judgments", "Judgment text"],
    index=0,
)

if mode == "Judges":
    if uploaded_csv_judge:
        st.write(df_judge)
        count1 = df_judge["Judge Code Names"].nunique()  # TODO: If you look at "Judges", there is a duplicate
        st.write(f"No of judges: {count1}, {df_judge.shape[0]}")

if mode == "Judgments":
    if uploaded_csv_judgment:
        st.markdown("## Appellant types and count")
        st.write(df_judgment["Type Appellant"].value_counts())
        st.markdown("## Respondent types and count")
        st.write(df_judgment["Type Respondent"].value_counts())
        st.markdown("## List of judges")
        all_judges = [item for sublist in list(df_judgment.bench.values) for item in sublist]
        all_judges = list(set([j.strip().lower() for j in all_judges if j not in ["", " ", "  ", np.NaN]]))
        st.write(f"Total no of judges found (in benches): {len(all_judges)}")
        st.write(all_judges)
        # 2. Count no of judgements by judge
        st.write("## Number of judgments by judge")
        df = []
        for index, row in df_judgment.iterrows():
            # row.bench, row.concurrence, row.dissent
            judges = list([j.strip().lower() for j in list(row.bench) if j not in ["", " ", "  ", np.NaN]])
            for judge in judges:
                new_df = [
                    row["Name of Case"],
                    judge,
                    row["Date of Decision"],
                    row["Split"],
                    row["Type Appellant"],
                    row["Type Respondent"],
                    row["Jurisdiction"],
                    row["Who Won"],
                ]
                df.append(new_df)
        df = pd.DataFrame(
            df,
            columns=[
                "case_name",
                "judge",
                "date",
                "split",
                "appellant_type",
                "respondent_type",
                "jurisdiction",
                "who_won",
            ],
        )
        st.write(df.judge.value_counts())
        st.write("## Count by various groups")

        judge_profile_cols = []
        if uploaded_csv_judge:
            df_judge_profile = df_judge.filter(
                [
                    "Judge Code Names",
                    "Appointing Chief Justice",
                    "Parent High Court",
                    "Appointing Authority",
                    "Bar and Non-Bar",
                    "Professional Background in Subordinate Judiciary",
                ]
            )
            df_judge_profile.columns = [
                "judge",
                "appointing_cji",
                "parent_hc",
                "appointing_authority",
                "bar_background",
                "judiciary_background",
            ]
            judge_profile_cols = list(df_judge_profile.columns)
            df = df.merge(df_judge_profile, how="left", on="judge")

        grouping_vars = st.multiselect(
            "Choose variables for grouping",
            ["judge", "appellant_type", "respondent_type"] + judge_profile_cols,
            ["judge"],
        )
        st.write("Grouping is done in following order:", grouping_vars)
        st.write("Note: The last column represents the count of cases, irrespective of column name!")

        df_grouped = (
            df.drop(
                ["case_name", "date", "jurisdiction", "who_won"],
                axis=1,
            )
            .groupby(grouping_vars)
            .count()
            .iloc[:, 0]
            .reset_index()
            .sort_values(by=grouping_vars)
        )

        st.write(df_grouped)
        st.write(
            download_button(df_grouped, "df_grouped.csv", "Click to download data!"),
            unsafe_allow_html=True,
        )

        # 3. Count no of Concurrence, Dissent by judge

if mode == "Judgment text":
    if uploaded_csv_text:
        st.write(df_text)
        st.write(df_text.describe())
