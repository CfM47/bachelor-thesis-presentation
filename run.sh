#!/bin/bash

# Run the presentation, this depends on uv and manim-slides being installed in the current environment

uv run manim-slides render main.py && uv run manim-slides convert --to html presentation.html