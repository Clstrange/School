import sys
"""Contains tests to run on the Exercise_seven main.py program"""

def hay_stack_TEST(hay_stack_object):
    """tests that the HayStack class properly creates objects"""
    try:
        hay_stack_object("http://roversgame.net/cs3270/page1.html", 4)
        print("Test Passed")
    except TypeError as error:
        print(f"Test Failed - {error}")

def crawl_TEST(hay_stack_object):
    try:
        test_object = hay_stack_object("http://roversgame.net/cs3270/page1.html", 4)
        assert(len(test_object.page_list) == 5), f"Page_list should have 5 items, instead it has - {len(test_object.page_list)}"
        print(f"Test Passed, Items consist of {test_object.page_list}")
    except Exception as error:
        print(error)
        print(f"\t - items consist of {test_object.page_list}")

def index_TEST(hay_stack_object):
    try:
        test_object = hay_stack_object("http://roversgame.net/cs3270/page1.html", 4)
        print(f"Unable to reasonably test check index data yourself - {test_object.index} - {len(test_object.index)}")
    except Exception as error:
        print(error)

def graph_TEST(hay_stack_object):
    try:
        test_object = hay_stack_object("http://roversgame.net/cs3270/page1.html", 4)
        print(f"Unable to reasonably test check graph data yourself - {test_object.graph} - {len(test_object.graph)}")
    except Exception as error:
        print(error)

