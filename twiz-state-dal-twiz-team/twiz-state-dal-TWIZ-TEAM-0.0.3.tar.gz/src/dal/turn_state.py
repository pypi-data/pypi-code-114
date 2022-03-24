
from enum import Enum
from twiz_cobot.custom_libraries.twiz_state_dal.src.dal.twiz_state_manager import TwizStateManager


class StateType(Enum):
    PREV = 'last_state'
    CURR = 'current_state'


class TurnState:
    state_manager: TwizStateManager
    state_type: StateType

    def __init__(self, state_manager: TwizStateManager, state_type: StateType = StateType.CURR):
        self.state_manager = state_manager
        self.state_type = state_type

    @property
    def state(self) -> dict:
        if self.state_type == StateType.PREV:
            return self.state_manager.last_state
        elif self.state_type == StateType.CURR:
            return self.state_manager.current_state
        else:
            raise Exception("Unrecognized State")

    @property
    def text(self) -> str:
        return self.state.get('text', None) if self.state else None

    def set_text(self, text: str = None):
        self.state_manager.write_state_attribute('text', text)

    @property
    def intent(self) -> str:
        return self.state.get('intent', None) if self.state else None

    def set_intent(self, intent: str = None):
        self.state_manager.write_state_attribute('intent', intent)

    @property
    def apl_screen(self) -> str:
        return self.state.get('apl_screen', None) if self.state else None

    def set_apl_screen(self, apl_screen: str = None):
        self.state_manager.write_state_attribute('apl_screen', apl_screen)

    # ----- variables which can only be read, not set ----- #
    @property
    def is_apl_supported(self) -> bool:
        supported_interfaces = self.state.get('supported_interfaces', None) if self.state else None
        if supported_interfaces:
            return supported_interfaces.get('apl', False)
        else:
            return False
