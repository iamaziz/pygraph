
Say you have the following relation statements

```raw
Person has Body
Arm partOf Body
Hand partOf Arm
Arm hasPart Hand
Head partOf Body
Ear partOf Head
Eye partOf Head
```

In the file

`dataset/kb-body.csv`

```python
from pygraph import dgraph
```

Create a graph instance

```python
g = dgraph.PyGraph()
```
Read the relation statements from the file

```python
g.file_relations('dataset/kb-body.csv')
```

Here how what it looks like after parsing them:

```python
print(g.graph_dict)
```

     {'Body': [], 
      'Head': [('partOf', 'Body')], 
      'Eye': [('partOf', 'Head')], 
      'Hand': [('partOf', 'Arm')], 
      'Person': [('has', 'Body')], 
      'Ear': [('partOf', 'Head')], 
      'Arm': [('partOf', 'Body'), ('hasPart', 'Hand')]}



Now lets visualize that:

```python
g.draw_graph("ex3")
```


Here we go:

![](img/ex3.png)
