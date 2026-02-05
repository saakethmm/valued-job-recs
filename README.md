# Valued Job Recommendations

A personalized job recommendation system using RAG-based personalization to surface roles that align with your values, mission, and skills.

## The Problem

When job hunting, it's overwhelming to decide which roles to focus on. You end up:
- Spending too much time on roles that don't matter
- Too little time on roles that align with your values
- No systematic way to learn from your own preferences

## The Solution

A daily recommendation flow that:
1. Understands your values and skills (static profile)
2. Learns from your feedback over time (dynamic preferences)
3. Compares against enriched job data (structured extraction)
4. Surfaces the best roles for today's constraints

## Architecture

```
/valued_job_recs/
├── values.md           # Your mission, motivations, non-negotiables
├── skills.md           # Your experience, technical skills, strengths
├── preferences.md      # Learned preferences (updated via feedback)
├── CLAUDE.md           # Instructions for the AI assistant
└── README.md           # This file

External:
└── Notion DB           # Job tracker with enriched fields
```

## How It Works

### Matching Dimensions

| You | Job |
|-----|-----|
| Mission/values (values.md) | Company mission, role purpose |
| Skills/experience (skills.md) | Required qualifications |
| Learned preferences (preferences.md) | Extracted job attributes |

### Scoring

```
Overall Fit = (Mission Alignment × w1) + (Skills Match × w2) + (Growth × w3) + (Practical × w4)
```

Weights start at defaults and adjust based on your feedback.

### Daily Flow

```
┌─────────────────────────────────────┐
│ 1. Check for un-enriched jobs       │
│    → Extract key info, update DB    │
├─────────────────────────────────────┤
│ 2. Load profile + preferences       │
│    → values.md, skills.md, prefs    │
├─────────────────────────────────────┤
│ 3. Query all active jobs            │
│    → Get structured data from DB    │
├─────────────────────────────────────┤
│ 4. Apply today's constraints        │
│    → "2 hours", "high alignment"    │
├─────────────────────────────────────┤
│ 5. Score and rank                   │
│    → Base scores × preference adj.  │
├─────────────────────────────────────┤
│ 6. Return recommendations           │
│    → Top N with reasoning           │
├─────────────────────────────────────┤
│ 7. Capture feedback                 │
│    → Update preferences.md          │
└─────────────────────────────────────┘
```

## Notion Database Fields

Required fields for the job tracker:

| Field | Type | Description |
|-------|------|-------------|
| Company Name | Title | Company name |
| Job Title | Text | Role title |
| Status | Select | Not Started, In Progress, Submitted, etc. |
| Job/Application Link | URL | Link to job posting |
| Mission Summary | Text | Extracted: what the company/role is about |
| Required Skills | Multi-select | Extracted: skills they're looking for |
| Mission Fit | Number (1-5) | Computed alignment with your values |
| Skills Match | Number (1-5) | Computed match with your skills |
| Overall Fit | Number | Composite score |
| Remote OK | Checkbox | Remote work available |
| Company Stage | Select | Startup, Growth, Enterprise |
| Enriched | Checkbox | Whether job has been processed |

## Feedback Loop

After each recommendation session:

1. **You provide feedback**: "Liked X because...", "Passed on Y because..."
2. **Preferences update**: Weights adjust, filters added
3. **Next session improves**: Recommendations reflect learned preferences

### Example Feedback → Preference Update

```
Feedback: "Scale AI isn't safety-focused enough"

Update to preferences.md:
- Soft penalty: "safety not central to mission"
- Weight adjustment: mission_alignment 0.4 → 0.5
```

## Key Concepts

- **RAG-based personalization**: No model fine-tuning; preferences loaded into context
- **In-context learning**: Model adapts via retrieved preferences, not weight updates
- **Cold start handling**: Initial recommendations use explicit values.md as prior
- **Enrichment**: One-time extraction of job info into structured fields

## Usage

Start a session with constraints:
> "I have 2 hours today, want high mission alignment, remote preferred"

Get recommendations with reasoning, provide feedback, repeat.
