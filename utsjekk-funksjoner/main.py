import overlap

print(
    f"[1-3] and [2-4]. Overlap? {'yes :)' if overlap.intervals_overlap((1,3), (2,4)) else 'no :('}"
)
