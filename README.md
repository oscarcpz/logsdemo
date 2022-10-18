# logsdemo

## Config project

### Conda

~~~
$ conda create -n logsdemo python=3.10
$ conda activate logsdemo
$ pip install -r requirements.txt
~~~

## Execution

The program takes two arguments:
1. seconds (int) - delay in seconds between log traces
2. number of log traces (int) - total number of log traces to be written
~~~
$ python main.py 5 100000
~~~

## References

* [Miniconda](https://docs.conda.io/en/latest/miniconda.html)
* [Faker](https://faker.readthedocs.io/en/master/)
* [loguru](https://github.com/Delgan/loguru)