import inspect


@yui.command('help', 'h')
def help(argv):
    """Returns doc for commands. Usage: help <command>"""
    if len(argv) < 2:
        return 'Usage: help <command>'
    hook = yui.hook_by_cmd(argv[1])
    if hook:
        doc = inspect.getdoc(hook.func)
        if doc:
            return doc

@yui.command('alias', 'al')
def alias(argv):
    """Returns all aliases for a command. Usage: alias <command>"""
    if len(argv) < 2:
        return
    hook = yui.hook_by_cmd(argv[1])
    if hook:
        return 'Aliases for %s: %s' % (hook, ', '.join(hook.cmd))


@yui.command('commands','cmds')
def commands(argv):
    """Lists one alias for every registered command. Usage: commands [search]"""
    cmds = []
    search = None
    if len(argv) > 1:
       search = argv[1]
    for h in yui.get_all_hooks():
        if h.cmd:
            if not search:
                cmds.append(h.cmd[0])
            else:
                for c in h.cmd:
                    if search in c:
                        cmds.append(c)
                        break
    if cmds:
        return ', '.join(cmds)
