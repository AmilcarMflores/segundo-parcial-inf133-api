from database import db

class Tarea(db.Model):
    __tablename__ = "tareas"
    
# id: Identificador único de la tarea. De tipo entero y autoincremental.
# title: Título de la tarea. De tipo cadena de texto.
# description: Descripción de la tarea. De tipo cadena de texto.
# status: Estado de la tarea (pendiente, en curso, completada). De tipo cadena de texto.
# created_at: Fecha de creación de la tarea. De tipo cadena de texto.
# assigned_to: Nombre del usuario asignado a la tarea. De tipo cadena de texto.
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.String(100), nullable=False)
    assigned_to = db.Column(db.String(100), nullable=False)

    def __init__(self,title,description,status,created_at,assigned_to):
        self.title=title
        self.description=description
        self.status=status
        self.created_at=created_at
        self.assigned_to=assigned_to

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Tarea.query.all()

    @staticmethod
    def get_by_id(id):
        return Tarea.query.get(id)
    
    #title,description,status,created_at,assigned_to
    def update(self,title=None,description=None,status=None,created_at=None,assigned_to=None):
        if title is None:
            self.title=title
        if description is None:
            self.description=description
        if status is None:
            self.status=status
        if created_at is None:
            self.created_at=created_at
        if assigned_to is None:
            self.assigned_to=assigned_to
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
        
        

        