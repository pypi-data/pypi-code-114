
from typing import List
from twiz_cobot.custom_libraries.twiz_state_dal.src.state_access.twiz_state_manager import TwizStateManager


class UserState:
    state_manager: TwizStateManager

    def __init__(self, state_manager: TwizStateManager):
        self.state_manager = state_manager

    @property
    def started_task(self) -> bool:
        _user_attributes = self.state_manager.user_attributes
        return _user_attributes.get('started_task', None)

    def set_started_task(self, started_task: str = None):
        """
        Returns the updated items
        """
        # TODO - IDK the return type
        _user_attributes = self.state_manager.user_attributes
        _user_attributes['started_task'] = started_task
        return self.state_manager.write_user_attributes(_user_attributes)

    @property
    def current_task(self) -> str:
        _user_attributes = self.state_manager.user_attributes
        return _user_attributes.get('current_task', None)

    def set_current_task(self, current_task: str = None):
        """
        Returns the updated items
        """
        # TODO - IDK the return type
        _user_attributes = self.state_manager.user_attributes
        _user_attributes['current_task'] = current_task
        return self.state_manager.write_user_attributes(_user_attributes)

    @property
    def current_query_result_index(self) -> int:
        _user_attributes = self.state_manager.user_attributes
        return _user_attributes.get('current_query_result_index', None)

    def set_current_query_result_index(self, current_query_result_index: str = None):
        """
        Returns the updated items
        """
        # TODO - IDK the return type
        _user_attributes = self.state_manager.user_attributes
        _user_attributes['current_query_result_index'] = current_query_result_index
        return self.state_manager.write_user_attributes(_user_attributes)

    @property
    def apl_screens(self) -> List:
        _user_attributes = self.state_manager.user_attributes
        return _user_attributes.get('apl_screens', None)

    def set_apl_screens(self, apl_screens: str = None):
        """
        Returns the updated items
        """
        # TODO - IDK the return type
        _user_attributes = self.state_manager.user_attributes
        _user_attributes['apl_screens'] = apl_screens
        return self.state_manager.write_user_attributes(_user_attributes)
