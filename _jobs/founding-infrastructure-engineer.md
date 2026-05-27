---
title: Public AI Founding Infrastructure Engineer
host: Current AI
category: funded
status: open
location: Fully remote, with a preference for Europe, US, or Canada
commitment: Full-time contract
compensation: $50,000 over 3 months, with opportunity to transition to full-time employment after
order: 1
date_posted: 2026-05-15
summary: First dedicated infrastructure hire and technical owner of the Public AI Inference Utility's operational backbone.
---

This opportunity is funded by and offered in collaboration with [Current AI](https://currentai.org), a Paris-based nonprofit.

**Location:** Fully remote, with a preference for Europe, US, or Canada  
**Commitment:** Full-time contract  
**Compensation:** $50,000 over 3 months, with opportunity to transition to full-time employment after  
**Start date:** ASAP

Public AI is building the Public AI Inference Utility: a public-access point for sovereign and public AI models, governed as public infrastructure. Think water, electricity, public libraries, the BBC. The utility already serves Apertus (Switzerland) and SEA-LION (Singapore) to users around the world at [chat.publicai.co](https://chat.publicai.co) and [platform.publicai.co](https://platform.publicai.co), and we're scaling toward national-scale inference with partners including CSCS, AI Singapore, AI Sweden, and Barcelona Supercomputing Center.

Right now, we're a small, scrappy team punching above our weight. The utility runs, but it needs to run well—with the reliability, transparency, and operational maturity of real public infrastructure. That's where you come in.

You'll be our first dedicated infrastructure hire and the technical owner of the platform's operational backbone. You'll report directly to the CTO and shape how a public AI utility actually works in production.

## You will

This is a hands-on builder/maintainer/integrator role. In your first three months, you'll likely:

- Harden the platform for the Apertus 1.5 and Apertus 2 launch. Load test, build fallback routing, set up per-agent monitoring. This is a real public moment and the infrastructure has to hold.
- Build end-to-end observability across OpenWebUI, AWS, CSCS, and (ideally) Infomaniak. We need integrated trace analysis and analytics so we can help our compute partners improve uptime and meet real SLAs.
- Ship downtime warnings and fallback behavior, including in our Preview deployment. We should have had this months ago.
- Implement routing transparency and endpoint provenance. When someone uses our chat or API, they should be able to see — and verify — which backend served their inference. This is core to what makes us a public utility.
- Speed up chat.publicai.co. People are writing us off based on a limited preview experience. Fix that, whether by collapsing Preview into the main chat, expanding Preview's feature set, or something better we haven't thought of.
- Improve the platform overall as a public good. Two ideas we're excited about: (1) integrating an MCP server so an agent can make changes to the inference configuration, and (2) making the utility more transparent and contributable — closer to how a public utility or active open-source project operates, even though it's a live service rather than static code.
- Work upstream in the open-source stack we depend on. Submit compatibility PRs across open-source and open-weight components (OpenWebUI, vLLM, LiteLLM, and related projects), build demos that show how different pieces fit together in a real public AI deployment, and fill gaps in specific OS projects where our production needs aren't yet met.

You'll have wide latitude to set priorities. We need someone who sees what's broken and fixes it, not someone who waits for tickets.

## What we're looking for

**Required**

- Significant experience operating production inference or ML serving infrastructure — vLLM, model routing, multi-region deployments, GPU-backed services, or comparable
- Strong distributed systems and SRE instincts: observability, incident response, fallback design, capacity planning
- Comfort working across heterogeneous infrastructure partners (cloud providers, sovereign HPC centers, institutional IT)
- Experience orchestrating many stacks; for better or worse you will also probably have to take on orchestrating a bunch of open source projects and dealing with the bugs that come with that
- Maintainer and integrator energy — you like making systems reliable, legible, and contributable, and you take pride in operational excellence
- Ability to work mostly autonomously in a small team and travel occasionally for team workshops

**Most important: intrinsic motivation.**

This is a nonprofit, open-source project building public goods. We need someone who actually cares about that mission and wants to build infrastructure for the public, not for a series B. We're looking for smart, creative, scrappy, intrinsically motivated, and moderately rebellious people who will challenge themselves, challenge us, and push for better. If you need a manager to tell you what to ship next, this isn't the right role.

**Nice to have**

- Open-source maintainer experience, especially on infrastructure or platform projects — including merged PRs to projects you don't own
- A track record of compatibility work across open-weight models and the tooling around them
- Familiarity with OpenWebUI, vLLM, or similar inference stacks
- Experience with MCP, agent tooling, or programmatic infrastructure interfaces
- Experience working with large HPCs, e.g. national supercomputing centers
- Background working with research labs or public-sector technology
- Track record of making complex systems transparent and accessible to outside contributors

## Logistics

- **Location:** Fully remote, with a preference for the US, Canada, or Europe. Must be available for occasional team workshops.
- **Employment:** Starting as a full- or part-time contract, with the option to graduate to a full-time employee role.
- **Compensation:** Starting at $50,000 USD over three months, with room to scope upward for exceptional experience.
- **Reports to:** CTO

---

Send a note to [josh@publicai.co](mailto:josh@publicai.co) with whatever best represents you — CV, GitHub, projects you're proud of, things you've maintained, things you've broken and fixed. Tell us why public AI matters to you.

We read every application.

[← Back to all jobs](/jobs/)
