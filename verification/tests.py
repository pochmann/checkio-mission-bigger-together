"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [1,2,3,4],
            "answer": 3087,
            "explanation": "4321 - 1234 = 3087"
        },
        {
            "input": [1,2,3,4, 11, 12],
            "answer": 32099877,
            "explanation": "43212111 - 11112234 = 32099877"
        },
        {
            "input": [0, 1],
            "answer": 9,
            "explanation": "10 - 01 = 9"
        },
        {
            "input": [100],
            "answer": 0,
            "explanation": "100 - 100 = 0"
        }
    ],
    "Extra": [
        {
            "input": [3, 4],
            "answer": 9,
            "explanation": "43 - 34 = 9"
        },{
            "input": [3, 12, 22, 32],
            "answer": 2009880,
            "explanation": "3232212 - 1222332 = 2009880"
        }
    ]
}
