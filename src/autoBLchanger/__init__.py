from Components.Language import language
from Tools.Directories import resolveFilename, SCOPE_PLUGINS
from Components.config import config, ConfigSubsection, ConfigSelection, ConfigText
from gettext import gettext, dgettext, bindtextdomain
from os.path import normpath, sep

PluginLanguageDomain = "autoBLchanger"
myPluginPath = resolveFilename(SCOPE_PLUGINS, f"Extensions/{PluginLanguageDomain}")

__version__ = "1.6"

strPluginName = "autoBLchanger"
strVersionIdx = f"v{__version__}"
strSearchPath = normpath(f"{myPluginPath}/logos") + sep


def localeInit():
	bindtextdomain(PluginLanguageDomain, f"{myPluginPath}/locale")


def _(txt):
	t = dgettext(PluginLanguageDomain, txt)
	if t == txt:
		t = gettext(txt)
	return t


localeInit()
language.addCallback(localeInit)
config.plugins.autoBLchanger = ConfigSubsection()
config.plugins.autoBLchanger.changeMode = ConfigSelection(default="man", choices=[("man", _("manual")), ("aut", _("startup"))])
config.plugins.autoBLchanger.selectMode = ConfigSelection(default="0", choices=[("0", _("random")), ("1", _("ascending")), ("2", _("descending"))])
config.plugins.autoBLchanger.logoPath = ConfigText(default=strSearchPath)
