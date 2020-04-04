# tcp_bandwidth
Autonomous activity for the class of Computer Networks 2019/2 at UFRGS.

Program to analyze the fairness of multiple TCP connections.

# Installation

```
pip install matplotlib numpy
```


# Usage

The `coordinator.py` program coordinates the connection between clients and servers. The number of parallel clients and servers can be passed to the program by command line arguments, as well as the starting listening port to be used. Each server will use an additional port, so if we use the below command, ports 13000 through 13005 will be used.

```
cd src && ./coordinator.py --port 13000 -c 5 -s 6 
```

Arguments:
- `--clients/-c` : number of parallel clients
- `--servers/-s` :  number of parallel servers
- `--port/-p` : starting listening port number

This command outputs a file summarizing the connection bandwidth throughout the test execution. This output file may be used with the `graph.py` program to produce an animated GIF of the connection bandwidth vs time. The graph program accepts a list of output files, separated by spaces, so it can plot a graph line for each output file / connection configuration provided. Sample output GIFs are provided in the `./results` folder.

```
cd src && ./graph.py -f <FILE_NAME>
```

