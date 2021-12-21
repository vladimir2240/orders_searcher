Introduction
---
This is the simple implementation of huge orders searching on **Binance** in order books through pairs (Like independent service). Working with WebSockets. Sending results to Kafka.

\
Main goal
--
To show the way of working in creating the structure, working with classes and transferring data to message broker.

\
How it works:
---
1. Firstly we are taking user presets from config.ini
2. Filtering list of tickers by user rules
3. Creating streams to each ticker
4. Analysing it by simple logic
5. Sending result to Kafka

To check the results I created kafka_consumer.py. **REMINDER**: never store variables in code:) It's just the testing file to visualize that everything is working. Use env variable for *'localhost:9092'*.

\
Used solutions:
---
1. [unicorn-binance-websocket-api](https://github.com/oliver-zehentleitner/unicorn-binance-websocket-api)
2. [kafka-docker](https://github.com/wurstmeister/kafka-docker)

\
How to use
---
1. Clone the repo
2. Insert your presets into config.ini. Pairs, Quotes *(comma separated)*
> **Notice** if you will add only "exact_pairs" without adding quotes - only exact pairs will be used.

> **But**! You can define exact quotes, and add pairs from other quotes. \
> If pairs and Quotes will be empty, you will receive data from all pairs list (1024 streaming limitation, according to the limits).

> volume_multiplicator - is used to multiply median value in the order book. Simple, stupid but so 🤷‍♂️

3.1. Just run `docker-compose` inside directory
```bash
docker-compose up
```
4. After the successful start of the containers, to check producer/consumer run `kafka_consumer.py`
```bash
python3 kafka_consumer.py
```

\
TODO
---
1. Identify is order unique or not. Binance is not sending uid of the order.
2. Tons of noize as a result of the way how it identifies order size. And the median of 20 last orders is nothing. Hope to have time to commit version with price assessment.
3. Custom filters to define pairs. According to the 1h, 24h, 7d volume, high_liquidity, and others (Already done, in future will add).
4. Migrate analysis logic from this service to consumer service side.

