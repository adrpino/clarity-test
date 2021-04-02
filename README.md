# Clarity take home
The repository is composed of two parts:
* The `playground` folder, where the jupyter notebook of the analysis of the data is done
* The `app` folder, with a Flask application serving the model.

## Usage
In order to run the development environment, you should do (you need [Pipenv](https://pipenv.pypa.io/en/latest/) installed)

```bash
# First time
pipenv update

# Then you can run the application with
pipenv shell
flask run
```

## Build
To build the Docker image, you should do:

```bash
docker build -t 'clarity' .
```

## Run:
To run (interactively, for illustration purposes), simply do:

```bash
docker run  -p 5000:5000 -it 'clarity'
```

Once running, you can test it with the following request:

```bash
curl -X POST localhost:5000/predict -H 'Content-Type: application/json' \
	-d '{
    "kjkrfgld": "qzGkS", 
    "bpowgknt": "THHLT",
    "raksnhjf": "DtMvg",
    "vwpsxrgk": "XAmOF",
    "omtioxzz": 17, 
    "yfmzwkru": -10,
    "tiwrsloh": -6,
    "weioazcf": 10.5
}'
```
