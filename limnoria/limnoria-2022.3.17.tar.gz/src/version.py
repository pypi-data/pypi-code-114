version = '2022.03.17'
try: # For import from setup.py
    import supybot.utils.python
    supybot.utils.python._debug_software_version = version
except ImportError:
    pass
