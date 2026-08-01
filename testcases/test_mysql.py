from common.mysql_util import query_one


def test_query_user():
    sql = """
    select *
    from user
    where username='test_user'
    """
    data = query_one(sql)
    print(data)

    assert data is not None
    assert data["username"] == "test_user"
    assert data["age"] == 20
