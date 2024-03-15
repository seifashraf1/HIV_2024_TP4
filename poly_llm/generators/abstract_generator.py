import abc
import typing
import numpy as np

class AbstractGenerator(abc.ABC):
    """Abstract class for all generators."""

    def __init__(self):
        """Initialize the generator.

        Args:
            config (dict): Dictionary containing the configuration parameters.
        """
        #self.size = solution_size
        self._name = "AbstractGenerator"


    @property
    def name(self) -> int:
        """Size of the phenotype.

        Returns:
            int: Size of the phenotype.
        """
        return self._name

    @abc.abstractmethod
    def generate_random_test(self)-> str:
        """Generate samples from the generator

        Returns:
            np.array: Generated samples.
        """
        pass

