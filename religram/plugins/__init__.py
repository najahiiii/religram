import importlib

from religram import LOAD_PLUGINS, NOLOAD_PLUGINS, log

def __list_all_modules():
    from os.path import dirname, basename, isfile
    import glob
    # This generates a list of modules in this folder for the * in __main__ to work.
    mod_paths = glob.glob(dirname(__file__) + "/*.py")
    all_modules = [basename(f)[:-3] for f in mod_paths if isfile(f)
                   and f.endswith(".py")
                   and not f.endswith('__init__.py')]

    if LOAD_PLUGINS or NOLOAD_PLUGINS:
        to_Load = LOAD_PLUGINS
        if to_Load:
            if not all(any(mod == module_name for module_name in all_modules) for mod in to_Load):
                log.error("Invalid Module name for Plugins!")
                quit(1)

        else:
            to_Load = all_modules

        if NOLOAD_PLUGINS:
            log.info("Plugins No load: {}".format(NOLOAD_PLUGINS))
            return [item for item in to_Load if item not in NOLOAD_PLUGINS]

        return to_Load

    return all_modules


ALL_PLUGINS = sorted(__list_all_modules())
log.info("Plugins loaded: %s", str(ALL_PLUGINS))
__all__ = ALL_PLUGINS + ["ALL_PLUGINS"]
