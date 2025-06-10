from machine import ADC as ADC

__platform__: str
__firmware__: str

def get_board_revision(adc: ADC) -> str | None:
    '''Detect the hardware revision by measuring a voltage divider.

    This function uses an ADC to measure the voltage across a resistor network
    that uniquely identifies different hardware revisions. It performs multiple
    readings to ensure accuracy and compares the average voltage against known
    revision thresholds.

    Args:
        adc: ADC instance configured for hardware revision detection.

    Returns:
        Hardware revision string (e.g., "R03", "R04") if detected, None if
        the voltage does not match any known revision.
    '''
