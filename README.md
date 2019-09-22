# trakt sopel plugin

[![pypi status](https://img.shields.io/pypi/v/sopel-modules.trakt.svg)](https://pypi.org/project/sopel-modules.trakt/)
[![Build Status](https://travis-ci.org/shanedabes-sopel/sopel-trakt.svg?branch=master)](https://travis-ci.org/shanedabes-sopel/sopel-trakt)
[![pyup status](https://pyup.io/repos/github/shanedonohoe/poku/shield.svg)](https://pyup.io/account/repos/github/shanedabes-sopel/sopel-trakt/)

A sopel plugin that returns the user's last play on trakt

## Installation

Can be installed from the pip using:

    pip install sopel_modules.trakt


## Testing

If you would like to make a contribution, be sure to run the included tests. Test requirements can be installed using:

    pip install -r requirements_dev.txt

run tests using:

    make test

and start up a test sopel instance with docker by using:

    docker-compose up -d
    docker attach weechat
