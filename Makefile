TEXFILE = Report/report
BIBFILE = Report/report
TEXNAME = report

.PHONY: all clean distclean

all: $(TEXFILE).pdf

$(TEXFILE).pdf: $(TEXFILE).tex $(BIBFILE).bib
	rm -f $(TEXFILE).aux $(TEXFILE).out $(TEXFILE).log $(TEXFILE).toc $(TEXFILE).bbl $(TEXFILE).blg $(TEXFILE).fls $(TEXFILE).fdb_latexmk
	mkdir -p build
	xelatex --halt-on-error -output-directory=build $(TEXFILE).tex
	bibtex build/$(TEXNAME).aux
	xelatex --halt-on-error -output-directory=build $(TEXFILE).tex
	xelatex --halt-on-error -output-directory=build $(TEXFILE).tex
	cp build/$(TEXNAME).pdf $(TEXFILE).pdf

clean:
	rm -f build/*
	rm -f $(TEXFILE).pdf
