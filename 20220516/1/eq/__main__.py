from . import eq
import locale
import gettext
import pyfiglet

locale.setlocale(locale.LC_ALL, locale.getlocale())
translation = gettext.translation('eq', 'po')
_ = translation.gettext


def main():
    figlet = pyfiglet.Figlet('graceful')
    
    a, b = [int(i) for i in input().split()]

    solution = eq(a, b)
    if solution is None:
        s = _("NO ROOTS")
        print(figlet.renderText(s))
    else:
        s = _("Root: {}").format(solution)
        print(figlet.renderText(s))


if __name__ == "__main__":
    main()
