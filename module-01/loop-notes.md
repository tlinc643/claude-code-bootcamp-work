Think of Claude as a capable junior engineer who needs clear direction: you Plan by writing a precise spec or
  prompt (the ticket), then Claude Implements by writing the code (the first draft PR), then you Test by running
  it and checking edge cases (QA), then you Review by reading every line Claude touched as if you were the
  senior on the team — because you are (the approval gate), and finally you Commit only what you'd be proud to
  have in git log forever. The junior can move fast and cover a lot of ground, but they don't know your
  codebase's hidden constraints, security requirements, or team conventions the way you do. Skipping Review is
  the most common failure mode because it turns Claude's confident-sounding output directly into production
  code, and confident is not the same as correct.
