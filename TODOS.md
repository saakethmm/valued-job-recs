# Job Recommendation System TODOs

## One-Time Setup
- [ ] Create customized fields in Notion corresponding to all of the necessary fields (have Claude create these for me)

- [ ] Check structure of preferences.md, ensure it includes contrastive examples, run a sample run for cold-start
  - [ ] Track which jobs you actually applied to / got interviews (add this as a guideline, start off with this)


- [ ] sort of a combination of all three (contrastive examples via preferences, constitution of values, decision questions are involved using enriched text + CLAUDE.md)?

## Per-Job Pipeline

1. **Clip job** → Notion Web Clipper → New page with company, title, description
2. **Enrich job** from description:
   - Required skills, experience level, domain
   - Product purpose, AI application, human element
   - Company mission/values
3. **Score job** using chosen approach
4. **Store results** (score, reasoning, matched criteria)

## Batch Processing (Existing Jobs)

- [ ] Run extraction + scoring on all "Not Started" / "In Progress" applications
- [ ] Populate Purpose field or local index with results


## Future Improvements

- [ ] Automate extraction when new job is clipped (Notion API webhook?)
- [ ] Build simple UI or CLI to query recommendations
