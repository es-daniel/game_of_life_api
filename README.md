# Game of Life Python API
## _The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970. It is a zero-player game, meaning that its evolution is determined by its initial state, requiring no further input_ 

## Installation

The API requires [Python](https://www.python.org/) v3.9.4 to run.

Install the dependencies and devDependencies and start the server.

```sh
cd python_api
pip3 install -r requirements.txt
python3 app.py or gunicorn app:app
```

## Plugins

The API was made using plugins like the listed below:

| Plugin | README |
| ------ | ------ |
| Gunicorn | [https://gunicorn.org/] |
| Flask | [https://flask.palletsprojects.com/en/2.0.x/] |

## End-Points
To get and initial pattern use this end-point:
* http://127.0.0.1:8000/start?pattern=
* pattern is a URL param and it can be: rand, gosper_glider_gun or pulsar.

To update the current grid use this end-point:
* http://127.0.0.1:8000/update

## License

MIT