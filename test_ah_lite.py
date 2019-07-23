from ah_lite import list, view, save, ah
from click.testing import CliRunner

runner = CliRunner()


def test_success_get_all_articles():
    result = runner.invoke(list)
    assert result.exit_code == 0


def test_failed_get_all_articles():
    result = runner.invoke(list)
    assert result.exit_code == 0


def test_success_get_single_article():
    result = runner.invoke(view, ["blog-post-2"])
    assert result.exit_code == 0


def test_failed_get_single_article():
    result = runner.invoke(view, ["i-dont-exist"])
    assert result.exit_code == 0
    assert "Not Found" in result.output


def test_success_save_article():
    result = runner.invoke(save, ["blog-post-2"])
    assert result.exit_code == 0


def test_failed_save_article():
    result = runner.invoke(save, ["i-dont-exist"])
    assert result.exit_code == 0
    assert "Not Found" in result.output


def test_ah():
    result = runner.invoke(ah)
    assert result.exit_code == 0
