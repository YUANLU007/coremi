# Vision

## News Needs More Than a Better Model

Language models can summarize, draft, compare, and calculate. None of those capabilities automatically creates trustworthy journalism.

A newsroom must still decide:

- which question is worth answering;
- which sources deserve authority;
- what a number actually measures;
- where two accounts conflict;
- which inference is fair;
- when the evidence is too weak to publish;
- who is accountable for the final judgment.

These are operating decisions, not text-generation features.

## The Harness Engineering Thesis

As models improve, the durable advantage moves outward from the model itself to the system around it.

For software agents, that surrounding system is often called a harness: the context, tools, permissions, state, checks, outputs, and recovery paths that turn model capability into dependable work.

**News Harness applies harness engineering to journalism and investment research.**

The objective is not to reveal a model's private reasoning. The objective is to preserve the work a newsroom actually needs to inspect: sources, claims, calculations, disagreements, decisions, revisions, and final accountability.

## From Prompt to Institution

A prompt can request good behavior. A harness makes good behavior observable and repeatable.

| A prompt says | A harness enforces |
|---|---|
| use strong sources | record source level and supported claim |
| verify the facts | produce claim-level verdicts before drafting |
| be transparent | save readable artifacts and state transitions |
| avoid hallucination | stop or qualify when evidence is insufficient |
| write a balanced article | require a counter-thesis and unresolved risks |
| improve the answer | return work to the exact stage that failed |

This is how an AI workflow begins to resemble an institution rather than a chat window.

## Editorial Judgment Is Not an Error Condition

News is not a database query with one mechanically correct output. Evidence can be incomplete, incentives can distort testimony, and material facts can change while a story is being written.

News Harness therefore treats uncertainty, disagreement, and editorial return as first-class states. The system can say:

- verified;
- qualified;
- disputed;
- unverified;
- false;
- revise;
- hold.

A system that cannot stop is not autonomous. It is uncontrolled.

## Why Open Source

The public value is not Coremi's private data or production infrastructure. It is the operating contract that others can inspect, test, criticize, and adapt.

Open sourcing the harness makes several questions discussable:

- What evidence should an agent need before it may write a claim?
- Which state belongs in files rather than conversation memory?
- How should a research run recover after a failed tool call?
- When should the system ask a human to decide?
- How can one model be replaced without rewriting the newsroom?
- How do we evaluate an article and the process that produced it?

## What Success Looks Like

News Harness succeeds when:

1. a small newsroom can run deep research without losing editorial control;
2. a reviewer can trace a material claim back to its evidence and stage;
3. a failed run can resume without starting over;
4. a model or tool can be replaced without breaking the artifact contract;
5. contributors improve reliability with testable changes, not grander claims;
6. the final publication still has a responsible human editor.

## Relationship to Coremi

Coremi is a journalism and judgment-intelligence product. News Harness is the open-source harness-engineering layer developed from its newsroom practice.

The product may evolve. The open contract should remain portable.

---

**The model generates. The harness governs. The editor decides.**
