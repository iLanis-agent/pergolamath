import json, math

def jsnum(x):
    return int(x) if isinstance(x, float) and x == int(x) else x
def plural(n, word, form=None): return str(jsnum(n)) + " " + (word if n == 1 else (form or word + "s"))
def fmt(x): return str(jsnum(x))
def round1(x): return jsnum(math.floor(x * 10 + 0.5) / 10)

def rafter_plan(spanCm, pitchCm):
    if not (spanCm > 0) or not (pitchCm > 0):
        return {"error": "the span and the labeled pitch must be positive"}
    if spanCm < pitchCm:
        return {"error": "the span is shorter than one labeled pitch"}
    rafters = math.floor(spanCm / pitchCm) + 1
    spare = round1(spanCm - (rafters - 1) * pitchCm)
    if rafters <= 4: verdict = "a sparse roof"
    elif rafters <= 8: verdict = "a typical roof"
    else: verdict = "a dense roof"
    return {"rafters": rafters, "spare": spare, "verdict": verdict}

def post_plan(runCm, bayCm):
    if not (runCm > 0) or not (bayCm > 0):
        return {"error": "the run and the labeled bay must be positive"}
    bays = math.ceil(runCm / bayCm)
    posts = bays + 1
    if bays == 1: verdict = "a single bay"
    elif bays <= 3: verdict = "a modest run"
    else: verdict = "a long run"
    return {"bays": bays, "posts": posts, "verdict": verdict}

def shade_plan(widthCm, depthCm, coverPct):
    if not (widthCm > 0) or not (depthCm > 0):
        return {"error": "the width and depth must be positive"}
    if not (coverPct > 0) or not (coverPct <= 100):
        return {"error": "the labeled coverage must sit above 0 and at or under 100"}
    shade = round1(widthCm * depthCm / 10000 * coverPct / 100)
    if shade < 3: verdict = "a dappled corner"
    elif shade < 8: verdict = "a sitting spot"
    else: verdict = "a full terrace"
    return {"shade": shade, "verdict": verdict}

def render_rafter(r, spanCm, pitchCm):
    return ("A span " + fmt(spanCm) + " cm at a labeled " + fmt(pitchCm) + " cm pitch takes "
            + plural(r["rafters"], "rafter") + ", both ends included, with " + fmt(r["spare"]) + " cm of extra spacing - " + r["verdict"] + ".")

def render_post(r, runCm, bayCm):
    return ("A run " + fmt(runCm) + " cm long at a labeled " + fmt(bayCm) + " cm bay becomes "
            + plural(r["bays"], "bay") + " and " + plural(r["posts"], "post") + " - " + r["verdict"] + ".")

def render_shade(r, widthCm, depthCm, coverPct):
    return ("A footprint " + fmt(widthCm) + " cm x " + fmt(depthCm) + " cm at a labeled " + fmt(coverPct)
            + "% coverage throws " + fmt(r["shade"]) + " sq m of shade - " + r["verdict"] + ".")

cases = []
def add(fn, f, rf, args):
    r = f(*args)
    c = {"fn": fn, "args": args, "result": r}
    if "error" not in r: c["render"] = rf(r, *args)
    cases.append(c)

for a in [[300,60],[200,60],[500,60],[60,60],[0,60],[300,0],[365.5,60],[59,60],[450,50],[240,60]]:
    add("rafterPlan", rafter_plan, render_rafter, a)
for a in [[300,300],[600,300],[1500,300],[250,300],[0,300],[300,0],[901,300],[100.5,300],[2000,300],[450,200]]:
    add("postPlan", post_plan, render_post, a)
for a in [[300,300,50],[200,200,50],[500,400,50],[200,200,100],[0,300,50],[300,300,0],[300,300,101],[250.5,250.5,50],[400,300,40],[150,150,60]]:
    add("shadePlan", shade_plan, render_shade, a)
json.dump(cases, open("expected.json", "w"), separators=(",", ":"))
print(len(cases), "cases")
