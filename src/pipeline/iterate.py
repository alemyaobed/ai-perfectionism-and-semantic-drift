from src.models.openai_client import OpenAIClient


def iterative_prompting(
    prompt: str,
    model_a: OpenAIClient,
    model_b: OpenAIClient,
    model_a_name: str,
    model_b_name: str,
    iterations: int = 10,
):
    outputs = []
    current_output = prompt
    first_output = model_a.generate_response(current_output, model=model_a_name)
    outputs.append(first_output)

    # for i in range(iterations - 1):
    #     # Feed the current output to model A
    #     output_a = model_a.generate_response(current_output, model=model_a_name)
    #     outputs.append(output_a)

    #     # Feed the output from model A to model B for improvement
    #     current_output = model_b.generate_response(
    #         f"I answered this question: {prompt} in this way: {output_a}. What do you think, any improvements?",
    #         model=model_b_name,
    #     )
    for i in range(iterations - 1):
        # # Feed the current output to model A
        # output_a = model_a.generate_response(current_output, model=model_a_name)
        # outputs.append(output_a)

        # Feed the output from model A to model B for improvement
        current_output = model_a.generate_response(
            f"I answered this question: {prompt} in this way: {outputs[-1]}. What do you think, any improvements? If there are please provide a revised answer.",
            model=model_a_name,
        )
        outputs.append(current_output)

    return outputs


def iterative_prompting_b(
    prompt: str,
    model_a: OpenAIClient,
    model_b: OpenAIClient,
    model_a_name: str,
    model_b_name: str,
    iterations: int = 10,
):
    outputs = []
    current_output = prompt
    first_output = model_a.generate_response(current_output, model=model_a_name)
    outputs.append(first_output)
    current_output = first_output

    # for i in range(iterations - 1):
    #     # Feed the current output to model A
    #     output_a = model_a.generate_response(current_output, model=model_a_name)
    #     outputs.append(output_a)

    #     # Feed the output from model A to model B for improvement
    #     current_output = model_b.generate_response(
    #         f"I answered this question: {prompt} in this way: {output_a}. What do you think, any improvements?",
    #         model=model_b_name,
    #     )
    for i in range(iterations - 1):
        # # Feed the current output to model A
        output_a = model_a.generate_response(
            f"I answered this question: {prompt} in this way: {current_output}. What do you think, any improvements? If there are please provide a revised answer.",
            model=model_a_name,
        )
        outputs.append(output_a)

        # Feed the output from model A to model B for improvement
        current_output = model_b.generate_response(
            f"I answered this question: {prompt} in this way: {outputs[-1]}. What do you think, any improvements? If there are please provide a revised answer.",
            model=model_b_name,
        )

    return outputs


def run_iterations(
    api_key: str,
    initial_prompt: str,
    model_a_name: str = "gpt-4",
    model_b_name: str = "gpt-3.5-turbo",
    iterations: int = 10,
):
    """
    Runs the iterative prompting process.

    Args:
        api_key (str): The OpenAI API key.
        initial_prompt (str): The initial prompt to start the process.
        model_a_name (str, optional): The name of the first model. Defaults to "gpt-4".
        model_b_name (str, optional): The name of the second model. Defaults to "gpt-3.5".
        iterations (int, optional): The number of iterations. Defaults to 10.

    Returns:
        list: A list of outputs from each iteration.
    """
    model_a = OpenAIClient(api_key=api_key)
    model_b = OpenAIClient(api_key=api_key)

    results = iterative_prompting_b(
        initial_prompt, model_a, model_b, model_a_name, model_b_name, iterations
    )

    return results
