# from project import ai_input
# from project import ingredients_data as ingredient_names

# def test_correct_matches():
#     # exact match
#     user_one = "Lamb, Pork, Red Wine"
#     assert ai_input(ingredient_names, user_one, True) == ["Lamb", "Pork", "Red Wine"]

#     # fuzzy match
#     user_two = "lam; por. red w"
#     assert ai_input(ingredient_names, user_two, True) == ["Lamb", "Pork", "Red Wine"]


# def test_threshold_handling():
#     user = "la; po. red w"

#     # high confidence
#     assert ai_input(ingredient_names, user, True, threshold=50) == ["Lamb", "Pork", "Red Wine"]

#     # low confidence
#     assert ai_input(ingredient_names, user, True, threshold=75) == (False, [])


# def test_edge_cases():
#     # empty inputs
#     user_one = ""
#     assert ai_input(ingredient_names, user_one, True) == []

#     # special characters
#     user_two = "sal ; rice.;"
#     assert ai_input(ingredient_names, user_two, True) == ["Salmon", "Rice"]

#     # case sensitivity
#     user_three = "ReD wInE; RiC"
#     assert ai_input(ingredient_names, user_three, True) == ["Red Wine", "Rice"]
