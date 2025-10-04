# AI Perfectionism and Semantic Drift: Research Plan

## 🧠 Research Focus

This project investigates how **iterative AI-generated suggestions**, intended to improve quality, may actually **hinder productivity** and cause **semantic drift** — especially for users who seek perfection or fast validation in writing or coding tasks.

---

## 🎯 Research Question

> **Do iterative AI suggestions, intended to improve quality, actually hinder productivity or conceptual clarity for users who seek perfection or fast validation?**

---

## 🔍 Motivation

AI tools like ChatGPT or GitHub Copilot offer iterative improvements — constantly tweaking outputs to make them “better.” While helpful, this behavior can:

- Encourage perfectionist loops that **slow down progress**.
- Cause **semantic drift**, where the AI’s iterations move away from the user’s original intent or core idea.
- Be particularly problematic for users who rely on quick feedback to validate their work and move forward.

Understanding this phenomenon can inform better design of AI interfaces — e.g., “fast validation” modes vs. “iterative improvement” modes.

---

## 📌 Hypotheses

- **H1**: Iteration count increases semantic drift from the original answer (A₁ → Aₙ).
- **H2**: Different model pairs (same model vs. different models; low temp vs. high temp) produce different drift rates.
- **H3**: Simulated perfectionist prompts (asking for more improvement each time) result in greater drift and lower productivity than fast-validation prompts.

---

## 🧪 Methodology

### 1. Iterative Prompting Setup

Simulate a user trying to perfect an answer through repeated AI interactions:

1. **Start with a prompt (P)** — e.g., essay question or code task.
2. **Feed P to Model A** → Output A₁
3. **Feed (P, A₁) to Model B**, prompting:  
   _"I answered this way. What do you think, any improvements?"_ → Output A₂
4. **Feed (P, A₂) to Model A**, pretending it’s a “manually tweaked” version.
5. Repeat for **N iterations** (e.g., 10–20).

At each step, **compare** the current output with the original (A₁).

---

### 2. Measurement Metrics

#### ✅ Quantitative Metrics

- **Semantic similarity** (e.g., using sentence embeddings + cosine similarity)
- **Lexical distance** (edit distance, ROUGE, BLEU)
- **Topic shift** (LDA topics or clustering)
- **Named entity drift** (new names/claims introduced)
- **Iteration cost** (tokens used, time per step)

#### ✅ Qualitative / Human Metrics

- **Human ratings of core idea retention** (Likert scale: 1–5)
- **Willingness to accept output and move on** (Yes/No)
- **Time to decision**

---

### 3. Experimental Variables

- **Prompt Type**: Essay, technical explanation, or code-related
- **Model Pairing**: Same model vs. alternating models (e.g., GPT-4o and GPT-3.5)
- **Temperature**: Low (0.0), medium (0.7), high (1.0)
- **Persona Style**:
  - *Perfectionist*: “Make it better, expand this more…”
  - *Fast Validator*: “Is this okay? Should I stop here?”

---

## 🛠️ Tools & Technologies

- Python (OpenAI API, requests)
- SentenceTransformers (`all-mpnet-base-v2`)
- `editdistance`, `nltk`, `scikit-learn`, `pandas`
- Optionally: Jupyter or Colab for visualization and analysis

---

## 📈 Expected Deliverables

- 📄 2–4 page research report (summary, results, plots)
- 📊 Graphs: Similarity vs. Iteration, Edit Distance over Iteration
- 📂 GitHub Repo: Scripts, Prompt Logs, Example Outputs
- ✅ README explaining how to reproduce results

---

## ⏳ Suggested Timeline (2–4 Weeks)

| Week | Tasks |
|------|-------|
| 1    | Finalize prompts, build iteration loop script |
| 2    | Run experiments, collect outputs |
| 3    | Run similarity and distance metrics, start human evaluation |
| 4    | Analyze results, create plots, write report and README |

---

## ⚠️ Limitations

- Results depend on API randomness and model updates
- Small user sample size for human evaluation
- Assumes user follows model suggestions, which might not reflect all real behaviors

---

## 🧩 Future Extensions

- Add real user testing (record human behavior in a live prompt loop)
- Extend to visual or audio outputs
- Explore effects in creative writing vs. factual writing

---

## 📎 References

- [OpenAI API docs](https://platform.openai.com/docs)
- [SentenceTransformers](https://www.sbert.net/)
- Papers on semantic drift, human-AI interaction, and perfectionism in usability studies

