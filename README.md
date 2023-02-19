# Customer admin example

This is an example of customer admin using Abstra dashes.

This example contains a simple CRUD application for illustration purposes

# Setting up

## VSCode extension
Install our vscode extension [Link](https://marketplace.visualstudio.com/items?itemName=abstra.abstraextension)

## Requirements
Install all required libraries
```sh
pip install -r requirements.txt
```

## Seed
Setup an empty database

```sh
cd src
python -c 'import setup.seed as ss;ss.run()'
```
