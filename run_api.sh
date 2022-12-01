#!/bin/bash

docker-compose kill api && docker-compose pull api && docker-compose up -d api