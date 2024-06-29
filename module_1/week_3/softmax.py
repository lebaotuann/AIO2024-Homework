# Section 1, Q1
import torch


class Softmax(torch.nn.Module):
    """This class implements a Softmax operation applied to each element across a specific dimension."""

    def __init__(self):
        super().__init__()

    @staticmethod
    def forward(data: torch.Tensor):
        """Applies softmax along the specified dimension.

        Args:
            data (torch.Tensor): The data tensor (1-dimensional)

        Returns:
            torch.Tensor: The output tensor with softmax.
        """
        """"""
        # Recommendation: return torch.nn.functional.softmax(data, dim=0)
        data_exp = torch.exp(data)
        sum_data_exp = data_exp.sum(0, keepdim=True)
        return data_exp / sum_data_exp


class SoftmaxStable(torch.nn.Module):
    """This class implements a Softmax operation applied to each element across a specific dimension."""

    def __init__(self):
        super().__init__()

    @staticmethod
    def forward(data: torch.Tensor):
        """Applies softmax along the specified dimension.

        Args:
            data (torch.Tensor): The data tensor (1-dimensional)

        Returns:
            torch.Tensor: The output tensor with softmax.
        """
        data_max = torch.max(data, dim=0, keepdim=True)
        data_exp = torch.exp(data - data_max.values)
        sum_data_exp = data_exp.sum(0, keepdim=True)
        return data_exp / sum_data_exp
