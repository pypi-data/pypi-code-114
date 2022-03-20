"""Utilities related to themes supported by each service."""

import enum

from .services import Service


class Theme(enum.Enum):
    A11Y_DARK = "a11y-dark"
    BASE_16_DARK = "base16-dark"
    BASE_16_LIGHT = "base16-light"
    BLACKBOARD = "blackboard"
    COBALT = "cobalt"
    DARCULA = "darcula"
    DARK_PLUS = "dark-plus"
    DRACULA = "dracula"
    DRACULA_PRO = "dracula-pro"
    DRACULA_SOFT = "dracula-soft"
    DUOTONE = "duotone"
    GITHUB_DARK = "github-dark"
    GITHUB_DARK_DIMMED = "github-dark-dimmed"
    HOPSCOTCH = "hopscotch"
    LUCARIO = "lucario"
    LUCARIO_CUSTOM = "lucario-custom"
    MATERIAL = "material"
    MATERIAL_DARKER = "material-darker"
    MATERIAL_DEEP_OCEAN = "material-deep-ocean"
    MATERIAL_DEFAULT = "material-default"
    MATERIAL_OCEAN = "material-ocean"
    MATERIAL_PALENIGHT = "material-palenight"
    MAYUKAI_SUNSET = "mayukai-sunset"
    MIN_DARK = "min-dark"
    MONOKAI = "monokai"
    NIGHTOWL = "nightowl"
    NIGHT_OWL = "night-owl"
    NORD = "nord"
    OCEANIC_NEXT = "oceanic-next"
    ONE_DARK = "one-dark"
    ONE_DARK_PRO = "one-dark-pro"
    ONE_LIGHT = "one-light"
    PANDA = "panda"
    PANDA_SYNTAX = "panda-syntax"
    PARAISO = "paraiso"
    POIMANDRES = "poimandres"
    ROUGE = "rouge"
    SETI = "seti"
    SHADES_OF_PURPLE_ = "shades-of-purple"
    SLACK_DARK = "slack-dark"
    SOLARIZED_DARK = "solarized-dark"
    SOLARIZED_LIGHT = "solarized-light"
    SUBLIME_OCEANIC = "sublime-oceanic"
    SYNTHWAVE_84 = "synthwave84"
    TWILIGHT = "twilight"
    VERMINAL = "verminal"
    VITESSE_DARK = "vitesse-dark"
    VSCODE = "vscode"
    YETI = "yeti"
    ZENBURN = "zenburn"
    _3024_NIGHT = "3024-night"


THEMES = {
    Service.CARBON: [
        Theme._3024_NIGHT,
        Theme.A11Y_DARK,
        Theme.BLACKBOARD,
        Theme.BASE_16_DARK,
        Theme.BASE_16_LIGHT,
        Theme.COBALT,
        Theme.DRACULA_PRO,
        Theme.DUOTONE,
        Theme.HOPSCOTCH,
        Theme.LUCARIO,
        Theme.MATERIAL,
        Theme.MONOKAI,
        Theme.NIGHT_OWL,
        Theme.NORD,
        Theme.OCEANIC_NEXT,
        Theme.ONE_LIGHT,
        Theme.ONE_DARK,
        Theme.PANDA,
        Theme.PARAISO,
        Theme.SETI,
        Theme.SHADES_OF_PURPLE_,
        Theme.SOLARIZED_DARK,
        Theme.SOLARIZED_LIGHT,
        Theme.SYNTHWAVE_84,
        Theme.TWILIGHT,
        Theme.VERMINAL,
        Theme.VSCODE,
        Theme.YETI,
        Theme.ZENBURN,
    ],
    Service.SNAPPIFY: [
        Theme.DARK_PLUS,
        Theme.DARCULA,
        Theme.DRACULA_SOFT,
        Theme.DRACULA,
        Theme.GITHUB_DARK_DIMMED,
        Theme.GITHUB_DARK,
        Theme.LUCARIO,
        Theme.LUCARIO_CUSTOM,
        Theme.MATERIAL_DARKER,
        Theme.MATERIAL_DEFAULT,
        Theme.MATERIAL_DEEP_OCEAN,
        Theme.MATERIAL_OCEAN,
        Theme.MATERIAL_PALENIGHT,
        Theme.MAYUKAI_SUNSET,
        Theme.MIN_DARK,
        Theme.MONOKAI,
        Theme.NIGHTOWL,
        Theme.NORD,
        Theme.ONE_DARK_PRO,
        Theme.PANDA_SYNTAX,
        Theme.POIMANDRES,
        Theme.ROUGE,
        Theme.SLACK_DARK,
        Theme.SOLARIZED_DARK,
        Theme.SUBLIME_OCEANIC,
        Theme.VITESSE_DARK,
    ],
}
