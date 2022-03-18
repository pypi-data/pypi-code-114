import os, sys
import click
import pandas as pd
import json
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer, TfidfTransformer

from typing import List, Dict, Any, Union

from useragent_classifier.custom_transformers.transformers import SplitWords, AutomatedKMeans
from useragent_classifier.features_importances import FeatureImportance
from useragent_classifier.graphical_explanation import run_server

def read_data(ua_path: str) -> pd.DataFrame:
    df = pd.read_csv(ua_path, header=None, sep="azrhuizehfiazhyufazghfai")
    df.columns = ["ua"]
    df = df.drop_duplicates(subset=["ua"], ignore_index=True)
    click.echo(f"Computing for {df.shape[0]} distinct User Agent Found")
    return df

def preprocessing(df: pd.DataFrame) -> pd.DataFrame:
    pipe = Pipeline([
        ("splitter", SplitWords("ua")),
        ("tfidf", TfidfVectorizer(ngram_range=(1, 3), token_pattern=r"(?u)\b\w+\b")),
    ])
    pipe.fit(df)
    res = pipe.transform(df)
    return res, pipe

def compute_feature_importance(features_names: List[str], labels: List[int], df: pd.DataFrame, n_top_words: int) -> Dict[int, pd.DataFrame]:
    computer = FeatureImportance(features_names, labels, df, n_top_words)
    importances = computer.get_features_importances_one_vs_all()
    return importances

def _write_results(output_dir_importance: str, filepath: str, df: pd.DataFrame, res: pd.DataFrame, output_dir:str, importances: Dict[str, Any]) -> pd.DataFrame:

    # Writing results
    output_file = f"{output_dir_importance}/{os.path.basename(filepath).split('.')[0]}_cluster_explanation.json"
    res = pd.concat([df, pd.Series(res)], axis=1)
    res.columns = ["ua", "cluster"]
    res.to_csv(output_file)
    click.echo(f"Results written to {output_file}")

    output_file_importance = f"{output_dir}/{os.path.basename(filepath).split('.')[0]}_clusters.csv"
    click.echo(f"Cluster explanations written to {output_file_importance}")
    with open(output_file_importance, "w") as f:
        json.dump(importances, f)
    return res

def _launch_graphical_explanation(importances: Dict[str, Any], predicted: pd.DataFrame):
    run_server(importances, predicted)

@click.command()
@click.option('-f', '--filepath', type=click.Path(exists=True), help='list of UA to analyze', required=True)
@click.option('-n', '--n-top-words', type=int, help='Number of top words/n-gram  to explain clusters', default=10)
@click.option('--output-dir-importance', type=click.Path(), help='Output file for cluster explanation', default="/tmp")
@click.option('-O', '--output-dir', type=click.Path(), help='Output file for cluster attribution', default="/tmp")
@click.option('-c', '--n-clusters', type=str , help='Number of clusters as a string separated by dot. Example: -c 5,6,7 will try 5, 6 and 7 clusters and will select the best one based on elbow method.', default=str(list(range(2, 10))))
@click.option('--graphical-explanation', is_flag=True, help='If should open a graphical cluster explanation on localhost')
def ua_clustering(filepath: str, n_top_words: int, output_dir_importance: str, output_dir: str, n_clusters: str, graphical_explanation: bool):
    n_clusters = [int(x) for x in n_clusters.replace("[", "").replace("]", "").split(",")]
    df = read_data(filepath)

    df_preprocessed, pipe = preprocessing(df)
    features_names = pipe.named_steps["tfidf"].get_feature_names_out()

    kmeans = AutomatedKMeans(n_clusters)
    kmeans.fit(df_preprocessed)
    res = kmeans.predict(df_preprocessed)
    
    importances = compute_feature_importance(features_names, res, df_preprocessed, n_top_words)
    importances_json = {str(k): v.to_json() for k, v in importances.items()}

    res = _write_results(output_dir_importance, filepath, df, res, output_dir, importances_json)

    if graphical_explanation:
        _launch_graphical_explanation(importances, res)



if __name__ == "__main__":
    ua_clustering()
