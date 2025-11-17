import pytest
from src.pipeline.metrics import calculate_semantic_similarity, calculate_lexical_distance

def test_calculate_semantic_similarity():
    # Example inputs
    text1 = "The quick brown fox jumps over the lazy dog."
    text2 = "A fast brown fox leaps over a sleepy dog."
    
    # Expected output (this should be determined based on your similarity function)
    expected_similarity = 0.85  # Placeholder value, adjust based on your implementation
    
    # Calculate similarity
    similarity = calculate_semantic_similarity(text1, text2)
    
    # Assert the similarity is within an acceptable range
    assert abs(similarity - expected_similarity) < 0.1

def test_calculate_lexical_distance():
    # Example inputs
    text1 = "The quick brown fox"
    text2 = "The quick brown dog"
    
    # Expected output (this should be determined based on your distance function)
    expected_distance = 1  # Placeholder value, adjust based on your implementation
    
    # Calculate lexical distance
    distance = calculate_lexical_distance(text1, text2)
    
    # Assert the distance is as expected
    assert distance == expected_distance

# Additional tests can be added here for other metrics functions as needed.