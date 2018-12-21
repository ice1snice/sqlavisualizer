# sqlavisualizer

# Usage

1. Intall package
```bash
pip install -e .
```

2. Install graphviz
```bash
sudo apt install graphviz
```

3. Create list of all your models, for example:
```python
import your_project.models as models_module
# Model - base class for your models

app_models = []

for model in iter(vars(models_module).values()):
    try:
        if issubclass(model, Model):
            app_models.append(model)
    except TypeError:
        continue
```

4. Import DBRepresentation and create .dot file:
```python
from sqlavisualizer import DBRepresentation

db_repr = DBRepresentation(app_models)
dot_repr = db_repr.to_dot()

with open('db.dot', 'w') as f:
    f.write(dot_repr)
```

5. Convert .dot file to .png with graphviz:
```bash
dot -T png db.dot > db.png
```
