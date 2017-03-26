import importlib
import sys
import subprocess

"""
Depresolv is a system that is constructed to prevent
runtime import errors on Windows systems. You provide a
list of deps to depresolv and it resolves them and restarts
the app. Only std dependencies
"""


def getFunctionalPip():

    try:
        subprocess.check_output(["pip"])
        return "pip"
    except BaseException:
        try:
            subprocess.check_output(["pip3"])
            return "pip3"
        except BaseException:
            print("No operational pip intallation found!")
            raise DepresolvFailed("No operational pip intallation found!")

class DependencyResolver():

    dependencies = None
    missing = []
    failed = []

    def config(self, dependencies, modulename):

        print("Resolving dependencies for {}: ".format(modulename) + str(dependencies))
        self.dependencies = dependencies

    def resolve(self):

        for module in self.dependencies:

            print("Resolving {} -- ".format(module), end="")

            try:
                importlib.import_module(module)
                print("OK!")
            except ModuleNotFoundError:

                print("Installing {} -- ".format(module), end="")

                try:
                    subprocess.check_output([getFunctionalPip(), "install", module], stderr=subprocess.STDOUT)
                    print("OK")
                except subprocess.CalledProcessError as e:
                    print("Module install failed for {} with the following output:\n\n{}".format(str(e), e.output.decode("utf-8")))
                    raise DepresolvFailed("Module install failed for {} with the following output:\n\n{}".format(str(e), e.output.decode("utf-8")))

        print("All dependencies satisfied.")

class PIPError(BaseException): pass
class DepresolvMain(BaseException): pass
class DepresolvFailed(BaseException): pass

def launch_main(deps):
    
        print("Resolving runtime dependencies, please wait. "
              "The program should start by itself, if something fails, restart the program.")

        resolver = DependencyResolver()
        resolver.config(deps, "launch_main")
        resolver.resolve()
        print("Launching main...")
        raise DepresolvMain
