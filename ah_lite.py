import click
import requests
import json


@click.group()
def ah():
    """
    Simple CLI for consuming Authors Haven API
    """
    pass


@ah.command()
def list():
    """This returns a list of articles on Authors Haven"""
    url_format = 'http://ah-premier-staging.herokuapp.com/api/articles'
    try:
        response = requests.get(url_format)
        response.raise_for_status()
        data = response.json()
        click.echo(json.dumps(data, indent=2))
    except Exception:
        click.secho("Oops, articles listing failed", fg="red")


@ah.command()
@click.argument('slug')
def view(slug):
    """
    This returns a particular article from the given slug on Authors Haven
    """
    url_format = 'http://ah-premier-staging.herokuapp.com/api/articles/{}'
    click.echo(slug)
    try:
        response = requests.get(url_format.format(slug))
        response.raise_for_status()
        data = response.json()
        click.echo(json.dumps(data, indent=2))
    except Exception as error:
        click.secho(str(error), fg="red")


@ah.command()
@click.argument('slug')
def save(slug):
    """
    This saves a particular article from the given slug on Authors Haven
    """
    url_format = 'http://ah-premier-staging.herokuapp.com/api/articles/{}'
    click.echo(slug)
    try:
        response = requests.get(url_format.format(slug))
        response.raise_for_status()
        data = response.json()
        click.echo(json.dumps(data, indent=2))
        with open('articles/article.json', 'w') as outfile:
            json.dump(data, outfile)
    except Exception as error:
        click.secho(str(error), fg="red")
