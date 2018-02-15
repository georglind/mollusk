# mollusk
Python library for parsing mol-files and drawing molecular skeleton/stick figures with matplotlib

## Simple usage

```python
from mollusk.mol import skeleton
import matplotlib.pyplot as plt

fig, ax = matplotlib.figure(figsize=8,6)
molfile = 'path/to/your/molfile.mol'

skeleton.draw_mol(fig, ax, molfile)

plt.show()
```
