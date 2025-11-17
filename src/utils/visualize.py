import matplotlib.pyplot as plt

def plot_metrics(metrics: dict, filename: str):
    """
    Generates and saves a plot of semantic similarity and lexical distance over iterations.

    Args:
        metrics (dict): A dictionary of metrics, including metrics_over_time.
        filename (str): The path to save the plot to.
    """
    metrics_over_time = metrics.get("metrics_over_time", [])
    if not metrics_over_time:
        print("No metrics to plot.")
        return

    iterations = [m["iteration"] for m in metrics_over_time]
    semantic_similarity = [m["semantic_similarity"] for m in metrics_over_time]
    lexical_distance = [m["lexical_distance"] for m in metrics_over_time]

    fig, ax1 = plt.subplots(figsize=(10, 6))

    color = 'tab:red'
    ax1.set_xlabel('Iteration')
    ax1.set_ylabel('Semantic Similarity', color=color)
    ax1.plot(iterations, semantic_similarity, color=color, marker='o', label='Semantic Similarity')
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()
    color = 'tab:blue'
    ax2.set_ylabel('Lexical Distance', color=color)
    ax2.plot(iterations, lexical_distance, color=color, marker='x', label='Lexical Distance')
    ax2.tick_params(axis='y', labelcolor=color)

    fig.tight_layout()
    plt.title('Semantic Similarity and Lexical Distance Over Iterations')
    plt.savefig(filename)
    plt.close()
