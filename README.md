# Aiohttp Api

## Setup

```bash
$ docker-compose up -d --build
```

## Test

```bash
$ curl -w "\n" http://localhost:3000
# output: Hello, Anonymous

$ curl -w "\n" http://localhost:3000/yoyea
# output: Hello, yoyea
```
