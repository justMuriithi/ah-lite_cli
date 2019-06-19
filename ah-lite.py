import click
import requests
import json


@click.group()
def main():
    """
    Simple CLI for consuming Authors Haven API
    """
    pass


@main.command()
def list():
    """This returns a list of articles on Authors Haven"""
    url_format = 'http://ah-premier-staging.herokuapp.com/api/articles'
    response = requests.get(url_format)

    data = response.json()
    try:
        click.echo(json.dumps(data, indent=2))
    except Exception:
        click.echo("Oops, articles listing failed")


@main.command()
@click.argument('slug')
def view(slug):
    """
    This returns a particular article from the given slug on Authors Haven
    """
    url_format = 'http://ah-premier-staging.herokuapp.com/api/articles/{}'
    click.echo(slug)
    response = requests.get(url_format.format(slug))

    data = response.json()
    try:
        click.echo(json.dumps(data, indent=2))
    except Exception as error:
        click.echo(str(error))


@main.command()
@click.argument('slug')
def save(slug):
    """
    This saves a particular article from the given slug on Authors Haven
    """
    url_format = 'http://ah-premier-staging.herokuapp.com/api/articles/{}'
    click.echo(slug)
    response = requests.get(url_format.format(slug))

    data = response.json()
    try:
        click.echo(json.dumps(data, indent=2))
        with open('articles/article.json', 'w') as outfile:
            json.dump(data, outfile)
    except Exception as error:
        click.echo(str(error))


if __name__ == '__main__':
    main()
