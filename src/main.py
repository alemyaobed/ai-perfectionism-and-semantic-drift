import os
import argparse
from dotenv import load_dotenv
from pipeline.iterate import run_iterations
from pipeline.metrics import calculate_metrics
from utils.logging import setup_logging
from utils.io import save_to_json
from utils.visualize import plot_metrics
from datetime import datetime


def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(
        description="Run AI perfectionism and semantic drift experiments."
    )
    parser.add_argument(
        "--prompt",
        type=str,
        default="What are the implications of AI in modern society?",
        help="The initial prompt to start the process.",
    )
    parser.add_argument(
        "--model_a", type=str, default="gpt-4", help="The name of the first model."
    )
    parser.add_argument(
        "--model_b",
        type=str,
        default="gpt-3.5-turbo",
        help="The name of the second model.",
    )
    parser.add_argument(
        "--iterations", type=int, default=10, help="The number of iterations."
    )
    args = parser.parse_args()

    # Load environment variables
    load_dotenv()

    # Set up logging
    setup_logging()

    # Get API key from environment variables
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError(
            "API key not found. Please set the OPENAI_API_KEY in the .env file."
        )

    # Run the iterative prompting setup
    results = run_iterations(
        api_key, args.prompt, args.model_a, args.model_b, args.iterations
    )

    # Calculate metrics based on results
    metrics = calculate_metrics(results)

    # Save the results and metrics to a file
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"results/results_{timestamp}.json"
    plot_filename = f"results/results_{timestamp}.png"
    data_to_save = {
        "prompt": args.prompt,
        "model_a": args.model_a,
        "model_b": args.model_b,
        "iterations": args.iterations,
        "results": results,
        "metrics": metrics,
    }
    save_to_json(data_to_save, filename)
    print(f"Results saved to {filename}")

    # Plot the metrics
    plot_metrics(metrics, plot_filename)
    print(f"Plot saved to {plot_filename}")


if __name__ == "__main__":
    main()
