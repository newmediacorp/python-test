import time

class Application():

    def __init__(self):
        self.name = None
        self.path = None

    def build(self, app_name):
        # TODO generate code from my-app/conf.yaml
        print 'Code generation completed'

        # TODO create local Git repo
        print 'Local Git repo is initialised in out/ directory'

    def release(self, app_name):
        self.name = app_name
        self.path = 'out/' + app_name

        # TODO create Tag in local Git repo
        print 'Creating a Tag in local Git repo...'
        # out/ directory is
        time.sleep(2)
        print 'Performing Origin push.'
        time.sleep(2)
        print 'Making a release...'
        #
        time.sleep(2)
        print 'SUCCESS: ' + self.name + '-0.1.3 was released. Please use deploy app-name environment to deploy the app.'