***A Simple Scrip to find  Mac Vendor from a Mac Address***
***

*How works*:
The script comunicate with ***MacVendors Api***  -> https://api.macvendors.com/

```
~$ curl https://api.macvendors.com/YOURMAC 
```

Can just execute and query for diferent macs or You can put file to extract de mac and another to the output, so the correct usage for the script is like that:

```
~$ python.exe .\MacFinder.py -f exaple.txt -o output.txt
```

In this example the txt have this format:

```
00:07:5f:ae:7f:25
10:4f:58:18:c9:c0
48:ea:63:24:98:bd

```

So the output looks like:

```
[00:07:5f:ae:7f:25] - VCS Video Communication Systems AG
[10:4f:58:18:c9:c0] - Aruba, a Hewlett Packard Enterprise Company
[48:ea:63:24:98:bd] - Zhejiang Uniview Technologies Co., Ltd.
```
