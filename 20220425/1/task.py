import pyfiglet
import gettext
translation = gettext.translation('task', 'task', fallback=True)
_, ngettext = translation.gettext, translation.ngettext

def solve(a, b):
    return -b / a if a != 0 else None


if __name__ == '__main__':
    root = solve(int(input(_('Enter a: '))), int(input(_('Enter b: '))))
    print(pyfiglet.Figlet(font='graceful').renderText(_('Root: {}').format(root) if root is not None else _('NO ROOTS')))
