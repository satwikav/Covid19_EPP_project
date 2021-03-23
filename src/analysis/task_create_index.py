import pandas as pd
import pytask

from src.config import BLD

sub_index_scores = [
    "SI_E1",
    "SI_E2",
    "SI_E3",
    "SI_E4",
    "R_index_score",
    "SI_S1",
    "SI_S2",
    "SI_S3",
    "SI_S4",
]
stringency_indices = ["E_index_score", "S_index_score", "stringency_index_score"]
subscores = [sub_index_scores[0:4], sub_index_scores[5:9], sub_index_scores]


def calculate_sub_index_score(df, policy_value, flag, recorded_flag, maximum):
    """Sub Score Indicies.

    This function calculates stringency level for each policy category.

    Args:
        df (df): Dataframe
        policy_value (int): Ordinal scale measurement that represents level of policy
                            stringency.
        flag (int): Dummy variable indicating whether or not an indicator
                    uses a flag to distinguish between regionally and federally
                    employed policies.
        recorded_flag (int): Dummy variable indicating whether the policy is implemented
                             regionally or federally.
        maximum (int): Maximum ordinal scale value each indicator can take.

    Note:
        For more detailed descriptions of args, see code book.

    Returns:
        int: A value between 0 and 100 with 0 indicating no policy restriction in place
        and 100 indicating the highest level of stringency a policy can take on.

    """
    numerator = df[policy_value] - 0.5 * (df[flag] - df[recorded_flag])
    denominator = df[maximum]
    return 100 * (numerator / denominator)


def create_index(
    df,
    sub_index_scores,
    ordinal_values,
    flag_dummies,
    recorded_flags,
    maxima,
    stringency_indices,
    subscores,
    path,
):
    """.

    This function calculates.

    Args:




    Returns:


    """
    for sub_index_score, ordinal_value, flag_dummy, recorded_flag, maximum in zip(
        sub_index_scores, ordinal_values, flag_dummies, recorded_flags, maxima
    ):
        df[sub_index_score] = calculate_sub_index_score(
            df, ordinal_value, flag_dummy, recorded_flag, maximum
        )
    for stringency_index, subscore in zip(stringency_indices, subscores):
        df[stringency_index] = df[subscore].mean(axis=1)
    return df.to_csv(path)


@pytask.mark.depends_on(BLD / "data" / "covid_policy.csv")
@pytask.mark.produces(BLD / "analysis" / "stringency_index_data.csv")
def task_create_index(depends_on, produces):
    # Read data
    data = pd.read_csv(depends_on).set_index("date")
    # Input lists
    ordinal_values = [col for col in data if col.startswith("scale")]
    flag_dummies = [col for col in data if col.startswith("flag")]
    recorded_flags = [col for col in data if col.startswith("recorded")]
    maxima = [col for col in data if col.startswith("maximum")]
    # Create dataset with indicies
    create_index(
        data,
        sub_index_scores,
        ordinal_values,
        flag_dummies,
        recorded_flags,
        maxima,
        stringency_indices,
        subscores,
        produces,
    )
