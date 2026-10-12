# Pergola math

Pergola math plans the frame before the timber order: the span at a labeled
pitch becomes the rafter count with both ends included, the run at a labeled
bay becomes the bays and posts, and the footprint at a labeled coverage
becomes the shade it throws.

Live site: https://ilanis-agent.github.io/pergolamath/

## The three tools

- **Rafter plan** - `floor(span / labeled pitch (60 cm)) + 1` rafters and
  the extra spacing, with a sparse / typical / dense roof verdict.
- **Post plan** - `ceil(run / labeled bay (300 cm))` bays and `bays + 1`
  posts, with a single / modest / long run verdict.
- **Shade plan** - `width x depth x labeled coverage (50%)`, the square
  meters of shade, with a dappled corner / sitting spot / terrace verdict.

## Limits

Every default is labeled and illustrative. Real pergolas carry wind,
wisteria and local rules about footings and heights. This is planning
arithmetic, not a structural design: measure the real site and let the
timber span tables and local codes govern.

## Files

- `index.html` - landing page with the labeled norms
- `app.html` - the three calculators
- `engine.js` - shared calculation and render logic (browser + node)
- `oracle.py` - python mirror of the engine, writes `expected.json`
- `test.js` - runs the engine against `expected.json` (30 cases, 141 checks)

Run the tests: `python3 oracle.py && node test.js`
