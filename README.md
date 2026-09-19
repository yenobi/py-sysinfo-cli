# Py-sysinfo-cli

Non-production linux system information CLI written in Python to practice language skills

## What is this repo?

Here you can find the cli tool written in Python in order to practice language skills and some work with Linux.
`py-sysinfo-cli` is the tool to provide snapshot of the system's current status.

You are welcome to create issues with recommendations, propositions or to point me to any errors that i have made.

### How to use

### How to run tests

## Feature list

```C
struct sysinfo {
    long uptime;             /* Seconds since boot */
    unsigned long loads[3];  /* 1, 5, and 15 minute load averages */
    unsigned long totalram;  /* Total usable main memory size */
    unsigned long freeram;   /* Available memory size */
    unsigned long sharedram; /* Amount of shared memory */
    unsigned long bufferram; /* Memory used by buffers */
    unsigned long totalswap; /* Total swap space size */
    unsigned long freeswap;  /* swap space still available */
    unsigned short procs;    /* Number of current processes */
    unsigned long totalhigh; /* Total high memory size */
    unsigned long freehigh;  /* Available high memory size */
    unsigned int mem_unit;   /* Memory unit size in bytes */
    char _f[20-2*sizeof(long)-sizeof(int)]; /* Padding for libc5 */
};
```

System name + uptime
`uptime` indicates the number of seconds since the system was last booted.

// TODO: think about any recommendations based on this
// This information is useful for monitoring the system's stability and determining when maintenance or reboots are necessary.

Memory section -> total ram, free ram, shared ram, buffer ram, total swap, free swap -> make it understandable and may be some additional process lookup for future (case: i see that ram is full, i want recommendations what to close based on large size or inactive window for an hour)

Human-readable load average -> The load average represents the average number of processes that are either in the running state or waiting to be run. A high load average may indicate that the system is under heavy load and may require additional resources.

// this is not sysinfo per se, but i want to add

CPU section -> model, usage, temp

Disk section -> total, occupied

Network -> ?
// what can i provide here?
// status of all wireless communications?

--

working `--help` command -> also part of usable documentation instead of `README.md`. Here i will gather more of non-API things or thoughts

`-v` and `--verbose` -> any feature will be more useful with this?

--

interactive mode -> work with user confirmations and input, `-i` and `--interactive`

--

After output to the terminal, think about output to json for example

## Dev notes

This is the section with reasoning about tools, that i have choosen or some thoughts for myself what to experiment with instead.

// TODO: write brief explanation what is uv here and why i choose it for project and package management

### Process methodology

Draft of feature in `README.md` as human-readable text -> tests -> minimal code -> polish code -> polish doc.


## Useful links
