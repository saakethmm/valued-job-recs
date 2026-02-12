# Job Recommendation System TODOs

## One-Time Setup
- [x] Create customized fields in Notion corresponding to all of the necessary fields (have Claude create these for me)
  - [x] for enrichment, need some more description for skills fit rather than just reducing it to a single number maybe... (like number of years experience which all might matter more than language knowledge)

- [ ] batch processing below
  - [ ] load all files in one session, then do enrichment one job at a time (not multi-agent), auto-compress context, doesn't matter, only the three main files should remain intact.
    - [ ] might be worth auto-summarizing before any enrichment, on job pasting (using claude web using the same markdown files to condense information accordingly)
    - [ ] definitely! no wonder I'm running into usage problems, there's so much nonsense in the json file -> far better to run as plaintext or at least make much more plain (e.g., content field, then also plain text field repeating the same thing -> then so much for EVERY DAMN OBJECT, if it's paragraph, bold, etc. -> all NEW entries in JSON duplicated across content/plaintext. this is wild...)
      - if there was a way to intercept mcp retrieval and convert everything to plaintext this would solve issue! 
  - [ ] Run extraction + scoring on all "Not Started" / "In Progress" applications
  - [ ] rejections also

- [ ] Check structure of preferences.md, ensure it includes contrastive examples, run a sample run for cold-start
  - [ ] ...using jobs I actually applied to / got interviews

- [ ] sort of a combination of all three (contrastive examples via preferences, constitution of values, decision questions are involved using enriched text + CLAUDE.md)?
- [ ] add a template version of enrichment schema

*drawback of MCP*: guzzles context, for each tool use request both the parameters to the tool and the result are written to context, which makes it very inefficient...
* interesting sort of work done here -> balances trade-off between context (serial approach, longer but less memory) and duplication (parallel, shorter but more duplication of context): decided for my use case (in order to not hit session limits), to use a serial approach instead. classic instantiation of time/memory tradeoff.


## Future Improvements

- [ ] Automate extraction when new job is clipped (Notion API webhook?)
- [ ] Build simple UI or CLI to query recommendations
- [ ] add ability to mcp to create/delete/update notion fields themselves
