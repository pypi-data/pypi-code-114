# -*- coding: utf-8 -*-
"""
Creating features for analysis
"""

import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer


def data_processing(data: pd.DataFrame, locations: pd.DataFrame):
    """ takes in specific dataset and creates new columns/features for analysis and modeling

    note:

        - can take in geo locations in specific format
        -  joins the 2 tables and then creates various new columns

    Args:
        data (pd.DataFrame): pandas dataframe with the following columns: 'listing_id', 'user_id', 'target', 'max_level_experience',
               'years_total', 'skills_count', 'max_level_qualification', 'location',
               'country', 'industries', 'categories', 'salary_expectation',
               'qualification_types', 'min_level_experience', 'min_years',
               'min_level_qualification', 'ls_location', 'ls_country', 'l_industry',
               'l_job_function', 'salary_min', 'salary_max', 'qualification_levels'

    Returns:
        featureset (pd.DataFrame): a pandas dataframe with the features ready for analysis and model processing


    """
    geo_data = pd.merge(
        data[["user_id", "location", "country", "ls_location", "ls_country"]],
        locations,
        how="left",
        left_on=["location", "country"],
        right_on=["location", "country"],
        suffixes=("_c", "_cgeo"),
    )
    geo_data = pd.merge(
        geo_data,
        locations,
        how="left",
        left_on=["ls_location", "ls_country"],
        right_on=["location", "country"],
        suffixes=("_c", "_l"),
    )

    geo_data = geo_data[["lat_c", "lon_c", "lat_l", "lon_l"]]
    geo_data["dist"] = np.nan
    for i, r in geo_data.iterrows():
        x1 = float(r["lat_c"])
        x2 = float(r["lat_l"])
        y1 = float(r["lon_c"])
        y2 = float(r["lon_l"])

        dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        geo_data["dist"][i] = dist
    # add flags for missing loc req and for missing loc c

    # get ratios between columns
    col = "max_level_experience"
    col = "years_total"
    col = "skills_count"
    col = "max_level_qualification"

    ratios = pd.DataFrame(data["user_id"])

    # get non empty rows
    ratios["exp_ratio"] = (
        data["max_level_experience"].dropna().div(data["min_level_experience"].dropna())
    )
    ratios["qual_ratio"] = (
        data["max_level_qualification"]
        .dropna()
        .div(data["min_level_qualification"].dropna())
    )
    ratios["years_ratio"] = data["years_total"].dropna().div(data["min_years"].dropna())

    industries = pd.DataFrame(data["user_id"])
    industries["industry_match"] = np.nan

    industries["function_match"] = np.nan
    # match industries
    for i, r in data.iterrows():
        if r["industries"] is not None:
            can_ind = r["industries"].split(",")
            list_ind = r["l_industry"]
            # find if listing industry is in the candidate list
            if list_ind in can_ind:
                industries["industry_match"][i] = 1
            else:
                industries["industry_match"][i] = 0

        if r["categories"] is not None:
            can_func = r["categories"].split(",")
            list_func = r["l_job_function"]
            # find if listing industry is in the candidate list
            if list_func in can_func:
                industries["function_match"][i] = 1
            else:
                industries["function_match"][i] = 0

    data[["l_industry", "l_job_function"]] = data[
        ["l_industry", "l_job_function"]
    ].fillna("Other")

    # convert categories to features
    enc = OneHotEncoder(handle_unknown="ignore")
    enc.fit(data[["l_industry", "l_job_function"]])
    # remember to output the encoder as a loblib before deploying
    categorical = pd.DataFrame(
        enc.transform(data[["l_industry", "l_job_function"]]).toarray(),
        columns=enc.get_feature_names(),
    )

    # salary between range
    salary = pd.DataFrame(data["user_id"])
    salary["salary_match"] = np.where(
        (data["salary_min"] <= data["salary_expectation"])
        & (data["salary_max"] >= data["salary_expectation"]),
        1,
        0,
    )
    # salary expect % of max
    salary["salary_ratio"] = data["salary_expectation"].div(data["salary_max"])

    # qualification match
    # no data for this now
    # fuzzy match percentage between- will work if application and lisitng are in the same language

    # fuzz.token_sort_ratio('To be or not to be', 'To be not or to be')

    # Combine into final feature set

    featureset = data[["listing_id", "user_id", "target"]]

    featureset["location_distince"] = geo_data["dist"]
    featureset["missing_location"] = geo_data["dist"]
    # replace nan with mean value and give missing value indicator
    geo_imputer = SimpleImputer(missing_values=np.nan, strategy="mean")
    geo_imputer = geo_imputer.fit(
        np.array(featureset["location_distince"]).reshape(-1, 1)
    )
    a = featureset["missing_location"]
    a[~np.isnan(a)] = 0
    a[np.isnan(a)] = 1
    featureset["location_distince"] = geo_imputer.transform(
        np.array(featureset["location_distince"]).reshape(-1, 1)
    )

    # add ratios
    ratios.replace([np.inf, -np.inf], np.nan, inplace=True)
    featureset[["exp_ratio", "qual_ratio", "years_ratio"]] = ratios[
        ["exp_ratio", "qual_ratio", "years_ratio"]
    ]
    featureset[
        ["missing_exp_ratio", "missing_qual_ratio", "missing_years_ratio"]
    ] = ratios[["exp_ratio", "qual_ratio", "years_ratio"]]

    featureset["missing_exp_ratio"][~np.isnan(featureset["missing_exp_ratio"])] = 0
    featureset["missing_exp_ratio"][np.isnan(featureset["missing_exp_ratio"])] = 1

    featureset["missing_qual_ratio"][~np.isnan(featureset["missing_qual_ratio"])] = 0
    featureset["missing_qual_ratio"][np.isnan(featureset["missing_qual_ratio"])] = 1

    featureset["missing_years_ratio"][~np.isnan(featureset["missing_years_ratio"])] = 0
    featureset["missing_years_ratio"][np.isnan(featureset["missing_years_ratio"])] = 1

    geo_imputer = SimpleImputer(missing_values=np.nan, strategy="mean")
    geo_imputer = geo_imputer.fit(
        featureset[["exp_ratio", "qual_ratio", "years_ratio"]]
    )
    featureset[["exp_ratio", "qual_ratio", "years_ratio"]] = geo_imputer.transform(
        featureset[["exp_ratio", "qual_ratio", "years_ratio"]]
    )

    featureset[["industry_match", "function_match"]] = industries[
        ["industry_match", "function_match"]
    ]
    featureset[["missing_industry", "missing_function"]] = industries[
        ["industry_match", "function_match"]
    ]

    featureset["missing_industry"][~np.isnan(featureset["missing_industry"])] = 0
    featureset["missing_industry"][np.isnan(featureset["missing_industry"])] = 1
    featureset["missing_function"][~np.isnan(featureset["missing_function"])] = 0
    featureset["missing_function"][np.isnan(featureset["missing_function"])] = 1

    geo_imputer = SimpleImputer(missing_values=np.nan, strategy="mean")
    geo_imputer = geo_imputer.fit(featureset[["industry_match", "function_match"]])
    featureset[["industry_match", "function_match"]] = geo_imputer.transform(
        featureset[["industry_match", "function_match"]]
    )

    salary.replace([np.inf, -np.inf], np.nan, inplace=True)
    featureset[["salary_ratio", "salary_match"]] = salary[
        ["salary_ratio", "salary_match"]
    ]
    featureset["salary_ratio"] = np.where(
        featureset["salary_ratio"] > 5, 6, featureset["salary_ratio"]
    )
    featureset[["missing_salary_ratio", "missing_salary_match"]] = salary[
        ["salary_ratio", "salary_match"]
    ]

    featureset["missing_salary_ratio"][
        ~np.isnan(featureset["missing_salary_ratio"])
    ] = 0
    featureset["missing_salary_ratio"][np.isnan(featureset["missing_salary_ratio"])] = 1
    featureset["missing_salary_match"][
        ~np.isnan(featureset["missing_salary_match"])
    ] = 0
    featureset["missing_salary_match"][np.isnan(featureset["missing_salary_match"])] = 1

    featureset=featureset.join(categorical)#this increases the column qty, should be removed if not used for ML,
    featureset.fillna(0, inplace=True)

    return featureset
