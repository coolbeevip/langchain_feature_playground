## Quick Start

Install dependencies

```shell
make init
```

Run

```shell
export OPENAI_API_KEY=<your key>
make run
```

## API

LangChain Agent with Wikipedia and LLM

```curl
curl -X POST -H "Content-Type: application/json" -d '{"question": "现在的美国总统是谁?"}' http://localhost:5000/api/openai/agent
```

LangChain Conversations

```curl
curl -X POST -H "Content-Type: application/json" -d '{"question": "哪个国家获得了2002年世界杯冠军?"}' http://localhost:5000/api/openai/conversation/0001
curl -X POST -H "Content-Type: application/json" -d '{"question": "那届世界杯谁获得了金靴奖?"}' http://localhost:5000/api/openai/conversation/0001
```

LangChain Documents

```curl
curl -X POST -H "Content-Type: application/json" -d '{"question": "现在的美国总统是谁?"}' http://localhost:5000/api/openai/documents
```

Upload File

```curl
curl -X POST -F "file=@tests/fixtures/test.txt" http://localhost:5000/api/upload
```

## References

* [Semantic Search with OpenSearch, Cohere, and FastAPI](https://dylancastillo.co/semantic-search-with-opensearch-cohere-and-fastapi/)
* [Semantic Search with Elasticsearch, OpenAI, and LangChain](https://dylancastillo.co/semantic-search-elasticsearch-openai-langchain/)