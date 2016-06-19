#!/bin/bash
curl -XDELETE localhost:9200/condominio/?pretty
curl -XPUT localhost:9200/condominio/?pretty
curl -XPUT localhost:9200/condominio/_mapping/condominio?pretty --data-binary @mapping.json

