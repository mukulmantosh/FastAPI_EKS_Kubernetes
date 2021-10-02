# FastAPI with Kubernetes

![stack](./docs/images/stack.png)


Welcome to the FastAPI & Kubernetes Tutorial Series with PyCharm & AWS EKS.

## Prerequisites 

Before starting up this project, make sure you have an AWS account and 
PyCharm installed in your machine.

* In this tutorial we will be using [PyCharm Professional](https://www.jetbrains.com/pycharm/).


### Software Installation

- [x] [AWS Command Line Interface](https://aws.amazon.com/cli/) - The AWS Command Line Interface (CLI) is a unified tool to manage your AWS services.


- [x] [eksctl](https://eksctl.io/) - The official CLI for Amazon EKS


- [x] [Docker](https://www.docker.com/) - Docker helps developers bring their ideas to life by conquering the complexity of app development.


- [x] [Kubernetes](https://kubernetes.io/) - also known as K8s, is an 
 open-source system for automating deployment, scaling, and management of containerized applications.


- [x] [Helm](https://helm.sh/) - The package manager for Kubernetes. Helm helps you manage 
Kubernetes applications — Helm Charts help you define, install, and upgrade even the most complex Kubernetes application.


- [x] [PostgreSQL](https://www.postgresql.org/) - The World's Most Advanced Open Source Relational Database


- [x] [Redis](https://redis.io/) - open source (BSD licensed), in-memory data structure store, used as a database, cache, and message broker


- [x] [NICE DCV](https://www.nice-dcv.com/) (Optional) - Deliver high-performance remote desktop and application streaming. If 
you are interested to run your workload directly in AWS.

## System Dependencies

- Make sure your system is up-to-date.
- Run the below command to install python system 
dependencies along-with postgres driver.

```bash

$ sudo apt-get install libpq-dev python-dev libssl-dev

```



## Python Dependencies

- Installing Python Packages

```bash

$ pip install -r requirements.txt

```

![requirements-install](./docs/images/requirements.gif)

- Running Uvicorn Server

```bash

$ uvicorn main:app --reload

```

## Environment

Make sure to update the environment variables in **ecommerce/config.py**, before starting up the project.


![config-file](./docs/images/env_file.png)



## Celery

Make sure before starting up Celery, redis is up and running.

Command to start celery worker :

```bash
$ celery -A main.celery worker -l info
```
or with execution pool
```bash
$ celery -A main.celery worker -l info --pool=prefork
```

Reference Materials:
* [Celery Execution Pools: What is it all about?](https://www.distributedpython.com/2018/10/26/celery-execution-pool/)
* [A complete guide to production-ready Celery configuration](https://medium.com/koko-networks/a-complete-guide-to-production-ready-celery-configuration-5777780b3166)
* [Eliminating Task Processing Outages by Replacing RabbitMQ with Apache Kafka Without Downtime](https://doordash.engineering/2020/09/03/eliminating-task-processing-outages-with-kafka/)


![celery-task](./docs/images/celery-task.png)

## Testing

Before proceeding make sure you have created a test database in Postgres.

![python-testing](./docs/images/testing.gif)



## References

If you are interested to know more about AWS with Python, then you can follow the below links.

- [Developing Serverless APIs using AWS Toolkit](https://www.jetbrains.com/pycharm/guide/tutorials/intro-aws/)
- [Developing Django Application using AWS](https://www.jetbrains.com/pycharm/guide/tutorials/django-aws/) 
