def calculate_costs(crew_usage_metrics, model_input_price, model_output_price, unit_of_tokens=1000):
    """
    Calculate the costs based on crew usage metrics and token pricing.
    
    Parameters:
    crew_usage_metrics (dict): A dictionary from result.token_usage or crew.usage_metrics.
    model_input_price (float): Cost per unit (e.g., per 1K tokens) for input tokens.
    model_output_price (float): Cost per unit for output tokens.
    unit_of_tokens (int): The number of tokens per unit cost (e.g., 1000).
    
    Returns:
    dict: A dictionary with the calculated costs.
    """
    prompt_tokens = crew_usage_metrics.get('prompt_tokens', 0)
    completion_tokens = crew_usage_metrics.get('completion_tokens', 0)

    input_cost = (prompt_tokens / unit_of_tokens) * model_input_price
    output_cost = (completion_tokens / unit_of_tokens) * model_output_price
    total_cost = input_cost + output_cost

    return {
        'total_cost': total_cost,
        'input_cost': input_cost,
        'output_cost': output_cost
    }