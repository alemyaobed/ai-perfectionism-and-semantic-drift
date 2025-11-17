import pytest
from src.pipeline.iterate import iterative_prompting

def test_iterative_prompting():
    # Test setup
    initial_prompt = "What are the benefits of AI in education?"
    expected_outputs = [
        "AI can personalize learning experiences.",
        "AI can automate administrative tasks.",
        "AI can provide real-time feedback to students."
    ]
    
    # Run the iterative prompting function
    outputs = iterative_prompting(initial_prompt, iterations=3)

    # Check if the outputs contain expected elements
    for expected in expected_outputs:
        assert any(expected in output for output in outputs), f"Expected output '{expected}' not found in results."

def test_semantic_drift():
    # Test setup
    original_output = "AI can enhance learning through personalized experiences."
    modified_output = "AI can improve education by tailoring learning to individual needs."

    # Check for semantic similarity
    drift = calculate_semantic_drift(original_output, modified_output)

    # Assert that drift is within acceptable limits
    assert drift < 0.5, "Semantic drift is too high."

def test_iteration_cost():
    # Test setup
    prompt = "Explain the significance of data privacy."
    
    # Measure the cost of iterations
    cost = measure_iteration_cost(prompt, iterations=5)

    # Assert that the cost is within expected bounds
    assert cost < 100, "Iteration cost exceeds expected limits."