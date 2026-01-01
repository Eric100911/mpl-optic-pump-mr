TEXFILE = Report/report
BIBFILE = Report/report
PREPFILE = Prep/prep
PREPNAME = prep
TEXNAME = report

.PHONY: all prep report clean

all: $(TEXFILE).pdf ${PREPFILE}.pdf

prep: ${PREPFILE}.pdf

report: $(TEXFILE).pdf

$(TEXFILE).pdf: $(TEXFILE).tex $(BIBFILE).bib
	rm -f $(TEXFILE).aux $(TEXFILE).out $(TEXFILE).log $(TEXFILE).toc $(TEXFILE).bbl $(TEXFILE).blg $(TEXFILE).fls $(TEXFILE).fdb_latexmk
	mkdir -p build
	xelatex --halt-on-error -output-directory=build $(TEXFILE).tex
	bibtex build/$(TEXNAME).aux
	xelatex --halt-on-error -output-directory=build $(TEXFILE).tex
	xelatex --halt-on-error -output-directory=build $(TEXFILE).tex
	cp build/$(TEXNAME).pdf $(TEXFILE).pdf

${PREPFILE}.pdf: ${PREPFILE}.tex
	rm -f ${PREPFILE}.aux ${PREPFILE}.out ${PREPFILE}.log ${PREPFILE}.toc ${PREPFILE}.fls ${PREPFILE}.fdb_latexmk
	mkdir -p build
	xelatex --halt-on-error -output-directory=build ${PREPFILE}.tex
	bibtex build/${PREPNAME}.aux
	xelatex --halt-on-error -output-directory=build ${PREPFILE}.tex
	xelatex --halt-on-error -output-directory=build ${PREPFILE}.tex
	cp build/${PREPNAME}.pdf ${PREPFILE}.pdf

clean:
	rm -f build/*
	rm -f $(TEXFILE).pdf
	rm -f ${PREPFILE}.pdf
