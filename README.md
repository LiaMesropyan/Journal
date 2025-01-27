# Action Tracker

This is a Python-based command-line tool to track actions with specific categories, descriptions, and time spent. It supports adding new actions and viewing existing ones.

## Features

- **Add Actions**: Record an action with a description, category, and time spent.
- **Show Actions**: Display all recorded actions.


## Usage
The program accepts the following commands:

## Add an Action
Use the add command to add a new action. You need to provide:

A description of the action (--description or -d).
A category (--category or -c) from the following options: [RAMS, MEET, WORK, PLAN, TARO, CODING,READING]
Time spent (--time or -t) in hours (integer).


Example:

python journal.py add -d "Team meeting on project updates" -c MEET -t 2

## Show Actions

Use the show command to display all recorded actions.

## Help

To get more information about the available commands, use the --help flag:
