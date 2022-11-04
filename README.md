# deephaven-matplotlib-base


This repository integrates [Deephaven](https://deephaven.io/) with [matplotlib](https://matplotlib.org/), a plotting library for the [Python](https://www.python.org/) programming language.

First, make sure you have all the needed dependencies to [Launch Deephaven from pre-built images](https://deephaven.io/core/docs/tutorials/quickstart/).

To clone this repo and get started, run:

```
git clone https://github.com/deephaven-examples/deephaven-matplotlib-base.git
cd deephaven-matplotlib-base
docker compose pull
docker compose up --build -d
```

This starts the Deephaven IDE with all the needed packages.

Navigate to [http://localhost:10000/ide](http://localhost:10000/ide) to enter your matplotlib query:

```python
import matplotlib.pyplot as plt

plt.figure()
x = [0, 2, 4, 6]
y = [1, 3, 4, 8]
plt.plot(x, y)
plt.xlabel('x values')
plt.ylabel('y values')
plt.title('plotted x and y values')
plt.legend(['line 1'])

m_figure=plt.gcf()
```

Your new plot will appear in the IDE!

The 3D examples in this readme are from [Rashida Nasrin Sucky](https://towardsdatascience.com/five-advanced-plots-in-python-matplotlib-134bfdaeeb86) the data is available from [kaggle](https://www.kaggle.com/fazilbtopal/auto85)
