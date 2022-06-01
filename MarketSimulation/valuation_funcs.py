from classes import Company

def ddm_valuation(company:Company,growth_rate:float,discount_rate:float) -> float:
    """Return the value estimate of the stock, if appropriate parameters are provided. Assumed perpetual dividend.
    """
    if growth_rate > discount_rate:
        raise Exception(f'Growth rate of {growth_rate} is greater than the discount rate of {discount_rate}. You broke math.')
    
    security_value = company.last_dividend * (1+growth_rate) / (discount_rate-growth_rate)

    return security_value