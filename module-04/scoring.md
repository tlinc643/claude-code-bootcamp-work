# Module 04 Scoring

## Goal

Compare two independent Claude-generated Notes API implementations and select a winner.

## Candidate A

### Strengths

- 

### Weaknesses

- 

### Test results

- Create note:
- List notes:
- Get note:
- Update note:
- Delete note:
- Error handling:

## Candidate B

### Strengths

- 

### Weaknesses

- 

### Test results

- Create note:
- List notes:
- Get note:
- Update note:
- Delete note:
- Error handling:

## Scoring

| Criterion | Candidate A | Candidate B |
|---|---:|---:|
| Correctness | /5 | /5 |
| Simplicity | /5 | /5 |
| Readability | /5 | /5 |
| Error handling | /5 | /5 |
| README usefulness | /5 | /5 |
| Overall fit | /5 | /5 |

## Winner

Winner:Candidate A

Reason: Why Candidate A won:
- Candidate A better matched the exercise examples because it used simple integer note IDs such as `/notes/1`.
- Candidate A was easier to test with the provided curl commands.
- Candidate A was simpler and more readable for a training exercise.
- Candidate B used UUIDs, which are more production-like, but this did not match the course examples.
- Candidate B’s UUID design caused the original `/notes/1` update test to fail.
- Candidate B’s DELETE behavior was valid, but the empty response body made the `json.tool` test command misleading.
- For a real production API, Candidate B’s UUID approach may be preferable.
- For this bootcamp exercise, Candidate A is the better fit.

Reason: Why Candidate B did not win:
* Candidate B uses UUID note IDs instead of simple integer IDs.
* This is realistic for production APIs, but it does not match the course example that used `/notes/1`.
* The first update test failed because I used `/notes/1`, but Candidate B expected a valid UUID.
* After listing the notes and copying the actual UUID, the update endpoint worked as expected.
* Candidate B’s DELETE endpoint appears to return an empty response body after successful deletion.
* Piping the DELETE response to `python3 -m json.tool` caused a parsing error because there was no JSON body to parse.
* This was a testing-command issue, not necessarily an API bug.
* The DELETE endpoint removed the note successfully.
* A second DELETE request for the same UUID returned `404 Not Found`.
* The second `404 Not Found` response is correct behavior because the note had already been deleted.
* Candidate B has more production-like ID handling because UUIDs are safer than predictable integer IDs.
* Candidate B is slightly less aligned with the exercise examples because the examples assumed simple numeric IDs.
* Candidate B should receive credit for correct delete behavior.
* Candidate B should lose a small amount of fit/alignment credit because the API examples in the exercise used integer-style IDs.

## Lessons Learned

- Best-of-N is useful because:
- The first implementation was/was not the best because:
- In future projects, I would use this workflow when:
