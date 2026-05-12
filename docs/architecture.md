# Architecture

## Goal

Represent a care operations command layer that helps coordination teams decide which patient pathway needs intervention first, why it is at risk, and which lane should own the next move.

## Core model

- `patient pathways`
  - current stage
  - owner lane
  - delay pressure
  - outreach friction
  - next-best action
- `handoffs`
  - source lane
  - destination lane
  - severity
  - causal barrier
  - regulatory or quality pressure

## Service behavior

`CarePathwayService` loads sample pathway data and decorates each patient with a normalized queue lane:

- `escalate`
  - severe risk or extended delay
- `watch`
  - moderate friction that still deserves fast action
- `clear`
  - on-plan pathways with low coordination pressure

## Experience surfaces

- `/`
  - executive overview
- `/queue`
  - patient-level coordination queue
- `/handoffs`
  - cross-team gap visibility
- `/api-summary`
  - sample downstream integration payload

## Why this repo is useful

This repo is deliberately operational rather than clinical. It does not attempt diagnosis or treatment selection. Instead, it focuses on pathway continuity, coordination pressure, and the institutional mechanics that determine whether follow-up plans actually happen.
