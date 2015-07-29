import cmd
import core

class Console(cmd.Cmd):

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = '> '
        self.intro  = '\033[1;34mWelcome to Console!\033[1;m'
        self.doc_header = 'Console help (type help <command>):'
        self.ruler = '='
        self.application = core.Application()

    def do_build(self, app_name):
        """Generates code from application/conf.yaml and initializes local Git repo under out/ directory"""

        if app_name:
            if self.application.build(app_name):
                self.prompt = '> '
        else:
            print 'Please specify an app to be built.'

    def do_release(self, app_name):
        """Makes a new application release"""

        # check if app_name was provided
        if app_name:
            self.application.release(app_name)
            self.prompt = '> '
        # release was invoked with no additional param
        else:
            # check if application has been selected previously
            if self.application.name:
                self.application.release(app_name)
            print 'Please specify an application to be released'