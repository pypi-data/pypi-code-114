from typing import List, Union
from ._template_matcher import TemplateMatcher
from ._feature_matcher import FeatureMatcher
from ._results import MatchingResult


class GenericMatcher(TemplateMatcher):
    def __init__(self, *args, strict_mode: bool = False, **kwargs):

        super().__init__(*args, **kwargs)
        self.strict_mode = strict_mode

    def find_all_results(self) -> List[MatchingResult]:
        results = super().find_all_results()
        if self.strict_mode or results:
            # strict mode will only use template matching
            return results
        else:
            feature_matcher = FeatureMatcher(
                self.image_path, self.template_path, self.convert_2_gray
            )
            return feature_matcher.find_all_results()

    def find_best_result(self) -> Union[MatchingResult, None]:
        result = super().find_best_result()
        if self.strict_mode or result is not None:
            # strict mode will only use template matching
            return result
        else:
            feature_matcher = FeatureMatcher(
                self.image_path, self.template_path, self.convert_2_gray
            )
            return feature_matcher.find_best_result()
