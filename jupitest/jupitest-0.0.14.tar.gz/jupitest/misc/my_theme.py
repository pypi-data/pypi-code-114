import tkstyle
from cyberpunk_theme import Cyberpunk
from cyberpunk_theme import constant
from cyberpunk_theme.widget import label, button, frame
from cyberpunk_theme.megawidget import tree


# ========================================
# RUNTEST THEME BASED ON CYBERPUNK THEME
# ========================================
def get_theme():
    theme = Cyberpunk()
    theme.add(_get_tree_titlebar_style(), pattern="*Tree*")
    theme.add(_get_tree_expander_button_style(),
              pattern="*Tree*treeExpanderButton")
    theme.add(_get_tree_title_one_label_style(),
              pattern="*Tree*treeTitleLabelOne")
    theme.add(_get_tree_title_two_label_style(),
              pattern="*Tree*treeTitleLabelTwo")
    theme.add(_get_toolbar_body_style(),
                    pattern="*runtestToolbar*")
    theme.add(_get_toolbar_label_testing_passed_style(),
                    pattern="*runtestToolbar*labelTestingPassed")
    theme.add(_get_toolbar_label_testing_failed_style(),
                    pattern="*runtestToolbar*labelTestingFailed")
    theme.add(_get_toolbar_button_run(),
                    pattern="*runtestToolbar*buttonRun")
    theme.add(_get_toolbar_button_rerun(),
                    pattern="*runtestToolbar*buttonRerun")
    theme.add(_get_toolbar_button_stop(),
                    pattern="*runtestToolbar*buttonStop")
    theme.add(_get_toolbar_button_cancel(),
                    pattern="*runtestToolbar*buttonCancel")
    theme.add(_get_toolbar_button_clean(),
                    pattern="*runtestToolbar*buttonClean")
    theme.add(_get_toolbar_button_log(),
                    pattern="*runtestToolbar*buttonLog")
    
    theme.add(_get_log_window_text_style(), pattern="*Text")

    return theme


# ========================================
#                   TREE
# ========================================

# titlebar
def _get_tree_titlebar_style():
    style = tree.get_style()
    style.background = constant.BACKGROUND_COLOR
    return style


# expander button
def _get_tree_expander_button_style():
    style = tkstyle.Button()
    style.font = (constant.FONT_FAMILY, constant.FONT_SIZE, "bold")
    style.background = constant.BACKGROUND_COLOR
    style.foreground = "gray"
    style.activeForeground = constant.BACKGROUND_COLOR
    style.highlightThickness = 0
    style.borderWidth = 0
    style.activeBackground = "#F0F8FF"
    style.padX = 3
    style.padY = 1
    return style


# title_one label
def _get_tree_title_one_label_style():
    style = tkstyle.Label()
    style.font = (constant.FONT_FAMILY, constant.FONT_SIZE, "bold")
    style.background = constant.BACKGROUND_COLOR
    style.foreground = "gray"
    return style


# title_two label
def _get_tree_title_two_label_style():
    style = tkstyle.Label()
    style.font = (constant.FONT_FAMILY, constant.FONT_SIZE, "bold")
    style.background = constant.BACKGROUND_COLOR
    style.foreground = "#CFCFCF"
    return style


# ========================================
#            TOOLBAR
# ========================================

# toolbar body
def _get_toolbar_body_style():
    style = frame.get_style()
    style.background = "#002323"
    return style


# label testing passed
def _get_toolbar_label_testing_passed_style():
    style = label.get_style()
    style.foreground = "#40A640"
    style.background = "#002323"
    return style


# label testing failed
def _get_toolbar_label_testing_failed_style():
    style = label.get_style()
    style.foreground = "#F73030"
    style.background = "#002323"
    return style


# button run
def _get_toolbar_button_run():
    style = button.get_style()
    style.background = "#004600"
    style.foreground = "white"
    style.activeBackground = "#006600"
    style.activeForeground = "white"
    style.highlightBackground = "white"
    style.highlightColor = "white"
    return style


# button rerun
def _get_toolbar_button_rerun():
    style = _get_toolbar_button_run()
    return style


# button stop
def _get_toolbar_button_stop():
    style = _get_toolbar_button_run()
    style.background = "#CF0000"
    style.activeBackground = "#FF0000"
    return style


# button cancel
def _get_toolbar_button_cancel():
    style = _get_toolbar_button_run()
    style.background = "#BF2600"
    style.activeBackground = "#D73E18"
    return style


# button clean
def _get_toolbar_button_clean():
    style = _get_toolbar_button_run()
    style.background = constant.BACKGROUND_COLOR
    style.activeBackground = "#FF0000"
    style.foreground = "gray"
    style.borderWidth = 0
    style.highlightThickness = 0
    return style


# button log
def _get_toolbar_button_log():
    style = _get_toolbar_button_run()
    style.background = "#003366"
    style.activeBackground = "#204B7E"
    return style


# ========================================
#               LOG WINDOW
# ========================================


# log window
def _get_log_window_text_style():
    style = tkstyle.Text()
    style.font = constant.FONT_FAMILY, 15, "normal"
    style.background = "#033669"
    style.foreground = "#7EB1B1"
    style.highlightThickness = 0
    return style
