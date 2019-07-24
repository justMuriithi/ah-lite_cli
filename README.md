# ah-lite_cli
[![Coverage Status](https://coveralls.io/repos/github/justMuriithi/ah-lite_cli/badge.svg?branch=develop)](https://coveralls.io/github/justMuriithi/ah-lite_cli?branch=develop)
[![Build Status](https://travis-ci.com/justMuriithi/ah-lite_cli.svg?branch=develop)](https://travis-ci.com/justMuriithi/ah-lite_cli)
### How to install
- Clone this repository on your local machine.
- Navigate to the main directory and run `pip install --editable .`
- You can now run the commands
### Available commands
- `ah --help` - get help information for the main command.
- `ah view --help` - get help information for sub-command view.
- `ah list --help` - get help information for sub-command list.
- `ah view <article_slug>` - get a single article from the database and display it.
- `ah save <article_slug>` - get a single article and save it in a docs folder as a json file.
- `ah list` - get all articles. Limit is default to two articles.
- `ah list --limit <str>` - set the limit of how many articles can be viewed.
- `ah list --search <author_name>` - Allows user to search article with the author name.
N.B. - you can use all options at the same time, for example, ah list --limit 10 --search benson will return the first ten articles written by the author Benson.
