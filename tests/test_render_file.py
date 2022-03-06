import pytest
from absql import render_file


@pytest.fixture
def extra_sql_path():
    return "tests/files/extra.sql"


@pytest.fixture
def simple_sql_path():
    return "tests/files/simple.sql"


@pytest.fixture
def simple_yml_path():
    return "tests/files/simple.yml"


@pytest.fixture
def constructor_sql_path():
    return "tests/files/constructor.sql"


def test_render_simple_sql(simple_sql_path):
    sql = render_file(simple_sql_path)
    assert sql == "SELECT * FROM my_table"


def test_render_simple_yml(simple_yml_path):
    sql = render_file(simple_yml_path)
    assert sql == "SELECT * FROM my_table"


def test_render_additional_sql(extra_sql_path):
    sql = render_file(extra_sql_path, extra_context={"extra": "my_extra_context"})
    assert sql == "SELECT * FROM my_table WHERE my_extra_context"


def test_render_constructor_sql(constructor_sql_path):
    sql = render_file(
        constructor_sql_path,
        extra_constructors={"!get_table": lambda: "my_constructor_table"},
    )
    assert sql == "SELECT * FROM my_constructor_table"
