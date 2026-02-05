# Job Recommendation System TODOs

## One-Time Setup

- [ ] **Create profile document** (skills, experience, interests, values, what to avoid)
  - Location: Notion page, local file, or CLAUDE.md
  - Include: Python/PyTorch/ML skills, years of experience, healthcare/mental health interests, ikigai mission, things to avoid (pure research, addictive tech)
    - CV
    - Values cards
    - Who am I page in Notion
  
- [ ] **Decide storage location** for extracted job data
  - Option A: Notion properties (Purpose field, new custom fields)
  - Option B: Local index file (JSON/markdown in this folder)

- [ ] **Choose scoring approach(es)** to test
  - Approach A: LLM-as-Evaluator (decision questions)
  - Approach B: Constitution/Profile Match (preference statements)
  - Approach C: Contrastive Examples (labeled good/bad fits)

- [ ] **Define scoring criteria** for chosen approach
  - If A: Write 5-7 decision questions with scoring rubric
  - If B: Write constitution as preference statements
  - If C: Label 5-10 existing jobs as great/poor fit with reasons

## Per-Job Pipeline

1. **Clip job** → Notion Web Clipper → New page with company, title, description
2. **Extract structured info** from description:
   - Required skills, experience level, domain
   - Product purpose, AI application, human element
   - Company mission/values
3. **Score job** using chosen approach
4. **Store results** (score, reasoning, matched criteria)

## Batch Processing (Existing Jobs)

- [ ] Run extraction + scoring on all "Not Started" / "In Progress" applications
- [ ] Populate Purpose field or local index with results

## Approach Comparison

| Approach | Pros | Cons |
|----------|------|------|
| A: Decision Questions | Transparent, tunable scores | Need to define right questions |
| B: Constitution | Rich/nuanced matching | Less quantitative |
| C: Contrastive Examples | No explicit criteria needed | Needs good labeled examples |

## Future Improvements

- [ ] Automate extraction when new job is clipped (Notion API webhook?)
- [ ] Build simple UI or CLI to query recommendations
- [ ] Track which jobs you actually applied to / got interviews → refine model
