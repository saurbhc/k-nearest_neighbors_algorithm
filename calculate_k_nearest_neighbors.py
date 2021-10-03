import pandas as pd

from calculate_euclidean_distance import EuclideanDistance


def get_input():
    help_text = """
    Find Euclidean Distance between multiple n-dimension cartesian-coordinate(s) with given same-dimension cartesian-coordinate

    (note) Send your suggestion on Saurabh.Chopra.2021@live.rhul.ac.uk for any suggestions.
    """
    print(help_text)
    from_vector = input(
        f"!Enter comma-seperated-without-spaces values your `test-coordinate` vector/cartesian-coordinate (Example: 1,2,3): "
    )
    number_of_vectors = int(input(
        f"How many coordinates would you like to compute the distance with your test-coordinate with? (Example: 3): "))
    euclidean_distance_df = pd.DataFrame()
    to_vector = None
    for vector_number in range(number_of_vectors):
        counter = vector_number + 1
        vector_or_cartesian_coordinate = input(
            f"!Enter comma-seperated-without-spaces values your `{counter}` vector/cartesian-coordinate (Example: 1,2,3-label): "
        )
        if not from_vector:
            from_vector = vector_or_cartesian_coordinate
        else:
            to_vector = vector_or_cartesian_coordinate
        ed = EuclideanDistance(_from_vector=from_vector, _to_vector=to_vector)
        ed_df = ed.execute()
        if euclidean_distance_df.empty:
            euclidean_distance_df = ed_df
        else:
            euclidean_distance_df = euclidean_distance_df.append(ed_df)

    print(f"""
>> Euclidean Distance Table:
{euclidean_distance_df.to_string()}
            """)

    _k_in_knn_value = int(input(
        f"Which `k`-nearest-neighbor Algorithm would you like to Apply: "
    ))

    return _k_in_knn_value, number_of_vectors, from_vector, to_vector, euclidean_distance_df


def most_common(lst):
    return max(set(lst), key=lst.count)


class KNearestNeighborsAlgorithm:
    def __init__(self, _k_in_knn_value, _euclidean_distance_df):
        self.euclidean_distance_df = _euclidean_distance_df
        self.k_in_knn_value = _k_in_knn_value

    def execute(self):
        return self.euclidean_distance_df.sort_values('EuclideanDistance')


if __name__ == "__main__":
    k_in_knn_value, number_of_vectors, from_vector, to_vector, euclidean_distance_df = get_input()

    knn_obj = KNearestNeighborsAlgorithm(_k_in_knn_value=k_in_knn_value, _euclidean_distance_df=euclidean_distance_df)
    knn_distance = knn_obj.execute()

    print(f"""
>> {k_in_knn_value}-Nearest-Neighbour Distance Table:
{knn_distance.head(k_in_knn_value)}
    """)

    print(f"""
>> {k_in_knn_value}-Nearest-Neighbours are: {knn_distance.head(k_in_knn_value).Label.tolist()}
>> Most Common Label is: {most_common(knn_distance.head(k_in_knn_value).Label.tolist())}
    """)


