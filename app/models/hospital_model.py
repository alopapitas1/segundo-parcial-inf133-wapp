from database import db

class Hospital(db.Model):
    __tablename__="hospital"
    
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100),nullable=False)
    lastname=db.Column(db.String(100),nullable=False)
    ci=db.Column(db.String(100),nullable=False)
    birthday=db.Column(db.String(100),nullable=False)
    
    def __init__(self,name,lastname,ci,birtday):
        self.name=name
        self.lastname=lastname
        self.ci=ci
        self.birthday=birtday
        
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        
    @staticmethod
    def get_all():
        return Hospital.query.all()
    
    @staticmethod
    def get_by_id(id):
        return Hospital.query.get(id)
        
    def update(self, name=None,lastname=None,ci=None,birtday=None):
        if name is not None:
            self.name=name
        if lastname is not None:
            self.lastname=lastname
        if ci is not None:
            self.ci=ci
        if birtday is not None:
            self.birthday=birtday