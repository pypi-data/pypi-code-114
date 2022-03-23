from .WOE import WOE, pd

class Distance(WOE):
    """

    """
    def __init__(self, variables, target, bins, fill_pos=False):
        """

        :param variables:
        :param target:
        :param bins:
        :param fill_pos:
        """
        super(Distance, self).__init__(variables, target, bins, fill_pos=fill_pos)

    def WoeIV(self, ):
        """

        :param return: woe [DataFrame], iv[float]
        """
        Bucket = pd.DataFrame({
            'variables': self.variables,
            'target': self.target,
            'Bucket': pd.cut(self.variables, self.bins, include_lowest=True, duplicates='drop')
        }).groupby('Bucket', as_index=True)
        self.woe_iv_res(Bucket)
        return self.res

