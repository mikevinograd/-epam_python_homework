import pytest
from task3.make_filter import make_filter, Filter

sample_data = [
    {
        "name": "Bill",
        "last_name": "Gilbert",
        "occupation": "was here",
        "type": "person",
    },
    {"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly"},
    {"name": "Lisa", "last_name": "Monetochka", "occupation": "singer", "type": "gold"},
]


@pytest.mark.parametrize(
    ["kwargs", "sample_data", "expected"],
    [
        (
            {"last_name": "Monetochka", "occupation": "singer"},
            sample_data,
            sample_data[2],
        ),
        ({"kind": "parrot", "type": "bird"}, sample_data, sample_data[1]),
        ({"last_name": "Gilbert"}, sample_data, sample_data[0]),
    ],
)
def test_make_filter(kwargs, sample_data, expected):
    assert make_filter(**kwargs).apply(sample_data) == [expected]
