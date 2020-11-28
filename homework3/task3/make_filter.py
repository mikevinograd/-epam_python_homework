# I decided to write a code that generates data filtering object from a list of keyword parameters:


class Filter:
    """
    Helper filter class. Accepts a list of single-argument
    functions that return True if object in list conforms to some criteria
    """

    def __init__(self, functions):
        self.functions = functions

    def apply(self, data):
        return [item for item in data if all(i(item) for i in self.functions)]


def make_filter(**keywords):
    """
    Generate filter object for specified keywords
    """
    filter_funcs = []
    for key, value in keywords.items():
        def keyword_filter_func(data, value=value, key=key):
            return data.get(key) == value
            # return data[key] == value

        filter_funcs.append(keyword_filter_func)
    return Filter(filter_funcs)


# sample_data = [
#     {
#         "name": "Bill",
#         "last_name": "Gilbert",
#         "occupation": "was here",
#         "type": "person",
#     },
#     {"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly"},
# ]
