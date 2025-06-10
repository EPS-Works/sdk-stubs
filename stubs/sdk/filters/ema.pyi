class ExponentialMovingAverage:
    """An exponential moving average (EMA) filter for smoothing time-series data.

    The EMA filter applies exponential smoothing to a sequence of values, reducing noise
    while preserving trends. It is commonly used in signal processing, sensor data filtering,
    and financial analysis.
    """
    def __init__(self, alpha: float) -> None:
        """Initializes the EMA filter with a given smoothing factor.

        Args:
            alpha: Smoothing factor (0 < alpha ≤ 1).
                  - Closer to 1: More responsive to recent changes (less smoothing).
                  - Closer to 0: Stronger smoothing (slower to adapt to changes).

        Raises:
            ValueError: If `alpha` is not in the range (0, 1].
        """
    def apply(self, value: float) -> float:
        """Update the filter with a new value and return the smoothed result.

        Args:
            value: The latest input value to incorporate into the EMA.

        Returns:
            The current smoothed value after applying exponential smoothing.
        """
