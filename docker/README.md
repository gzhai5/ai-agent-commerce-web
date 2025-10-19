# Docker Guide

## Description

* `docker-compose.yml`: contains all the services needed both for dev and deploy.

## Services

### backend-server

Contains the logic to retrieve database data. Currently for simplicty, it is very simple, get all data.

### mcp-server

Write AI agent invoke in the [MCP](https://modelcontextprotocol.io/overview) method. Contains the logic of how AI bot answer human queries.

### dozzle

A log monitor to easily monitor all logs of the docker containers.