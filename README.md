# Kramdown Preview

Simple Sublime Text 3 plugin making it possible to easily render currently edited
[kramdown](https://kramdown.gettalong.org/) document using a web browser.

![Example](res/example.png)

Also works for Markdown (since kramdown is a superset).
Useful for quick live-preview of documents such as READMEs.

Integrated with [MathJax](https://www.mathjax.org/), so mathematical formulas 
written using LaTeX will render as expected.

## Dependencies

1. Kramdown - must be available under PATH as `kramdown`.
2. Web browser - must be available under PATH as `sensible-browser` (this works
	by default in most Debian-based Linux distributions).

## Installation

Clone the repository into Sublime `Packages` directory (below is default for Linux):

`$ git clone https://github.com/drabard/kramdown-preview-sublime ~/.config/sublime-text-3/Packages`

## Usage

Press the associated key combination (default: `Ctrl + Alt + Shift + m`) 
while editing a buffer in ST3. It is going to be interpreted as kramdown and 
rendered in your web browser.
