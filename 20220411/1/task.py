import gettext

entered = len(input().split())
translation = gettext.translation('task', 'po', fallback=True)
_, ngettext = translation.gettext, translation.ngettext
print(ngettext('Entered {} word', 'Entered {} words', entered).format(entered))
