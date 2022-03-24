from collections import namedtuple

class Analysis:
    """The Analysis class holds information about an Analysis in
    Stat-Ease 360. Instances of this class are typically created by
    :func:`statease.client.SEClient.get_analysis`.
    """

    def __init__(self, client, name):
        self.client = client
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()

    def predict(self, points, coded=False):
        """ Makes predictions at one or more points."""
        result = self.client.send_payload({
            "method": "POST",
            "uri": "analysis/" + self.name + "/predict",
            "points": points,
            "coded": coded,
        })

        return result['payload']

    def set_model(self, model):
        """ Sets the model used in the analysis. """
        self.client.send_payload({
            "method": "POST",
            "uri": "analysis/" + self.name + "/model",
            "model": model,
        })

    def auto_select(self, initial_model, criterion, method, alpha=None, select_by_degree=False, **kwargs):
        """ Performs an auto-selection on an initial model.

        :param str initial_model: A model to auto-select a subset of terms from.
        :param str criterion: The criterion used to evaluate each sub-model.
                              Valid options are "AICc", "BIC", "pValues",
                              or "AdjRSquared" (case-insensitive).
        :param str method: The method used to select sub-models. Valid options
                           are "Forward", "Backward", "Stepwise", and
                           "AllHierarchical" (case-insensitive).
        :param float alpha: This is the alpha used to either include or exclude
                            terms when using the "pValues" criterion. You can
                            also pass `alpha_in` and/or `alpha_out` to set
                            those values separately (setting both only has an
                            effect when using the "Stepwise" method).
        :param bool select_by_degree: Restricts the sub-model comparisons to
                                      lower order terms before considering
                                      higher order terms.

        :Example:
            >>> result_model = analysis.auto_select('A+B+C+AB+BC+ABC', 'BICc', 'Backward')
            >>> print(result_model)
            >>> "A+B+AB"
        """
        payload = {
            "method": "POST",
            "uri": "analysis/" + self.name + "/autoselect",
            "model": initial_model,
            "criterion": criterion,
            "select_method": method,
            "select_by_degree": select_by_degree,
        }
        if kwargs.get("alpha_in", alpha):
            payload["alpha_in"] = kwargs.get("alpha_in", alpha)
        if kwargs.get("alpha_out", alpha):
            payload["alpha_out"] = kwargs.get("alpha_out", alpha)
        result = self.client.send_payload(payload)

        return result['payload']

    def go_to_node(self, node):
        """ Forces the Stat-Ease 360 GUI to display a particular node. """
        self.client.send_payload({
            "method": "POST",
            "uri": "nodes",
            "node": str(node),
            "analysis": self.name,
        })

    def analyze(self):
        """ Runs the analyses on the selected model. """
        return self.get_anova()

    def get_anova(self):
        """ Retrieves an AnovaResults object for this analysis. """
        return AnovaResults(self.client, self.name)

    def get_diagnostics(self):
        """ Retrieves an DiagnosticsResults object for this analysis. """
        return DiagnosticsResults(self.client, self.name)

class AnovaResults:

    def __init__(self, client, analysis_name):
        self.client = client
        self.analysis_name = analysis_name

        result = self.client.send_payload({
            "method": "GET",
            "uri": "analysis/" + self.analysis_name + "/anova",
        })

        self.terms = []
        for k, v in result['payload'].items():
            if k == 'terms':
                for term_dict in v:
                    term = namedtuple('Term', iter(term_dict.keys()))(**term_dict)
                    self.terms.append(term)
            else:
                setattr(self, k, v)

    def __str__(self):
        return """R2: {r2}
Adj R2: {adjr2}
BIC: {bic}
AICc: {aicc}
Terms: {terms}""".format(
            r2=self.r2,
            adjr2=self.adj_r2,
            bic=self.bic,
            aicc=self.aicc,
            terms=self.terms,
        )

class DiagnosticsResults:

    def __init__(self, client, analysis_name):
        self.client = client
        self.analysis_name = analysis_name

        result = self.client.send_payload({
            "method": "GET",
            "uri": "analysis/" + self.analysis_name + "/diagnostics",
        })

        for k, v in result['payload'].items():
            setattr(self, k, v)

    def __str__(self):
        return """Actual: {actual}

Predicted: {predicted}

Residuals: {residuals}
""".format(
            actual=self.actual,
            predicted=self.predicted,
            residuals=self.residuals,
        )
