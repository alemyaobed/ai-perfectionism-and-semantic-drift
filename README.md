# AI Perfectionism and Semantic Drift: Research Project

## Overview

This project investigates the impact of iterative AI-generated suggestions on productivity and semantic clarity, particularly for users who strive for perfection or quick validation in writing and coding tasks. The goal is to understand how these suggestions can lead to semantic drift and hinder progress.

#### Question:

> Do iterative AI suggestions, intended to improve quality, actually hinder productivity or conceptual clarity for users who seek perfection or fast validation?


## Project Structure

- **src/**: Contains the main application code.
  - **main.py**: Entry point for running experiments and analysis.
  - **config.py**: Configuration settings, including API key management.
  - **pipeline/**: Contains modules for handling iterative prompting, metrics calculation, analysis, and evaluation.
  - **models/**: Includes code for interacting with AI models and generating sentence embeddings.
  - **utils/**: Utility functions for I/O operations and logging.

- **prompts/**: Contains example prompts for various tasks (essay, technical, coding).

- **notebooks/**: Jupyter notebook for exploratory data analysis.

- **docs/**: Research plan and methodology documentation.

- **tests/**: Unit tests for the application.

- **.env.example**: Template for environment variables, including API key placement.

- **requirements.txt**: Lists project dependencies.

- **pyproject.toml**: Project configuration file.

- **.gitignore**: Specifies files to ignore in version control.

## Setup Instructions

1. **Clone the Repository**: 
   ```
   git clone <repository-url>
   cd ai-perfectionism-and-semantic-drift
   ```

2. **Create a Virtual Environment**:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```
   pip install -r requirements.txt
   ```

4. **Download SpaCy Model**:
   ```
   python -m spacy download en_core_web_sm
   ```

5. **Set Up Environment Variables**:
   - Copy `.env.example` to `.env` and add your OpenAI API key:
     ```
     cp .env.example .env
     ```
   - Open `.env` and add your API key:
     ```
     OPENAI_API_KEY=your_api_key_here
     ```

## Usage

The application can be run from the command line with several arguments to control the experiment.

```bash
python src/main.py [OPTIONS]
```

**Options:**

*   `--prompt`: The initial prompt to start the process. (Default: "What are the implications of AI in modern society?")
*   `--model_a`: The name of the first model. (Default: "gpt-4")
*   `--model_b`: The name of the second model. (Default: "gpt-3.5-turbo")
*   `--iterations`: The number of iterations. (Default: 10)

**Example:**

```bash
python src/main.py --prompt "Explain the concept of photosynthesis in simple terms." --model_a "gpt-3.5-turbo" --model_b "gpt-3.5-turbo" --iterations 5
```

## Testing

Unit tests are provided in the `tests/` directory. You can run them using:
```
pytest tests/
```

## Future Work

- Conduct real user testing to observe behavior in live prompting scenarios.
- Extend the project to include visual or audio outputs.
- Explore the effects of AI suggestions in different writing contexts (creative vs. factual).

## License

This project is licensed under the MIT License. See the [LICENSE file](./LICENSE) for details.