from openwebpos.extensions import db


class SQLMixin(object):

    def save(self):
        """
        Save model instance.
        :return: model instance
        """
        db.session.add(self)
        db.session.commit()
        return self

    def delete(self):
        """
        Delete model instance
        :return: db.session.commit()'s result
        """
        db.session.delete(self)
        return db.session.commit()
