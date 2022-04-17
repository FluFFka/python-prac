import gettext
translation = gettext.translation('prog', 'po', fallback=True)
_ = translation.gettext
ngettext = translation.ngettext

def _(arg):
    return arg


while (s := input().split()):
    print(_("Entered {} words").format(len(s)))