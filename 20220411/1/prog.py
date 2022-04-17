import gettext
translation = gettext.translation('prog', 'po', fallback=True)
_ = translation.gettext
ngettext = translation.ngettext


while (s := input().split()):
    n = len(s)
    print(ngettext("Entered {} word", "Entered {} words", n).format(n))