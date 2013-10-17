from flask.ext.script import Command, Option
from myapp.models import db, Things, User

class AdminUser(Command):
    "add admin user"

    def run(self):
        user = User("admin", "password")
        db.session.add(user)
        db.session.commit()

class AddUser(Command):
    "add a user"

    def get_options(self):
        return [
            Option('-n', '--name', dest='name'),
            Option('-p', '--password', dest='password'),
            Option('-r', '--role', dest='0 for user, 1 for admin', default=0)
        ]

    def run(self, name, password, role):
        if not name or not password:
            print "missing name or password"
            return
        user = User(name, password)
        if role:
            role = int(role)
            if role not in [0, 1]:
                print "role must be 0 or 1"
                return
            user.role = role

        db.session.add(user)
        db.session.commit()

