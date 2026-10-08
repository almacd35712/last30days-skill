import sqlite3
from unittest import mock

import pytest
from lib import library_index


def test_sync_library_closes_database(tmp_path):
    db_path = tmp_path / "library.db"
    connection = library_index._connect(db_path)
    with mock.patch.object(library_index, "_connect", return_value=connection):
        library_index.sync_library(tmp_path, tmp_path, db_path=db_path)
    with pytest.raises(sqlite3.ProgrammingError, match="closed"):
        connection.execute("SELECT 1")
