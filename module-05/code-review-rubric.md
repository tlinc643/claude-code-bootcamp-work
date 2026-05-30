# Module 05 Code Review Rubric

## Purpose

This rubric is used to review AI-generated code before accepting it.

## Checklist

- Does the code satisfy the original requirements?
- Does it avoid unnecessary complexity?
- Are files created only in the expected folder?
- Are dependencies necessary and listed clearly?
- Are errors handled with clear status codes or messages?
- Are tests written against the real implementation?
- Do tests cover success cases and failure cases?
- Do tests avoid copying application logic into the test file?
- Can the app be run and tested with documented commands?
- Is the code readable enough for a human to maintain?

## Specific Lesson from Module 05

The tests must import and exercise the real application code. Passing tests are not meaningful if the test file recreates or mocks the actual implementation too heavily.

## Go / No-Go Rule

Accept the code only if:

- the app runs;
- tests pass;
- the implementation is understandable;
- the test suite covers the main API behavior;
- no unrelated files or unnecessary dependencies were added.
