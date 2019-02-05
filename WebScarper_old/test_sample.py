from sqlalchemy import Table, MetaData, create_engine

def inc(x):
    try:
        db = create_engine(x)
        db.execute("Select NOW()")
        return True
    except:
        return False


def test_answer():
    assert inc('postgresql+psycopg2://postgres:integra@localhost:5432/postgres') == True