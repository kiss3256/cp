import thread6


class Manager(object):
    def __init__(self):
        self.userEntities = []

    def add_user(self, user):
        self.userEntities.append(user)

    def run(self):
        for user in self.userEntities:
            if user.status == 'online':
                thread6.run_threaded(user.run, ['simulate_1'])
