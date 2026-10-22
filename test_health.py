import app


def test_health_returns_ok():
    result = app.health()
    assert result["status"] == "ok"
    assert result["dependencies"]["database"] == "ok"
    assert result["dependencies"]["cache"] == "ok"
