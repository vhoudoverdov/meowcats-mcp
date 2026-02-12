# meowfacts-mcp

This repository is designed to be a tutorial for building very simple MCP servers. It shows the underlying components of MCP servers (like python scripts) using a public API called  [meowfacts](https://github.com/wh-iterabb-it/meowfacts)  by  [wh-iterabb-it](https://github.com/wh-iterabb-it/)

This server uses much of the same boilerlate used by the tutorial example on  [modelcontextprotocol.io](https://modelcontextprotocol.io/docs/develop/build-server#weather-api-issues)  and shows how the tutorial can be easily leveraged to create other simple MCP servers.

A collection of small security utilities, including tools for parsing Loki IOC logs, configuring host-based IDS, timestomping files, and more.

### Introduction

MCP servers allow Large Language Models (LLMs) to interact with external data sources and APIs.  The MCP protocol facilitates this interaction using a client/server model which abstracts a significant amount of the effort that would typically be involved in running API commands, parsing results, and maintaining scripts.

A good place to start with implementing a new MCP server is by studying the example on [modelcontextprotocol.io](https://modelcontextprotocol.io/docs/develop/build-server#weather-api-issues).  This example uses the National Weather Service (NWS) API to create an MCP server that exposes two tools:  A tool for getting weather advisories given a state, and a tool for getting weather forecasts given a latitude and longitude coordinate pair.

The theory behind the example allows us to extend this functionality to other APIs.  meowfacts-mcp uses the code in the example as a boilerplate starting point to develop a new MCP server which exposes a tool which allows the LLM to return a random cat fact.

### Setup
