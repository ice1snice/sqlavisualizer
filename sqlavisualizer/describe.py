from sqlalchemy.orm import class_mapper

from sqlalchemy.sql.elements import Label

from sqlavisualizer.dot_templates import CLASS_TEMPLATE, COLUMN_TEMPLATE, \
    RELATION_TEMPLATE, INIT_TEMPLATE


class ModelRepresentation:
    class_name = ''
    columns = []
    table_name = ''

    def __init__(self, model):
        mapper = class_mapper(model)
        self.class_name = mapper.class_.__name__
        self.columns = mapper.columns
        self.table_name = model.__tablename__

    def to_repr(self):
        model_repr = {
            'name': self.class_name,
            'cols': [(self._column_type(col), name, self._column_role(col), )
                     for name, col in self.columns.items()
                     if not isinstance(col, Label)],
        }
        return model_repr

    def _column_type(self, column):
        return str(column.type)

    def _column_role(self, column):
        if column.primary_key:
            return 'pk'
        elif column.foreign_keys:
            return 'fk'


class DBRepresentation:
    models_representations = []
    models_simplified = []
    models_relations = []

    def __init__(self, models):
        for model in set(models):
            self.models_representations.append(ModelRepresentation(model))
        self._create_db_representation()

    def _create_db_representation(self):
        for model_repr in self.models_representations:
            self.models_simplified.append(model_repr.to_repr())

            for col in model_repr.columns:
                for fk in col.foreign_keys:
                    table = fk.column.table
                    for m in self.models_representations:
                        try:
                            if str(table) == str(m.table_name):
                                self.models_relations.append({
                                    'from': model_repr.class_name,
                                    'by': '{}:{}'.format(
                                        col.name, fk.target_fullname.split('.')[-1]),
                                    'to': m.class_name,
                                })
                        except AttributeError:
                            pass

    def to_dot(self):
        classes, relations = self.models_simplified, self.models_relations

        result = [INIT_TEMPLATE]

        for cls in classes:
            cols = ' '.join([
                COLUMN_TEMPLATE % {
                    'type': c[0],
                    'name': c[1]
                } for c in map(self._format_column, cls['cols'])
            ])
            rendered = CLASS_TEMPLATE % {
                'name': cls['name'],
                'cols': cols,
            }
            result.append(rendered)

        for item in relations:
            result.append(RELATION_TEMPLATE % item)

        result.append('}')

        return '\n'.join(result)

    def _format_column(self, column):
        col_type, name, role = column
        role_char = {
            'pk': u'\U00002605',
            'fk': u'\U00002606',
        }.get(role, u'\U000026AA')

        return col_type, '%s %s' % (role_char, name)
    