import pytest
from pathlib import Path
from task1.file_merge import merge_sorted_files


# @pytest.fixture
# def create_tmp_file(request):
#     file_name, value = request.param
#     with open(file_name, "w") as f:
#         f.write(str(value))
#     yield file_name
#     os.remove(file_name)
#
#
# @pytest.mark.parametrize(
#     "create_tmp_file",
#     [
#         ("text1.txt", (9, 8, 7, 6, 5, 4)),
#         ("text2.txt", (1, 3, 2)),
#         ("text3.txt", (-1, -2, -3, 0)),
#     ],
#     indirect=["create_tmp_file"],
# )
def test_file_merge(tmpdir):
    tmpdir.join(f"text1.txt").write("9\n8\n7\n6\n5\n4\n")
    tmpdir.join(f"text2.txt").write("1\n3\n2\n")
    tmpdir.join(f"text3.txt").write("-1\n-2\n-3\n0\n")

    assert list(merge_sorted_files([f"{Path(str(tmpdir))}/text1.txt", f"{Path(str(tmpdir))}/text2.txt",
                                    f"{Path(str(tmpdir))}/text3.txt"])) == range(-3, 10)
