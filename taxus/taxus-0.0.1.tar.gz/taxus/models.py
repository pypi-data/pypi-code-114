from gpytorch.models import ApproximateGP
from gpytorch.variational import (
    CholeskyVariationalDistribution,
    VariationalStrategy,
    UnwhitenedVariationalStrategy,
    IndependentMultitaskVariationalStrategy,
)
from gpytorch.priors import NormalPrior
from gpytorch.kernels import ScaleKernel, RBFKernel
from gpytorch.means import ConstantMean
from gpytorch.mlls import VariationalELBO
from gpytorch.distributions import MultivariateNormal
from patsy import dmatrices, dmatrix
import torch
from torch.optim import Adam
import tqdm
import numpy as np
import pandas as pd


class GP(ApproximateGP):
    def __init__(self, formula, train_df, likelihood):
        train_y_df, train_x_df = dmatrices(formula, train_df,
                                           return_type='dataframe')
        train_x_df = train_x_df.drop('Intercept', axis=1, errors='ignore')
        variational_strategy = self._get_variational_strategy(train_x_df)
        super(GP, self).__init__(variational_strategy)
        self.formula = formula
        self.train_y_df = train_y_df
        self.train_x_df = train_x_df
        self.likelihood = likelihood
        self.mean_module = ConstantMean()
        self.covar_module = ScaleKernel(
            base_kernel=RBFKernel(
                ard_num_dims=self.train_x.size(1),
                lengthscale_prior=NormalPrior(loc=0, scale=1)
            )
        )

    def _get_variational_strategy(self, train_x_df):
        inducing_points = torch.tensor(train_x_df.values, dtype=torch.float32)
        variational_distribution = CholeskyVariationalDistribution(
            num_inducing_points=inducing_points.size(0)
        )
        variational_strategy = UnwhitenedVariationalStrategy(
            self, inducing_points, variational_distribution,
            learn_inducing_locations=False
        )
        return variational_strategy

    @property
    def covariates(self):
        return list(self.train_x_df.columns)

    @property
    def train_y(self):
        return torch.tensor(self.train_y_df.values.T, dtype=torch.float32)

    @property
    def train_x(self):
        return torch.tensor(self.train_x_df.values, dtype=torch.float32)

    def forward(self, x):
        mean_x = self.mean_module(x)
        covar_x = self.covar_module(x)
        latent_pred = MultivariateNormal(mean_x, covar_x)
        return latent_pred

    def fit(self, n_steps=600, lr=0.1, tol=1e-4, n_retries=2,
            show_progress_bar=True):
        """
        ELBO approximates (usually intractable) log marginal likelihood, 
        so can be used for likelihood ratio tests
        """
        self.losses_ = []
        mll = VariationalELBO(self.likelihood, self, self.train_y.size(1))

        optimizer = Adam([
            {'params': self.parameters()},
        ], lr=lr)

        self.train()
        self.initialize(**{
            'covar_module.base_kernel.lengthscale': torch.tensor(
                [2.]*self.train_x.shape[1]),
            'covar_module.outputscale': torch.log(self.train_y.mean()),
            'mean_module.constant': torch.log(self.train_y.mean())
        })

        try:
            with tqdm(total=n_steps, desc='Fitting GP', leave=False,
                      disable=not show_progress_bar) as progress_bar:
                for i in range(n_steps):       
                    optimizer.zero_grad()
                    # Get predictive output
                    output = self(self.train_x)
                    # Calc loss and backprop gradients
                    loss = -mll(output, self.train_y)
                    loss_item = loss.item()
                    self.losses_.append(loss_item)
                    if i > 20 and abs(loss_item - self.losses_[-2]) < tol:
                        return loss_item
                    progress_bar.set_postfix(
                        loss=loss_item,
                    )
                    progress_bar.update()
                    loss.backward()
                    optimizer.step()
            return loss_item
        except Exception:
            if not n_retries:
                return np.nan
            self.fit(n_steps=n_steps, lr=lr, tol=tol, n_retries=n_retries-1,
                     show_progress_bar=show_progress_bar)

    def predict(self, test_x_df, n_likelihood_samples=100,
                n_latent_samples=100,
                percentiles=[0.5, 2.5, 5, 50, 95, 97.5, 99.5]):

        formula_rhs = self.formula.split('~')[1]
        _test_x_df = (
            dmatrix(formula_rhs, test_x_df, return_type='dataframe')
            .drop('Intercept', axis=1, errors='ignore')
        )
        assert not (
            self.train_x_df.columns.difference(_test_x_df.columns).values.size)
        self.eval()

        test_x = torch.tensor(_test_x_df.values, dtype=torch.float32)

        f_pred = self(test_x)
        y_pred = self.likelihood(
            f_pred, sample_shape=torch.Size([n_likelihood_samples, 1])
        )

        model_samples = (
            y_pred.sample([n_latent_samples])
            .reshape(n_latent_samples * n_likelihood_samples,
                     f_pred.mean.size(0))
            .numpy()
        )

        percentiles_pred = np.percentile(model_samples, percentiles, axis=0)

        return pd.DataFrame(
            np.concatenate([
                percentiles_pred.T,
                model_samples.mean(axis=0).reshape(-1, 1),
            ], axis=1),
            columns=[*[f'p{p}' for p in percentiles],'mean']
        )

    def fit_predict(self, test_x_df):
        self.fit()
        return self.predict(test_x_df)


class MultiTaskGP(ApproximateGP):
    def __init__(self, train_x, n_outputs=1):
        inducing_points = torch.unique(train_x, dim=0)
        variational_distribution = CholeskyVariationalDistribution(
            num_inducing_points=inducing_points.size(0),
            batch_shape=torch.Size([n_outputs])
        )
        variational_strategy = IndependentMultitaskVariationalStrategy(
            VariationalStrategy(
                self, inducing_points, variational_distribution,
                learn_inducing_locations=False
            ),
            num_tasks=n_outputs,
            task_dim=-1
        )
        super(MultiTaskGP, self).__init__(variational_strategy)
        self.mean_module = ConstantMean(batch_shape=torch.Size([n_outputs]))
        self.covar_module = (
            ScaleKernel(
                RBFKernel(
                    ard_num_dims=3,
                    lengthscale_prior=NormalPrior(loc=0, scale=1),
                    batch_shape=torch.Size([n_outputs])
                ),
                batch_shape=torch.Size([n_outputs])
            )
            # ScaleKernel(RBFKernel(ard_num_dims=3))
            # ScaleKernel(MaternKernel(nu=0.5, ard_num_dims=3))
        )

    def forward(self, x):
        mean_x = self.mean_module(x)
        covar_x = self.covar_module(x)
        latent_pred = MultivariateNormal(mean_x, covar_x)
        return latent_pred