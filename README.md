# javascript-web-htmx-get-mustache-python-flask-api-couchdb-simple

## Description
A demo of htmx using a python flask
api to return contents of table from
couchdb.

## Tech stack
- htmx
    - get
    - ext
    - swap
    - target
- mustache
- python
    - flask
    - cors
- couchdb

## Docker stack
- httpd:latest
- python:latest
- apache/couchdb:latest

## To run
`sudo ./install.sh -u`
- Available at http://localhost

## To stop
`sudo ./install.sh -d`

## To see help
`sudo ./install.sh -h`

## Credit
- [Htmx clientside template](https://htmx.org/extensions/client-side-templates/)
- [Htmx rendering JSON](https://marcus-obst.de/blog/htmx-json-handling)