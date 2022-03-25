import os
import mock
import pytest
from pandas import DataFrame
from sqlalchemy import create_engine
from absql.macros.db import table_exists


@pytest.fixture(scope="module")
def engine():
    engine = create_engine("duckdb:///:memory:")
    engine.execute(
        "register",
        ("my_table", DataFrame.from_dict({"name": ["Thelma"], "friend": "Louise"})),
    )
    return engine


def test_table_exists(engine):
    exists_true = table_exists("my_table", engine)
    exists_false = table_exists("nonexistent_table", engine)
    assert exists_true
    assert exists_false is False


@pytest.fixture(autouse=True)
def mock_settings_env_vars():
    with mock.patch.dict(os.environ, {"AB__URI": "sqlite:///:memory:"}):
        yield


def test_ab_uri():
    exists_false = table_exists("some_table")
    assert exists_false is False