Introduction
---
This is the simple implementation of huge orders searching on **Binance** in order books through pairs. Working with WebSockets.\
Especially thanks Oliver Zehentleitner for [unicorn-binance-websocket-api](https://github.com/oliver-zehentleitner/unicorn-binance-websocket-api).
\

How to use
---
1. Clone the repo
2. Insert your presets into config.ini. Pairs, Quotes *(comma separated)*
> **Notice** if you will add only "exact_pairs" without adding quotes - only exact pairs will be used.

> **But**! You can define exact quotes, and add pairs from other quotes. \
> If pairs and Quotes will be empty, you will receive data from all pairs list (1024 streaming limitation, according to the limits).

> volume_multiplicator - is used to multiply median value in the order book. Simple, stupid but so 🤷‍♂️
3. Just build and run **dockerfile**
```bash
docker build -t orders_searcher .
docker run orders_searcher
```
\
Not able and in future will fix:
---
1. Identify is order unique or not. Binance is not sending uid of the order.
2. Tons of noize as a result of the way how it identifies order size. And the median of 20 last orders is nothing. Hope to have time to commit version with price assessment.
3. Custom filters to define pairs. According to the 1h, 24h, 7d volume, high_liquidity, and others (Already done, in future will add).
4. Create temp storage to migrate data from this connector to other microservices.

