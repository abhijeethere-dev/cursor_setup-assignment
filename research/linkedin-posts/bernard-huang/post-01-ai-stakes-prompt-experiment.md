# Bernard Huang — LinkedIn Post 01

**Author:** Bernard Huang  
**Profile:** https://www.linkedin.com/in/bernardjhuang/  
**Date:** June 2026 (4 days ago)  
**Topic:** AI Prompting Experiment — Stakes-Based Prompting Improves Output Quality 24%

---

**Key Insight:** Bernard ran a controlled experiment showing that adding false urgency/stakes to AI prompts produces measurably better output — raising an important ethical and practical question for AI content production workflows.

**Experiment results:**
- Audit score jumped from 55/81 to 68/81 (24% improvement) when told "I will lose my job"
- API audit: stakes version caught 6 P0 bugs the polite version missed, including duplicate JSON keys
- Comparison page audit: 16/16 dimensions scored at highest level vs 3/16 in control
- Gemini 3.1 Pro graded both runs blind — same verdict: stakes version "significantly better"

**Three open questions Bernard raises:**
1. Is signaling false stakes "manipulation"? Of what, exactly?
2. If a technique only works when we lie, do we use it in production?
3. What happens when models get good enough to call our bluff?

**Why this matters for AI SEO:** If prompt engineering with stakes framing produces 24% better content audits and page optimizations, this is directly actionable for AI-powered SEO content production workflows.

---

**Raw post text:**

I lied to an AI yesterday. I told it I would lose my job if it didn't audit my work properly.

The audit score went from 55/81 to 68/81. The same model handed me 24% better work for the lie.

I ran this twice:
- API audit: the stakes version caught 6 P0 bugs the polite version missed, including duplicate JSON keys in a public spec
- Comparison page audit: 16 of 16 dimensions scored at highest level vs 3 of 16 in the control

Gemini 3.1 Pro graded both runs blind. Same verdict: the stakes version was "significantly better."

If the model gives me 24% better work when I claim I'm about to be ruined, what is it doing the other 99% of the time when I ask politely?