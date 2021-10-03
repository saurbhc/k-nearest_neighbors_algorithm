# k-nearest_neighbors_algorithm
CS5920 - Machine Learning - Chapter 1 - k-nearest neighbors algorithm

### Setup

python3 -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt

python calculate_k_nearest_neighbors.py

~~


    Find Euclidean Distance between multiple n-dimension cartesian-coordinate(s) with given same-dimension cartesian-coordinate

    (note) Send your suggestion on Saurabh.Chopra.2021@live.rhul.ac.uk for any suggestions.
    
!Enter comma-seperated-without-spaces values your `test-coordinate` vector/cartesian-coordinate (Example: 1,2,3): 1,1 

How many coordinates would you like to compute the distance with your test-coordinate with? (Example: 3): 4

!Enter comma-seperated-without-spaces values your `1` vector/cartesian-coordinate (Example: 1,2,3-label): 0,0-positive

!Enter comma-seperated-without-spaces values your `2` vector/cartesian-coordinate (Example: 1,2,3-label): 0,2-positive

!Enter comma-seperated-without-spaces values your `3` vector/cartesian-coordinate (Example: 1,2,3-label): 1,2-negative

!Enter comma-seperated-without-spaces values your `4` vector/cartesian-coordinate (Example: 1,2,3-label): 0,3-negative

`Euclidean Distance Table:
 
 FromVector ToVector     Label  EuclideanDistance

0        1,1      0,0  positive           1.414214

0        1,1      0,2  positive           1.414214

0        1,1      1,2  negative           1.000000

0        1,1      0,3  negative           2.236068

! Which `k`-nearest-neighbor Algorithm would you like to Apply: 3

3-Nearest-Neighbour Distance Table:

  FromVector ToVector     Label  EuclideanDistance

0        1,1      1,2  negative           1.000000

0        1,1      0,0  positive           1.414214

0        1,1      0,2  positive           1.414214
    

>> 3-Nearest-Neighbours are: ['negative', 'positive', 'positive']

>> Most Common Label is: positive
